from pydantic import BaseModel
from typing import List, Optional

# Modèles pour le mode Vocabulaire
class CrosswordItem(BaseModel):
    word: str
    definition: str
    difficulty: int = 1

class GapFillItem(BaseModel):
    text: str # Texte avec des marqueurs {1}, {2}, {3} pour les trous
    words: List[str]
    definitions: List[str]
    difficulty: int = 1

class SynonymMatchItem(BaseModel):
    word: str
    synonym: str
    difficulty: int = 1

# Modèles pour le mode Grammaire
class OddOneOutItem(BaseModel):
    words: List[str]
    correct_index: int # Indice de l'intrus dans la liste
    explanation: str # Explication de pourquoi c'est l'intrus
    difficulty: int = 1

class VerbConjugationItem(BaseModel):
    sentence: str # Phrase avec un marqueur {verb} où le verbe conjugué doit être placé
    verb: str # Verbe à l'infinitif
    tense: str
    correct_form: str
    difficulty: int = 1

class PhrasalVerbItem(BaseModel):
    verb: str
    particle: str
    meaning: str
    example: str
    difficulty: int = 1

#Modèles pour le mode Culture
class RegionalVariantItem(BaseModel):
    uk_word: str
    us_word: str
    meaning: str
    difficulty: int = 1

class FoodOriginItem(BaseModel):
    dish_name: str
    origin_country: str
    description: str
    difficulty: int = 1

class IdiomItem(BaseModel):
    expressions: List[str]
    fake_index: int
    explanation: str
    difficulty: int = 1