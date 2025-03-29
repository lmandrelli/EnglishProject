from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import auth, game
from .utils.auth import get_current_active_user
from .database.init_game_data import init_game_data

app = FastAPI(
    title="English Project API",
    description="API for giving questions and answers",
    version="0.0.1",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins - for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Inclure les routeurs
app.include_router(auth.router)
app.include_router(game.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/protected-route")
async def protected_route(user=Depends(get_current_active_user)):
    return {"message": f"Bonjour {user.username}, vous avez accès à cette route protégée"}

@app.on_event("startup")
async def startup_event():
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client["celestial_wordforge"]
    # Supprimez toutes les collections
    for collection in db.list_collection_names():
        db[collection].drop()
    # Puis initialisez
    init_game_data(force_update=True)
    print("Application démarrée et données réinitialisées")