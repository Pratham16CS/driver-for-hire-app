from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app import models,schemas,crud,auth
from app.database import get_db

router = APIRouter()

# User Registration
@router.post("/register",response_model=schemas.UserOut)
def register_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
    db_user = crud.get_user_by_email(db,email=user.email)
    if db_user:
        raise HTTPException(status_code=400,detail="Email already registered")
    hashed_password = auth.hash_password(user.password_hash)
    user_with_hashed_pw = user.copy(update={"password_hash": hashed_password})
    return crud.create_user(db=db,user=user_with_hashed_pw)

# User Login
@router.post("/login",response_model=schemas.Token)
def login_user(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user = crud.get_user_by_email(db,email=form_data.username)
    if not user:
        raise HTTPException(status_code=401,detail="Invalid Credentials")
    if not auth.verify_password(form_data.password,user.password_hash):
        raise HTTPException(status_code=401,detail="Invalid Password")
    
    access_token = auth.create_access_token(data={"sub":str(user.user_id)})
    return {"access_token":access_token,"token_type":"bearer"}

# Get Current User Info
@router.get("/me",response_model=schemas.UserOut)
def get_current_user_info(current_user:models.User=Depends(auth.get_current_user)):
    return current_user

