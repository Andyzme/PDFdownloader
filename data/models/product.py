from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.sql import func


Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    created = Column(DateTime(timezone=True), server_default=func.now())
