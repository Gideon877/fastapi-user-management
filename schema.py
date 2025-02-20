from pydantic import BaseModel

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
    id: int

    class Config:
        from_attributes = True
