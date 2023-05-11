import logging

from selenium.webdriver.common.by import By

from app.models import schemas as rpc
from app.parser.base import Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Google(Base):
    base_url = "https://google.com/"

    def get_links(self, driver) -> list:
        result = []
        links = driver.find_elements(By.CLASS_NAME, "yuRUbf")
        for link in links:
            result.append(link.find_element(By.TAG_NAME, "a").get_attribute("href"))
        return result

    def extract(self, links, _session):
        cnt = 0
        request = _session.query(self.request_table).order_by(self.request_table.id.desc()).first()
        for link in links:
            instance = rpc.LinkCreate(
                link=link,
                request_id=request.id
            )
            _session.add(self.link_table(**(instance.dict())))
            cnt += 1
        logger.info(f"For {self.request} saved {cnt} links")
        return cnt
