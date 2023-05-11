import logging
from abc import ABC
from datetime import datetime

import models.schemas as rpc

from db import new_session
from models import Request, Link

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Base(ABC):
    base_url: str
    request_table = Request
    link_table = Link

    def __init__(self, request: str):
        self.request = request

    def load(self):
        return NotImplementedError

    def save_request(self):
        with new_session() as session:
            now = datetime.now()
            instance = rpc.RequestCreate(
                created_at=now.strftime("%D-%M-%Y"),
                text=self.request
            )
            session.add(Request(**instance.dict()))

    def get_links(self, driver):
        return NotImplementedError

    def extract(self, links, _session):
        return NotImplementedError
