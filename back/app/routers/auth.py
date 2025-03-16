from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from bson import ObjectId

from ..database.mongodb import users_collection
from ..models.user import UserCreate, Token, User, UserInDB
from ..utils.auth import (
    get_current_user,
    create_access_token,
    authenticate_user,
    get_password_hash,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/register", response_model=User)
async def register(user_data: UserCreate):
    # Vérifier si l'utilisateur existe déjà
    if users_collection.find_one({"email": user_data.email}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="L'email existe déjà dans le système"
        )
    
    # Créer un nouvel utilisateur
    user_dict = user_data.model_dump()
    hashed_password = get_password_hash(user_dict.pop("password"))
    
    user_in_db = UserInDB(
        **user_dict,
        hashed_password=hashed_password
    )
    
    # Insérer dans MongoDB
    result = users_collection.insert_one(user_in_db.model_dump())
    new_user_id = result.inserted_id
    
    # Retourner l'utilisateur créé
    return User(id=str(new_user_id), email=user_data.email, username=user_data.username)


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou mot de passe incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Mettre à jour la dernière connexion
    users_collection.update_one(
        {"_id": user["_id"]},
        {"$set": {"last_login": timedelta(minutes=0)}}
    )
    
    # Créer le token d'accès
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user