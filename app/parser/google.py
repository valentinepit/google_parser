import logging

from selenium.webdriver.common.by import By

from app .models import schemas as rpc
from app.parser.base import Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def interceptor(request):
    del request.headers["Referer"]
    request.headers["Referer"] = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                      "(KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }


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
            print(link)
            instance = rpc.LinkCreate(
                link=link,
                request_id=request.id
            )
            _session.add(self.link_table(**(instance.dict())))
            cnt += 1
        return cnt
