from sqlalchemy_utils import database_exists, create_database

import models
from db import engine


def create_db():
    if not database_exists(engine.url):
        create_database(engine.url)
    print(f" database created: {database_exists(engine.url)}")


create_db()
models.Base.metadata.create_all(bind=engine)

