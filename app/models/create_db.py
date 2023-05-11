import logging

from sqlalchemy_utils import database_exists, create_database

from app.models.models import Base
from app.db import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_db():
    if not database_exists(engine.url):
        create_database(engine.url)
        Base.metadata.create_all(bind=engine)
    logger.info(f" database created: {database_exists(engine.url)}")

