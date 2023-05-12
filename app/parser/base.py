import logging
from abc import ABC
from datetime import datetime
from typing import List

from selenium import webdriver

from app.db import new_session
from app.models import schemas as rpc
from app.models.models import Link, Request
from app.utils.selen_driver import get_webdriver

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Base(ABC):
    base_url: str
    request_table = Request
    link_table = Link

    def __init__(self, request: str):
        self.request = request

    def load(self) -> int:
        with new_session() as session:
            self.save_request()
            driver = get_webdriver()
            driver.get(f"{self.base_url}/search?q={self.request}")
            links = self.get_links(driver)
            cnt = self.extract(links, session)
        return cnt

    def save_request(self) -> None:
        with new_session() as session:
            now = datetime.now()
            instance = rpc.RequestCreate(created_at=now.strftime("%D-%M-%Y"), text=self.request)
            session.add(Request(**instance.dict()))

    def get_links(self, driver: webdriver) -> List[str]:
        raise NotImplementedError

    def extract(self, links, _session) -> int:
        raise NotImplementedError
