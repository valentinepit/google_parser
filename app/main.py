import uvicorn as uvicorn
from fastapi import FastAPI

from app.models.create_db import create_db
from app.models.models import Link
from app.parser.google import Google

from .db import new_session

app = FastAPI()
create_db()


@app.get("/")
async def read_root():
    return "You can use /docs to see functionality"


@app.get("/request/{request}")
async def search_request(request: str):
    parser = Google(request)
    cnt = parser.load()
    return cnt


@app.get("/links/{request_id}")
async def links_by_id(request_id: int):
    with new_session() as session:
        data = session.query(Link).filter_by(request_id=request_id).all()
        return [link.link for link in data] if data else "No links or wrong id"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
