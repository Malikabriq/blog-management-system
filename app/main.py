from fastapi import FastAPI
from routers.auth_router import router as auth_router
from routers.user_router import router as user_router
from routers.blog_router import router as blog_router
from services.user_service import ensure_default_admin

app = FastAPI(title="Personal Blog Backend")

ensure_default_admin()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(blog_router)
