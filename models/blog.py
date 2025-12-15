from pydantic import BaseModel

class Blog(BaseModel):
    id: str
    owner_id: str
    title: str
    content: str
    date: str
