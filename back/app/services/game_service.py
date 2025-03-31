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
    if "crossword_cache" not in session:
        session["crossword_cache"] = []

    # Check if we have cached words
    if session["crossword_cache"]:
        # Use a word from our cache of crossword-optimized words
        item = session["crossword_cache"].pop(0)

        # Update session
        session["used_questions"]["crossword_items"].append(str(item["_id"]))
        session["last_crossword_word"] = item.get("word", "").lower()
        session["last_accessed"] = datetime.utcnow()

        # Save session with updated cache
        db.session_questions.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "used_questions": session["used_questions"],
                    "last_crossword_word": session["last_crossword_word"],
                    "last_accessed": session["last_accessed"],
                    "crossword_cache": session["crossword_cache"]
                }
            }
        )

        item["_id"] = str(item["_id"])
        return item

    # Build base query
    query = {
        "_id": {"$nin": [ObjectId(id_str) for id_str in session["used_questions"]["crossword_items"]]}
    }
    if difficulty is not None:
        query["difficulty"] = difficulty

    # Get all available words
    all_items = list(collection.find(query))

    # If no unused words available, reset the used questions
    if not all_items:
        session["used_questions"]["crossword_items"] = []
        query.pop("_id", None)
        all_items = list(collection.find(query))
        if not all_items:
            return None

    # Create a cache of words optimized for crossword creation
    cached_words = []
    word_length_categories = {}

    # First, categorize words by length for better crossword construction
    for item in all_items:
        word = item.get("word", "").strip().upper()
        if not word:
            continue

        # Filter out words with unusual characters
        if not all(c.isalpha() for c in word):
            continue

        length = len(word)

        # Group by length
        if length not in word_length_categories:
            word_length_categories[length] = []
        word_length_categories[length].append(item)

    # Prioritize words that have common letters (good for intersections)
    common_letters = 'EARIOTNSCLUD'  # Common letters in English

    # First, select words with medium length (4-8 letters) containing common letters
    for length in sorted(word_length_categories.keys()):
        if 4 <= length <= 8:  # Medium length words are ideal for crosswords
            words_in_category = word_length_categories[length]

            # Sort by number of common letters
            words_in_category.sort(key=lambda x: sum(
                1 for c in x["word"].upper() if c in common_letters), reverse=True)

            # Add top 50% of these words to our cache
            top_count = max(1, len(words_in_category) // 2)
            cached_words.extend(words_in_category[:top_count])

    # If we need more words, add shorter and longer words
    if len(cached_words) < 20:
        for length in sorted(word_length_categories.keys()):
            if length < 4 or length > 8:
                words_in_category = word_length_categories[length]
                # Sort by number of common letters
                words_in_category.sort(key=lambda x: sum(
                    1 for c in x["word"].upper() if c in common_letters), reverse=True)
                # Add top 30% of these words
                top_count = max(1, len(words_in_category) // 3)
                cached_words.extend(words_in_category[:top_count])

    # If we still don't have enough words, add some random ones
    remaining_count = 20 - len(cached_words)
    if remaining_count > 0:
        remaining_items = [
            item for item in all_items if item not in cached_words]
        if remaining_items:
            cached_words.extend(random.sample(
                remaining_items, min(remaining_count, len(remaining_items))))

    # Shuffle our cache for randomness
    random.shuffle(cached_words)

    # Update our cache in the session
    session["crossword_cache"] = cached_words[1:]  # All except the first

    # Select the first item for immediate use
    if not cached_words:
        # Fallback to random selection if we couldn't create a cache
        item = random.choice(all_items)
    else:
        item = cached_words[0]

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
                "last_accessed": session["last_accessed"],
                "crossword_cache": session["crossword_cache"]
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
        selected_items = random.sample(
            available_items, min(count, len(available_items)))

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
