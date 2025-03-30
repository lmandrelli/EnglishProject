from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LeaderboardEntry(BaseModel):
    user_id: str
    username: str
    score: int
    created_at: datetime

class LeaderboardEntryInDB(LeaderboardEntry):
    id: str

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
