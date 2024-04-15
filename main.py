from fastapi import FastAPI

from searcher.provider import openlibrary as provider


app = FastAPI()


@app.get("/api/v1/books")
def books(isbn):
    result = provider.search_book(isbn)
    return {"response": result}
