from typing import Dict, List, Set
from datetime import datetime
from pydantic import BaseModel, Field

class SessionQuestions(BaseModel):
    user_id: str
    used_questions: Dict[str, List[str]] = Field(default_factory=dict)
    last_accessed: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
