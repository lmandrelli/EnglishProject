from ..database.mongodb import db
from bson import ObjectId
from datetime import datetime, timedelta
from typing import Optional, List
import random

def get_session_questions(user_id: str) -> dict:
    session = db.session_questions.find_one({"user_id": user_id})
    if not session:
        session = {
            "user_id": user_id,
            "used_questions": {},
            "last_accessed": datetime.utcnow()
        }
        db.session_questions.insert_one(session)
    elif (datetime.utcnow() - session["last_accessed"]) > timedelta(hours=24):
        # Reset session if it's older than 24 hours
        session["used_questions"] = {}
        session["last_accessed"] = datetime.utcnow()
        db.session_questions.update_one(
            {"user_id": user_id},
            {"$set": session}
        )
    return session

def get_random_item(collection_name: str, user_id: str, difficulty: Optional[int] = None):
    collection = db[collection_name]
    session = get_session_questions(user_id)
    
    # Initialize used questions list for this collection if it doesn't exist
    if collection_name not in session["used_questions"]:
        session["used_questions"][collection_name] = []
    
    # Build query
    query = {
        "_id": {"$nin": [ObjectId(id_str) for id_str in session["used_questions"][collection_name]]}
    }
    if difficulty is not None:
        query["difficulty"] = difficulty
    
    # Get available questions
    available_items = list(collection.find(query))
    
    # If no unused questions available, reset the used questions for this collection
    if not available_items:
        session["used_questions"][collection_name] = []
        query.pop("_id")
        available_items = list(collection.find(query))
        if not available_items:
            return None
    
    # Select random item from available ones
    item = random.choice(available_items)
    
    # Update used questions
    session["used_questions"][collection_name].append(str(item["_id"]))
    session["last_accessed"] = datetime.utcnow()
    
    # Save session
    db.session_questions.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "used_questions": session["used_questions"],
                "last_accessed": session["last_accessed"]
            }
        }
    )
    
    return item

def get_vocab_crossword(difficulty=None, user_id=None):
    collection = db["crossword_items"]
    session = get_session_questions(user_id)
    
    # Initialize used questions and last word for crossword
    if "crossword_items" not in session["used_questions"]:
        session["used_questions"]["crossword_items"] = []
    if "last_crossword_word" not in session:
        session["last_crossword_word"] = None
    
    # Build base query
    query = {
        "_id": {"$nin": [ObjectId(id_str) for id_str in session["used_questions"]["crossword_items"]]}
    }
    if difficulty is not None:
        query["difficulty"] = difficulty
    
    last_word = session.get("last_crossword_word")
    available_items = []
    
    if last_word:
        # Find words that share at least one non-first letter with the last word
        last_word_letters = set(last_word[1:])  # Exclude first letter
        all_items = list(collection.find(query))
        
        for item in all_items:
            current_word = item.get("word", "").lower()
            if current_word:
                # Skip if first letters match
                if current_word[0].lower() == last_word[0].lower():
                    continue
                # Check if any non-first letter matches
                word_letters = set(current_word[1:])  # Exclude first letter
                if last_word_letters & word_letters:  # Check for intersection
                    available_items.append(item)
    
    # If no matching words found or no last word, get any unused word
    if not available_items:
        session["used_questions"]["crossword_items"] = []  # Reset used questions
        query.pop("_id", None)  # Remove the used questions filter
        available_items = list(collection.find(query))
    
    if not available_items:
        return None
    
    # Select random item from available ones
    item = random.choice(available_items)
    
    # Update session
    session["used_questions"]["crossword_items"].append(str(item["_id"]))
    session["last_crossword_word"] = item.get("word", "").lower()
    session["last_accessed"] = datetime.utcnow()
    
    # Save session
    db.session_questions.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "used_questions": session["used_questions"],
                "last_crossword_word": session["last_crossword_word"],
                "last_accessed": session["last_accessed"]
            }
        }
    )
    
    item["_id"] = str(item["_id"])
    return item

def get_vocab_gap_fill(difficulty=None, user_id=None):
    item = get_random_item("gap_fill_items", user_id, difficulty)
    if item:
        item["_id"] = str(item["_id"])
    return item

def get_batch_items(collection_name: str, user_id: str, count: int = 5, difficulty: Optional[int] = None):
    collection = db[collection_name]
    session = get_session_questions(user_id)
    
    # Initialize used questions list for this collection if it doesn't exist
    if collection_name not in session["used_questions"]:
        session["used_questions"][collection_name] = []
    
    # Build query for unused items
    query = {
        "_id": {"$nin": [ObjectId(id_str) for id_str in session["used_questions"][collection_name]]}
    }
    if difficulty is not None:
        query["difficulty"] = difficulty
    
    # Get available questions
    available_items = list(collection.find(query))
    
    # If we don't have enough unused questions, reset the used questions
    if len(available_items) < count:
        session["used_questions"][collection_name] = []
        query.pop("_id")
        available_items = list(collection.find(query))
    
    # Get random items
    selected_items = []
    if available_items:
        # Take up to count random items
        selected_items = random.sample(available_items, min(count, len(available_items)))
        
        # Update used questions
        for item in selected_items:
            item_id = str(item["_id"])
            if item_id not in session["used_questions"][collection_name]:
                session["used_questions"][collection_name].append(item_id)
        
        # Update session
        session["last_accessed"] = datetime.utcnow()
        db.session_questions.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "used_questions": session["used_questions"],
                    "last_accessed": session["last_accessed"]
                }
            }
        )
    
    # Convert ObjectId to string
    for item in selected_items:
        item["_id"] = str(item["_id"])
    
    return selected_items

def get_vocab_synonym_match(difficulty=None, count=5, user_id=None):
    return get_batch_items("synonym_match_items", user_id, count, difficulty)

def get_grammar_odd_one_out(difficulty=None, user_id=None):
    item = get_random_item("odd_one_out_items", user_id, difficulty)
    if item:
        item["_id"] = str(item["_id"])
    return item

def get_grammar_verb_conjugation(difficulty=None, user_id=None):
    item = get_random_item("verb_conjugation_items", user_id, difficulty)
    if item:
        item["_id"] = str(item["_id"])
    return item

def get_grammar_phrasal_verbs(difficulty=None, count=5, user_id=None):
    return get_batch_items("phrasal_verb_items", user_id, count, difficulty)

def get_culture_regional_variants(difficulty=None, count=5, user_id=None):
    return get_batch_items("regional_variant_items", user_id, count, difficulty)

def get_culture_food_origins(difficulty=None, count=5, user_id=None):
    return get_batch_items("food_origin_items", user_id, count, difficulty)

def get_culture_idioms(difficulty=None, user_id=None):
    item = get_random_item("idiom_items", user_id, difficulty)
    if item:
        item["_id"] = str(item["_id"])
    return item
