from typing import Union

from fastapi import FastAPI
import uvicorn

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/{user_id}")
def read_user_me(user_id: str, q: Union[str, None] = None):
    return {"user_id": user_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
