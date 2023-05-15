from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings

url = f"postgresql://{settings.db_user}" f":{settings.db_password}" f"@{settings.db_host}" f":{settings.db_port}/links"
engine = create_engine(url)

Session = sessionmaker(autoflush=False, bind=engine)


@contextmanager
def new_session(**kwargs) -> Session:
    _session = Session(**kwargs)
    try:
        yield _session
    except Exception:
        _session.rollback()
        raise
    else:
        _session.commit()
