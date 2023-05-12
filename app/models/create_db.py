import logging

from sqlalchemy_utils import create_database, database_exists

from app.db import engine
from app.models.models import Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_db():
    if not database_exists(engine.url):
        create_database(engine.url)
        Base.metadata.create_all(bind=engine)
    logger.info(f" database created: {database_exists(engine.url)}")
