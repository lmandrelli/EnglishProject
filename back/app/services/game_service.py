from ..database.mongodb import db
from bson import ObjectId
import random

def get_random_item(collection_name, difficulty=None):
    collection = db[collection_name]

    query = {}
    if difficulty is not None:
        query["difficulty"] = difficulty
    
    count = collection.count_documents(query)
    if count == 0:
        return None
    
    random_index = random.randint(0, count - 1)
    return collection.find(query).limit(1).skip(random_index).next()

def get_vocab_crossword(difficulty=None):
    item = get_random_item("crossword_items", difficulty)
    if item:
        item["_id"] = str(item["_id"])
    return item

def get_vocab_gap_fill(difficulty=None):
    item = get_random_item("gap_fill_items", difficulty)
    if item:
        item["_id"] = str(item["_id"])
    return item

def get_vocab_synonym_match(difficulty=None, count=5):
    collection = db["synonym_match_items"]

    query = {}
    if difficulty is not None:
        query["difficulty"] = difficulty
    
    items = list(collection.aggregate([
        {"$match": query},
        {"$sample": {"size": count}}
    ]))

    for item in items:
        item["_id"] = str(item["_id"])
    
    return items

def get_grammar_odd_one_out(difficulty=None):
    item = get_random_item("odd_one_out_items", difficulty)
    if item:
        item["_id"] = str(item["_id"])
    return item

def get_grammar_verb_conjugation(difficulty=None):
    item = get_random_item("verb_conjugation_items", difficulty)
    if item:
        item["_id"] = str(item["_id"])
    return item

def get_grammar_phrasal_verbs(difficulty=None, count=5):
    collection = db["phrasal_verb_items"]

    query = {}
    if difficulty is not None:
        query["difficulty"] = difficulty
    
    items = list(collection.aggregate([
        {"$match": query},
        {"$sample": {"size": count}}
    ]))

    for item in items:
        item["_id"] = str(item["_id"])
    
    return items

def get_culture_regional_variants(difficulty=None, count=5):
    collection = db["regional_variant_items"]

    query = {}
    if difficulty is not None:
        query["difficulty"] = difficulty
    
    items = list(collection.aggregate([
        {"$match": query},
        {"$sample": {"size": count}}
    ]))

    for item in items:
        item["_id"] = str(item["_id"])
    
    return items

def get_culture_food_origins(difficulty=None, count=5):
    collection = db["food_origin_items"]

    query = {}
    if difficulty is not None:
        query["difficulty"] = difficulty
    
    items = list(collection.aggregate([
        {"$match": query},
        {"$sample": {"size": count}}
    ]))

    for item in items:
        item["_id"] = str(item["_id"])
    
    return items

def get_culture_idioms(difficulty=None):
    item = get_random_item("idiom_items", difficulty)
    if item:
        item["_id"] = str(item["_id"])
    return item