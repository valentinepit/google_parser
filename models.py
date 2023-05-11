from datetime import datetime
from enum import Enum

from pydantic import BaseModel, HttpUrl


class Request(BaseModel):
    text: str
    created_at: str


class Tags(BaseModel):
    url: str
    request: Request
