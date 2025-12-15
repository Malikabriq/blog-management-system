import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

USER_DIR = os.path.join(BASE_DIR, "data", "users")
BLOG_DIR = os.path.join(BASE_DIR, "data", "blogs")

os.makedirs(USER_DIR, exist_ok=True)
os.makedirs(BLOG_DIR, exist_ok=True)

JWT_SECRET = "super-secret-key"
JWT_ALGO = "HS256"
