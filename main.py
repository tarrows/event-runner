from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"hello": "world"}

@app.get("/items/{item_id}")
def items(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
