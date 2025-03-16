from pymongo import MongoClient
from pymongo.collection import Collection
import os
from dotenv import load_dotenv

load_dotenv()

# Récupération des variables d'environnement
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "celestial_wordforge")

# Connexion à MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Collections
users_collection = db["users"]

# Index pour les emails uniques
users_collection.create_index("email", unique=True)

def get_collection(collection_name: str) -> Collection:
    return db[collection_name]