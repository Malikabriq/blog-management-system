from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from services.user_service import authenticate_user, create_user
from core.auth import create_token

router = APIRouter(prefix="/auth", tags=["Auth"])



class RegisterRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(data.username, data.password)
    if not user:
        raise HTTPException(401, "Invalid credentials")

    token = create_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/register")
def register(data: RegisterRequest):
    user = create_user(data.username, data.password)
    if not user:
        raise HTTPException(400, "User already exists")
    return {"message": "User created successfully", "id": user.id}
