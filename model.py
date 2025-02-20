from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    # Index to allow searching
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    age = Column(Integer, nullable=True)
    gender = Column(String, index=True, nullable=True)
    race = Column(String, index=True, nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', age={self.age}, gender='{self.gender}', race='{self.race}')>"
