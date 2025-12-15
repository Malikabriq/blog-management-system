from fastapi import APIRouter, Depends, HTTPException
from core.auth import get_current_user
from services.user_service import list_users, delete_user, update_user, get_user_by_id

router = APIRouter(prefix="/users", tags=["Users"])

def admin_required(user):
    if user.role != "admin":
        raise HTTPException(403, "Admin only")


@router.get("/")
def get_all_users(current = Depends(get_current_user)):
    admin_required(current)
    return list_users()


@router.put("/{uid}")
def update(uid: str, username: str, role: str, current = Depends(get_current_user)):
    admin_required(current)
    return update_user(uid, username, role)


@router.delete("/{uid}")
def remove(uid: str, current = Depends(get_current_user)):
    admin_required(current)
    delete_user(uid)
    return {"message": "User deleted"}
