from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/books")
def read_root(isbn):
    return {"response": []}
