from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100), nullable=False)
    completed = Column(Boolean, default=False)
