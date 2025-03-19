from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "celestial_wordforge")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Données pour le mode Vocabulaire - Mots-croisés
crossword_data = [
    {
        "word": "ephemeral",
        "definition": "Lasting for a very short time",
        "difficulty": 2
    },
    {
        "word": "ubiquitous",
        "definition": "Present, appearing, or found everywhere",
        "difficulty": 3
    },
    {
        "word": "serendipity",
        "definition": "The occurrence of events by chance in a beneficial way",
        "difficulty": 2
    },
    {
        "word": "eloquent",
        "definition": "Fluent or persuasive in speaking or writing",
        "difficulty": 1
    },
    {
        "word": "paradox",
        "definition": "A statement that contradicts itself but might be true",
        "difficulty": 1
    }
]

# Données pour le mode Vocabulaire - Texte à trous
gap_fill_data = [
    {
        "text": "The {1} of social media on society is both {2} and {3}.",
        "words": ["impact", "profound", "complex"],
        "definitions": [
            "The effect or influence of one thing on another",
            "Very great or intense",
            "Consisting of many different and connected parts"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} between the two countries was finally {2} after years of {3}.",
        "words": ["agreement", "signed", "negotiations"],
        "definitions": [
            "An arrangement or promise to do something, made by two or more people or groups",
            "To write your name on a document to show that you agree with its contents",
            "Official discussions between groups who are trying to reach an agreement"
        ],
        "difficulty": 2
    },
    {
        "text": "Scientists are {1} new ways to {2} renewable energy in order to {3} climate change.",
        "words": ["exploring", "harness", "combat"],
        "definitions": [
            "To investigate or examine a subject or place in order to learn about it",
            "To control and use the force or strength of something to produce power or energy",
            "To try to stop something harmful from happening or getting worse"
        ],
        "difficulty": 2
    }
]

# Données pour le mode Vocabulaire - Relier synonymes
synonym_data = [
    {
        "word": "begin",
        "synonym": "commence",
        "difficulty": 1
    },
    {
        "word": "strange",
        "synonym": "peculiar",
        "difficulty": 1
    },
    {
        "word": "happy",
        "synonym": "delighted",
        "difficulty": 1
    },
    {
        "word": "essential",
        "synonym": "vital",
        "difficulty": 2
    },
    {
        "word": "conceal",
        "synonym": "hide",
        "difficulty": 2
    }
]

# Données pour le mode Grammaire - Trouver l'intrus
odd_one_out_data = [
    {
        "words": ["running", "swimming", "jumping", "happy", "walking"],
        "correct_index": 3,
        "explanation": "'Happy' is an adjective while all the others are gerunds/present participles of verbs describing activities",
        "difficulty": 1
    },
    {
        "words": ["beautiful", "handsome", "pretty", "table", "gorgeous"],
        "correct_index": 3,
        "explanation": "'Table' is a noun while all the others are adjectives describing appearance",
        "difficulty": 1
    },
    {
        "words": ["slowly", "quickly", "carefully", "nice", "quietly"],
        "correct_index": 3,
        "explanation": "'Nice' is an adjective while all the others are adverbs ending in -ly",
        "difficulty": 1
    }
]

# Données pour le mode Grammaire - Conjugaison de verbes
verb_conjugation_data = [
    {
        "sentence": "She {verb} to the store every day.",
        "verb": "go",
        "tense": "present simple",
        "correct_form": "goes",
        "difficulty": 1
    },
    {
        "sentence": "They {verb} the project when the power went out.",
        "verb": "complete",
        "tense": "past continuous",
        "correct_form": "were completing",
        "difficulty": 2
    },
    {
        "sentence": "By next month, I {verb} here for five years.",
        "verb": "work",
        "tense": "future perfect",
        "correct_form": "will have worked",
        "difficulty": 3
    }
]

# Données pour le mode Grammaire - Phrasal verbs
phrasal_verb_data = [
    {
        "verb": "look",
        "particle": "up",
        "meaning": "Search for information in a reference book or database",
        "example": "If you don't know the meaning of a word, look it up in a dictionary.",
        "difficulty": 1
    },
    {
        "verb": "give",
        "particle": "up",
        "meaning": "Stop trying to do something",
        "example": "Don't give up on your dreams, keep working hard.",
        "difficulty": 1
    },
    {
        "verb": "put",
        "particle": "off",
        "meaning": "Postpone or delay something",
        "example": "We'll have to put off the meeting until next week.",
        "difficulty": 1
    },
    {
        "verb": "break",
        "particle": "down",
        "meaning": "Stop working or functioning",
        "example": "My car broke down on the way to work this morning.",
        "difficulty": 1
    }
]

# Données pour le mode Culture - Variantes régionales
regional_variant_data = [
    {
        "uk_word": "lift",
        "us_word": "elevator",
        "meaning": "A moving platform or cage for carrying people or goods between the floors of a building",
        "difficulty": 1
    },
    {
        "uk_word": "flat",
        "us_word": "apartment",
        "meaning": "A self-contained housing unit in a building",
        "difficulty": 1
    },
    {
        "uk_word": "biscuit",
        "us_word": "cookie",
        "meaning": "A small baked unleavened cake, typically crisp, flat, and sweet",
        "difficulty": 1
    },
    {
        "uk_word": "autumn",
        "us_word": "fall",
        "meaning": "The third season of the year, when crops and fruits are gathered and leaves fall",
        "difficulty": 1
    },
    {
        "uk_word": "petrol",
        "us_word": "gas",
        "meaning": "A fuel for internal combustion engines",
        "difficulty": 1
    }
]

