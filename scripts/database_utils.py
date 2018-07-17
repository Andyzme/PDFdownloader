from sqlalchemy import Table, Column, String, DateTime, Integer
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.sql import func

from data import session
from data.models.product import Product

_db_uri = 'postgresql://postgres:postgres@host.docker.internal:5050'
# _db_uri = 'postgresql://postgres:postgres@localhost:5050'
_engine = create_engine(_db_uri, echo=False)
metadata = MetaData(_engine)


def create_all_db() -> None:
    metadata.create_all()


def drop_all_db() -> None:
    metadata.drop_all()


# Table schemas
product = Table('products', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String, unique=True, nullable=False),
                Column('created', DateTime, unique=False, nullable=False,
                       server_default=func.now()))


def db_create_seed():
    # Drop all
    drop_all_db()
    # Create all
    create_all_db()
    # Seed all
    test_product_1 = Product(name='test_1')
    session.add(test_product_1)
    test_product_2 = Product(name='test_2')
    session.add(test_product_2)
    test_product_3 = Product(name='test_3')
    session.add(test_product_3)
    test_product_4 = Product(name='test_4')
    session.add(test_product_4)
    test_product_5 = Product(name='test_5')
    session.add(test_product_5)
    test_product_6 = Product(name='test_6')
    session.add(test_product_6)
    test_product_7 = Product(name='test_7')
    session.add(test_product_7)
    test_product_8 = Product(name='test_8')
    session.add(test_product_8)
    session.commit()
