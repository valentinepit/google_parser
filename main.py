from typing import Union

import uvicorn as uvicorn
from fastapi import FastAPI
from parser.google import Google
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/request/{request}")
async def read_item(request: str, q: Union[str, None] = None):
    parser = Google(request)
    return parser.load()



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)