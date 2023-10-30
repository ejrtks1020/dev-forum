from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import Question, User
import schema
import crud
from typing import List
from starlette import status
from router.user_router import get_current_user

router = APIRouter(
    prefix="/api/question",
    tags=['question']
)

@router.get("/list", response_model=schema.question_schema.QuestionList)
def question_list(db: Session=Depends(get_db), page: int = 0, size: int = 10, keyword: str = ''):
    total, _question_list = crud.question_crud.get_question_list(db, skip=page*size, limit=size, keyword=keyword)
    return {
        'total': total,
        'question_list': _question_list
        }

@router.get("/detail/{question_id}", response_model=schema.question_schema.Question)
def question_detail(question_id: int, page: int = 0, size: int = 10, db: Session=Depends(get_db)):
    question = crud.question_crud.get_question(db=db, question_id=question_id)
    response = schema.question_schema.Question.from_orm(question)
    return response

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: schema.question_schema.QuestionCreate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    crud.question_crud.create_question(db=db, question_create=_question_create, user=current_user)

@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def question_update(_question_update: schema.question_schema.QuestionUpdate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_question = crud.question_crud.get_question(db=db, question_id=_question_update.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을 수 없습니다.")
    if current_user.id != db_question.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 권한이 없습니다.")
    
    crud.question_crud.update_question(db=db, db_question=db_question, question_update=_question_update)

@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def question_delete(_question_delete: schema.question_schema.QuestionDelete,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_question = crud.question_crud.get_question(db=db, question_id=_question_delete.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을 수 없습니다.")
    if current_user.id != db_question.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="삭제 권한이 없습니다.")
    
    crud.question_crud.delete_question(db=db, db_question=db_question)

@router.post("/vote", status_code=status.HTTP_204_NO_CONTENT)
def question_vote(_question_vote: schema.question_schema.QuestionVote,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    db_question = crud.question_crud.get_question(db=db, question_id=_question_vote.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="데이터를 찾을 수 없습니다.")
    crud.question_crud.vote_question(db=db, db_question=db_question, db_user=current_user)
    