from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
import services, model, schema
from database import engine, get_db, database

# Create database tables from models
model.Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting lifespan up ....")
    yield
    print("Shutting lifespan down ....")

app = FastAPI(lifespan=lifespan)

# Create User
@app.post("/users/", response_model=schema.UserResponse)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = services.create_user(db, user)
    print(db_user)
    return db_user

@app.get("/users/", response_model=list[schema.UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return services.get_users(db, skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model=schema.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = services.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    success = services.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}


# TODO: create filter and groups for stats - e.g most common names, average age, race and etc