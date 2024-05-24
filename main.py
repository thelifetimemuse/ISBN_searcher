from fastapi import FastAPI


app = FastAPI()


@app.get("/api/v1/books")
def books(isbn, provider_name):
    """
    Endpoint /api/v1/books?isbn=1&provider_name=XXX
    """

    provider = None

    if provider_name == "openbooks":
        from searcher.provider import openlibrary as provider
    elif provider_name == "muse":
        from searcher.provider import local as provider
    elif provider_name == "bookfinder":
        from searcher.provider import bookfinder as provider
    else:
        return {"error": "no provider specified"}

    result = provider.search_book(isbn)
    return {"response": result}
