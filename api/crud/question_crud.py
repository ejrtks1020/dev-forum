from datetime import datetime
from database.models import Question, Answer
from sqlalchemy.orm import Session
from schema import QuestionCreate, QuestionUpdate, QuestionDelete
from database.models import User

def get_question_list(db: Session, skip: int = 0, limit: int = 10, keyword: str = ''):

    question_list = db.query(Question)
    if keyword:
        search = '%%{}%%'.format(keyword)
        sub_query = db.query(Answer.question_id, Answer.content, User.username) \
                    .outerjoin(User, Answer.user_id == User.id).subquery()
        question_list = question_list \
                        .outerjoin(User) \
                        .outerjoin(sub_query, sub_query.c.question_id == Question.id) \
                        .filter(Question.subject.ilike(search) |
                                Question.content.ilike(search) |
                                User.username.ilike(search) | 
                                sub_query.c.content.ilike(search) |
                                sub_query.c.username.ilike(search))
    total = question_list.distinct().count()
    question_list = question_list.order_by(Question.create_date.desc()) \
                    .offset(skip).limit(limit).all()

    # _question_list = db.query(Question)\
    #     .order_by(Question.create_date.desc())
    
    # total = _question_list.count()
    # question_list = _question_list.offset(skip).limit(limit).all()
    return total, question_list

def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question

def create_question(db: Session, question_create: QuestionCreate, user: User):
    db_question = Question(subject=question_create.subject,
                           content=question_create.content,
                           create_date=datetime.now(),
                           user=user)
    db.add(db_question)
    db.commit()

def update_question(db: Session, db_question: Question, question_update: QuestionUpdate):
    db_question.subject = question_update.subject
    db_question.content = question_update.content
    db_question.modify_date = datetime.now()
    db.add(db_question)
    db.commit()

def delete_question(db: Session, db_question: Question):
    db.delete(db_question)
    db.commit()

def vote_question(db: Session, db_question: Question, db_user: User):
    db_question.voter.append(db_user)
    db.commit()