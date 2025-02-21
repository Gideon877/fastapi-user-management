from pydantic import BaseModel
from uuid import UUID

class UserBase(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: str
    race: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserResponse(UserBase):
    id: UUID  # 🔥 Change from int to UUID

    class Config:
        from_attributes = True
