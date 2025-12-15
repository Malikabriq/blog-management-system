import os
import uuid
from typing import List
from core.config import USER_DIR
from utils.file_ops import read_json, write_json, delete_file
from core.security import hash_password, verify_password
from models.user import User

def user_path(uid: str):
    return os.path.join(USER_DIR, f"{uid}.json")


def list_users() -> List[User]:
    users = []
    for file in os.listdir(USER_DIR):
        path = os.path.join(USER_DIR, file)
        if not os.path.isfile(path):
            continue
        data = read_json(path)
        users.append(User(**data))
    return users


def get_user_by_id(uid: str):
    data = read_json(user_path(uid))
    return User(**data) if data else None


def get_user_by_username(username: str):
    for u in list_users():
        if u.username == username:
            return u
    return None


def create_user(username: str, password: str, role="user") -> User:
    if get_user_by_username(username):
        return None  # already exists

    uid = str(uuid.uuid4())
    user = User(id=uid, username=username, password=hash_password(password), role=role)
    write_json(user_path(uid), user.dict())
    return user


def ensure_default_admin():
    if not get_user_by_username("admin"):
        create_user("admin", "admin222", role="admin")


def update_user(uid: str, username: str, role: str):
    user = get_user_by_id(uid)
    user.username = username
    user.role = role
    write_json(user_path(uid), user.dict())
    return user


def delete_user(uid: str):
    delete_file(user_path(uid))


def authenticate_user(username, password):
    user = get_user_by_username(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
