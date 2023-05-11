import uvicorn as uvicorn
from fastapi import FastAPI

from app.models.models import Link
from app.parser.google import Google
from db import new_session



app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/request/{request}")
async def read_item(request: str):
    parser = Google(request)
    return parser.load()


@app.get("/links/{request_id}")
async def read_item(request_id: int):
    with new_session() as session:
        data = session.query(Link).filter_by(request_id=request_id).all()
    return [link.link for link in data]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
