
from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from crud import pwd_context
from fastapi import APIRouter, Depends, HTTPException
from database.database import get_db
from sqlalchemy.orm import Session
from starlette import status
from schema import UserCreate, Token
from crud import create_user, get_existing_user, get_user
from starlette.config import Config

config = Config('env/.env')

ACCESS_TOKEN_EXPIRE_MINUTES = int(config('ACCESS_TOKEN_EXPIRE_MINUTES'))
SECRET_KEY = config('SECRET_KEY')
ALGORITHM = "HS256"

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/api/user/login")

router = APIRouter(
    prefix="/api/user"
)

def get_current_user(token: str = Depends(oauth2_schema),
                     db: Session = Depends(get_db)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credential",
        headers={"WWW-Authenticate" : "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credential_exception
    except JWTError:
        raise credential_exception
    else:
        user = get_user(db=db, username=username)
        if user is None:
            raise credential_exception
        return user


    

@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create:UserCreate, db:Session = Depends(get_db)):
    user = get_existing_user(db=db, user_create=_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="이미 존재하는 사용자입니다.")
    create_user(db=db, user_create=_user_create)


@router.post('/login', response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
               db: Session = Depends(get_db)):
    print(form_data)
    user = get_user(db=db, username=form_data.username)
    if not user or pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect Username or Password",
            headers= {"WWW-Authenticate" : "Bearer"}
        )
    
    # make access token
    data = {
        "sub" : user.username,
        "exp" : datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, key=SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token" : access_token,
        "token_type" : "bearer",
        "username" : user.username
    }