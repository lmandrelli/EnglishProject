from fastapi import APIRouter, Depends, HTTPException
from ..services import leaderboard_service
from ..utils.auth import get_current_active_user
from ..models.user import User
from typing import List

router = APIRouter(
    prefix="/api/leaderboard",
    tags=["leaderboard"],
    responses={404: {"description": "Not found"}},
)

from pydantic import BaseModel

class ScoreSubmission(BaseModel):
    score: int

@router.post("/submit")
async def submit_score(
    submission: ScoreSubmission,
    current_user: User = Depends(get_current_active_user)
):
    success = leaderboard_service.submit_score(
        user_id=current_user.id,
        username=current_user.username,
        score=submission.score
    )
    return {"success": success}

@router.get("/top")
async def get_top_scores(
    current_user: User = Depends(get_current_active_user)
):
    scores = leaderboard_service.get_top_scores()
    return {"scores": scores}

@router.get("/user")
async def get_user_score(
    current_user: User = Depends(get_current_active_user)
):
    score = leaderboard_service.get_user_score(current_user.id)
    if not score:
        raise HTTPException(status_code=404, detail="Score not found")
    return score
