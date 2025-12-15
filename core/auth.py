from fastapi import HTTPException, Depends, Header
from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import datetime, timedelta
from core.config import JWT_SECRET, JWT_ALGO
from services.user_service import get_user_by_username

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def create_token(data: dict):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(hours=10)
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGO)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        username = payload.get("sub")
        user = get_user_by_username(username)
        if not user:
            raise HTTPException(401, "User not found")
        return user
    except:
        raise HTTPException(401, "Invalid token")

def admin_required(current=Depends(get_current_user)):
    if current.role != "admin":
        raise HTTPException(403, "Admin access required")
    return current
