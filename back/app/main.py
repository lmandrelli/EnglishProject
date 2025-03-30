import os

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pymongo import MongoClient

from dotenv import load_dotenv

from .routers import auth, game, leaderboard
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
app.include_router(leaderboard.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/protected-route")
async def protected_route(user=Depends(get_current_active_user)):
    return {"message": f"Bonjour {user.username}, vous avez accès à cette route protégée"}

@app.on_event("startup")
async def startup_event():
    load_dotenv()
    mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
    client = MongoClient(mongo_uri)
    db = client["celestial_wordforge"]
    # Supprimez toutes les collections
    for collection in db.list_collection_names():
        db[collection].drop()
    # Puis initialisez
    init_game_data(force_update=True)
    print("Application démarrée et données réinitialisées")
