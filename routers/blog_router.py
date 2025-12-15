from fastapi import APIRouter, Depends, HTTPException
from core.auth import admin_required
from services.blog_service import (
    list_blogs, create_blog, update_blog, delete_blog, get_blog
)

router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.get("/")
def all_blogs():
    return list_blogs()

@router.get("/{bid}")
def get_single_blog(bid: str):
    blog = get_blog(bid)
    if not blog:
        raise HTTPException(404, "Blog not found")
    return blog

@router.post("/")
def create(title: str, content: str, current=Depends(admin_required)):
    return create_blog(current.id, title, content)

@router.put("/{bid}")
def edit(bid: str, title: str, content: str, current=Depends(admin_required)):
    blog = get_blog(bid)
    if not blog:
        raise HTTPException(404, "Blog not found")
    return update_blog(bid, title, content)

@router.delete("/{bid}")
def delete(bid: str, current=Depends(admin_required)):
    blog = get_blog(bid)
    if not blog:
        raise HTTPException(404, "Not found")
    delete_blog(bid)
    return {"message": "Blog deleted"}
