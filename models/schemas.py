from pydantic import BaseModel


class RequestBase(BaseModel):
    text: str
    created_at: str


class RequestCreate(RequestBase):
    pass


class Request(RequestBase):
    id: int
    created_at: str
    text: str

    class Config:
        orm_mode = True


class LinkBase(BaseModel):
    link: str
    request_id: int


class LinkCreate(LinkBase):
    pass


class Link(LinkBase):
    id: int
    link: str
    request: Request

    class Config:
        orm_mode = True
