import datetime
from pydantic import BaseModel, ConfigDict, validator
from schema.answer_schema import Answer
from schema.user_schema import User

from typing import List, Union

class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: List[Answer] = []
    user: Union[User, None]
    modify_date: Union[datetime.datetime, None] = None
    voter: List[User] = []
    view: Union[int, None] = None

    class Config:
        orm_mode = True
    
    @staticmethod
    def from_orm(question):
        answers = question.answers
        sorted_answers = sorted(answers, key = lambda x : [len(x.voter), x.create_date], reverse=True)
        return Question(
            id=question.id,
            subject=question.subject,
            content=question.content,
            create_date=question.create_date,
            answers=sorted_answers,
            user=question.user,
            modify_date=question.modify_date,
            voter=question.voter,
            view=question.view 
        )

class QuestionCreate(BaseModel):
    subject: str
    content: str

    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v

class QuestionList(BaseModel):
    total: int
    question_list: List[Question] = []

class QuestionUpdate(QuestionCreate):
    question_id: int

class QuestionDelete(BaseModel):
    question_id: int

class QuestionVote(BaseModel):
    question_id: int