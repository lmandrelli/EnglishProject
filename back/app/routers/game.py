from fastapi import APIRouter, Depends, Query
from typing import List, Optional

from ..services import game_service
from ..utils.auth import get_current_active_user
from ..models.user import User

router = APIRouter(
    prefix="/api/game",
    tags=["game"],
    responses={404: {"description": "Not found"}},
)

@router.get("/vocabulary/crossword")
async def get_vocabulary_crossword(
    difficulty: Optional[int] = Query(None, description="Niveau de difficulté (1-3)"),
    current_user: User = Depends(get_current_active_user)
):
    return game_service.get_vocab_crossword(difficulty, current_user.id)

@router.get("/vocabulary/gap-fill")
async def get_vocabulary_gap_fill(
    difficulty: Optional[int] = Query(None, description="Niveau de difficulté (1-3)"),
    current_user: User = Depends(get_current_active_user)
):
    return game_service.get_vocab_gap_fill(difficulty, current_user.id)

@router.get("/vocabulary/synonyms")
async def get_vocabulary_synonyms(
    difficulty: Optional[int] = Query(None, description="Niveau de difficulté (1-3)"),
    count: int = Query(5, description="Nombre de paires de synonymes à récupérer"),
    current_user: User = Depends(get_current_active_user)
):
    return game_service.get_vocab_synonym_match(difficulty, count, current_user.id)

@router.get("/grammar/odd-one-out")
async def get_grammar_odd_one_out(
    difficulty: Optional[int] = Query(None, description="Niveau de difficulté (1-3)"),
    current_user: User = Depends(get_current_active_user)
):
    return game_service.get_grammar_odd_one_out(difficulty, current_user.id)

@router.get("/grammar/verb-conjugation")
async def get_grammar_verb_conjugation(
    difficulty: Optional[int] = Query(None, description="Niveau de difficulté (1-3)"),
    current_user: User = Depends(get_current_active_user)
):
    return game_service.get_grammar_verb_conjugation(difficulty, current_user.id)

@router.get("/grammar/phrasal-verbs")
async def get_grammar_phrasal_verbs(
    difficulty: Optional[int] = Query(None, description="Niveau de difficulté (1-3)"),
    count: int = Query(5, description="Nombre de phrasal verbs à récupérer"),
    current_user: User = Depends(get_current_active_user)
):
    return game_service.get_grammar_phrasal_verbs(difficulty, count, current_user.id)

@router.get("/culture/regional-variants")
async def get_culture_regional_variants(
    difficulty: Optional[int] = Query(None, description="Niveau de difficulté (1-3)"),
    count: int = Query(5, description="Nombre de variantes régionales à récupérer"),
    current_user: User = Depends(get_current_active_user)
):
    return game_service.get_culture_regional_variants(difficulty, count, current_user.id)

@router.get("/culture/food-origins")
async def get_culture_food_origins(
    difficulty: Optional[int] = Query(None, description="Niveau de difficulté (1-3)"),
    count: int = Query(5, description="Nombre de plats et origines à récupérer"),
    current_user: User = Depends(get_current_active_user)
):
    return game_service.get_culture_food_origins(difficulty, count, current_user.id)

@router.get("/culture/idioms")
async def get_culture_idioms(
    difficulty: Optional[int] = Query(None, description="Niveau de difficulté (1-3)"),
    current_user: User = Depends(get_current_active_user)
):
    return game_service.get_culture_idioms(difficulty, current_user.id)
