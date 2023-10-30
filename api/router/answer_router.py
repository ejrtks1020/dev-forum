from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from starlette.responses import RedirectResponse
from schema import *
from crud import answer_crud, question_crud, get_answer, update_answer, delete_answer, vote_answer, get_answer_list
from sqlalchemy.orm import Session
from database.database import get_db
from router.user_router import get_current_user
from database.models import User

router = APIRouter(
    prefix="/api/answer",
    tags=['answer']
)

@router.get("/list/{question_id}", response_model=AnswerList)
def question_list(question_id: int, page: int = 0, size: int = 10, db: Session=Depends(get_db)):
    total, _answer_list = get_answer_list(db, question_id=question_id, skip=page*size, limit=size)
    response = AnswerList(answer_list=_answer_list, total=total)
    return response

@router.post("/create/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def answer_create(question_id: int,
                  _answer_create: AnswerCreate,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    # db에서 question id에 해당하는 데이터 조회
    question = question_crud.get_question(db, question_id=question_id)

    # 없으면 오류 출력	
    if not question:
        raise HTTPException(status_code=404, detail='Question not found')
    answer_crud.create_answer(db, question=question, answer_create=_answer_create, user=current_user)

    from router.question_router import router as question_router

    url = question_router.url_path_for('question_detail', question_id=question_id)
    return RedirectResponse(url, status_code=status.HTTP_303_SEE_OTHER)

@router.get("/detail/{answer_id}", response_model=Answer)
def answer_detail(answer_id, db: Session = Depends(get_db)):
    answer = answer_crud.get_answer(db=db, answer_id=answer_id)
    return answer

@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def answer_update(_answer_update: AnswerUpdate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_answer = get_answer(db=db, answer_id=_answer_update.answer_id)
    if not db_answer:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을 수 없습니다.")
    if current_user.id != db_answer.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 권한이 없습니다.")
    
    update_answer(db=db, db_answer=db_answer, answer_update=_answer_update)

@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def answer_delete(_answer_delete: AnswerDelete,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_answer = get_answer(db=db, answer_id=_answer_delete.answer_id)
    if not db_answer:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을 수 없습니다.")
    if current_user.id != db_answer.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="삭제 권한이 없습니다.")
    
    delete_answer(db=db, db_answer=db_answer)

@router.post("/vote", status_code=status.HTTP_204_NO_CONTENT)
def answer_vote(_answer_vote: AnswerVote,
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    db_answer = get_answer(db=db, answer_id=_answer_vote.answer_id)
    if not db_answer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="데이터를 찾을 수 없습니다.")
    vote_answer(db=db, db_answer=db_answer, db_user=current_user)
    