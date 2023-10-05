import datetime
from pydantic import BaseModel, validator
from typing import Union
from schema.user_schema import User
from typing import List
class AnswerCreate(BaseModel):
    content: str
        
    @validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v
    
class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime
    user: Union[User, None]
    question_id: int
    modify_date: Union[datetime.datetime, None] = None
    voter: List[User] = None


    class Config:
        orm_mode = True

class AnswerUpdate(AnswerCreate):
    answer_id: int

class AnswerDelete(BaseModel):
    answer_id: int

class AnswerVote(BaseModel):
    answer_id: int