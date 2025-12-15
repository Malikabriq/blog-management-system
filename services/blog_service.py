import os
import uuid
from datetime import datetime
from typing import List
from core.config import BLOG_DIR
from utils.file_ops import read_json, write_json, delete_file
from models.blog import Blog


def blog_path(bid: str):
    return os.path.join(BLOG_DIR, f"{bid}.json")


def list_blogs() -> List[Blog]:
    blogs = []
    for file in os.listdir(BLOG_DIR):
        data = read_json(os.path.join(BLOG_DIR, file))
        blogs.append(Blog(**data))

    blogs.sort(key=lambda b: b.date, reverse=True)
    return blogs


def get_blog(bid: str):
    data = read_json(blog_path(bid))
    return Blog(**data) if data else None


def create_blog(owner_id: str, title: str, content: str) -> Blog:
    bid = str(uuid.uuid4())
    date = datetime.now().isoformat()
    blog = Blog(
        id=bid,
        owner_id=owner_id,
        title=title,
        content=content,
        date=date
    )
    write_json(blog_path(bid), blog.dict())
    return blog


def update_blog(bid: str, title: str, content: str):
    blog = get_blog(bid)
    if not blog:
        return None

    blog.title = title
    blog.content = content
    write_json(blog_path(bid), blog.dict())
    return blog


def delete_blog(bid: str):
    delete_file(blog_path(bid))