# Données pour le mode Culture - Plats et nationalités
food_origin_data = [
    {
        "dish_name": "Fish and Chips",
        "origin_country": "United Kingdom",
        "description": "Deep-fried fish in batter served with thick potato chips",
        "difficulty": 1
    },
    {
        "dish_name": "Apple Pie",
        "origin_country": "United States",
        "description": "Pastry filled with sliced apples and cinnamon, often served with ice cream",
        "difficulty": 1
    },
    {
        "dish_name": "Poutine",
        "origin_country": "Canada",
        "description": "A dish of french fries topped with cheese curds and gravy",
        "difficulty": 1
    },
    {
        "dish_name": "Meat Pie",
        "origin_country": "Australia",
        "description": "A hand-sized meat pie containing ground beef and gravy",
        "difficulty": 2
    },
    {
        "dish_name": "Jerk Chicken",
        "origin_country": "Jamaica",
        "description": "Spicy grilled chicken marinated with a hot spice mixture called Jamaican jerk spice",
        "difficulty": 1
    },
    {
        "dish_name": "Irish Stew",
        "origin_country": "Ireland",
        "description": "A traditional stew made with lamb or mutton, potatoes, carrots and onions",
        "difficulty": 2
    },
    {
        "dish_name": "Pavlova",
        "origin_country": "New Zealand",
        "description": "A meringue-based dessert with a crisp crust and soft inside, topped with fruit and whipped cream",
        "difficulty": 2
    }
]

# Données pour le mode Culture - Expressions idiomatiques
idiom_data = [
    {
        "expressions": [
            "It's raining cats and dogs",
            "Break a leg",
            "The early bird catches the worm",
            "To dance with the cloudy elephants",
            "Bite off more than you can chew"
        ],
        "fake_index": 3,
        "explanation": "'To dance with the cloudy elephants' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To cost an arm and a leg",
            "To be on cloud nine",
            "To see the golden mountains",
            "To hit the nail on the head",
            "A piece of cake"
        ],
        "fake_index": 2,
        "explanation": "'To see the golden mountains' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To kick the bucket",
            "Once in a blue moon",
            "To speak with silver bells",
            "To let the cat out of the bag",
            "To pull someone's leg"
        ],
        "fake_index": 2,
        "explanation": "'To speak with silver bells' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    }
]

def init_game_data():
    if "crossword_items" not in db.list_collection_names():
        db.create_collection("crossword_items")
    if "gap_fill_items" not in db.list_collection_names():
        db.create_collection("gap_fill_items")
    if "synonym_match_items" not in db.list_collection_names():
        db.create_collection("synonym_match_items")
    if "odd_one_out_items" not in db.list_collection_names():
        db.create_collection("odd_one_out_items")
    if "verb_conjugation_items" not in db.list_collection_names():
        db.create_collection("verb_conjugation_items")
    if "phrasal_verb_items" not in db.list_collection_names():
        db.create_collection("phrasal_verb_items")
    if "regional_variant_items" not in db.list_collection_names():
        db.create_collection("regional_variant_items")
    if "food_origin_items" not in db.list_collection_names():
        db.create_collection("food_origin_items")
    if "idiom_items" not in db.list_collection_names():
        db.create_collection("idiom_items")

    if db.crossword_items.count_documents({}) == 0:
        db.crossword_items.insert_many(crossword_data)
        print("Données de mots-croisés insérées")
    
    if db.gap_fill_items.count_documents({}) == 0:
        db.gap_fill_items.insert_many(gap_fill_data)
        print("Données de texte à trous insérées")
    
    if db.synonym_match_items.count_documents({}) == 0:
        db.synonym_match_items.insert_many(synonym_data)
        print("Données de synonymes insérées")
    
    if db.odd_one_out_items.count_documents({}) == 0:
        db.odd_one_out_items.insert_many(odd_one_out_data)
        print("Données d'intrus insérées")
    
    if db.verb_conjugation_items.count_documents({}) == 0:
        db.verb_conjugation_items.insert_many(verb_conjugation_data)
        print("Données de conjugaison de verbes insérées")
    
    if db.phrasal_verb_items.count_documents({}) == 0:
        db.phrasal_verb_items.insert_many(phrasal_verb_data)
        print("Données de phrasal verbs insérées")
    
    if db.regional_variant_items.count_documents({}) == 0:
        db.regional_variant_items.insert_many(regional_variant_data)
        print("Données de variantes régionales insérées")
    
    if db.food_origin_items.count_documents({}) == 0:
        db.food_origin_items.insert_many(food_origin_data)
        print("Données de plats et nationalités insérées")
    
    if db.idiom_items.count_documents({}) == 0:
        db.idiom_items.insert_many(idiom_data)
        print("Données d'expressions idiomatiques insérées")

    print("Initialisation des données de jeu terminée")

if __name__ == "__main__":
    init_game_data()