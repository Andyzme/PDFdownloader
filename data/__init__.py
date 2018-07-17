from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


_db_uri = 'postgresql://postgres:postgres@host.docker.internal:5050'
# _db_uri = 'postgresql://postgres:postgres@localhost:5050'
_engine = create_engine(_db_uri, echo=False)


def make_db_session() -> sessionmaker:
    Session = sessionmaker(bind=_engine)
    return Session()


session = make_db_session()
