from datetime import datetime
from bson import ObjectId
from ..database.mongodb import db
from ..models.leaderboard import LeaderboardEntry

def submit_score(user_id: str, username: str, score: int) -> bool:
    """
    Submit a new score for a user. If the user already has a score,
    update it only if the new score is higher.
    """
    collection = db["leaderboard"]
    
    # Check if user already has a score
    existing_entry = collection.find_one({"user_id": user_id})
    
    if existing_entry and existing_entry["score"] >= score:
        # Don't update if existing score is higher
        return False
    
    entry = LeaderboardEntry(
        user_id=user_id,
        username=username,
        score=score,
        created_at=datetime.utcnow()
    )
    
    if existing_entry:
        # Update existing entry
        collection.update_one(
            {"user_id": user_id},
            {"$set": {
                "score": score,
                "created_at": entry.created_at
            }}
        )
    else:
        # Create new entry
        collection.insert_one(entry.dict())
    
    return True

def get_top_scores(limit: int = 10):
    """
    Get the top scores from the leaderboard.
    Returns only the highest score per user.
    """
    collection = db["leaderboard"]
    
    # Sort by score descending and get top entries
    cursor = collection.find().sort("score", -1).limit(limit)
    
    # Convert cursor to list and format entries
    leaderboard = []
    for entry in cursor:
        entry["id"] = str(entry.pop("_id"))
        leaderboard.append(entry)
    
    return leaderboard

def get_user_score(user_id: str):
    """
    Get the score for a specific user.
    """
    collection = db["leaderboard"]
    entry = collection.find_one({"user_id": user_id})
    
    if entry:
        entry["id"] = str(entry.pop("_id"))
        return entry
    return None
