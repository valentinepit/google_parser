from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class Request(Base):
    __tablename__ = "request"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    created_at = Column(String)
    text = Column(String)

    link = relationship("Link", back_populates="request")


class Link(Base):
    __tablename__ = "link"
    id = Column(Integer, primary_key=True, autoincrement=True)
    request_id = Column(Integer, ForeignKey("request.id"))
    link = Column(String)

    request = relationship("Request", back_populates="link")
