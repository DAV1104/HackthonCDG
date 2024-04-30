from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] | None = None
    name: str
    email: str
    password: str