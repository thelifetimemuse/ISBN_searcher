import requests


SEARCH_URL = "https://openlibrary.org/search.json?isbn={}&fields=title,number_of_pages_median"


def search_book(isbn):
    """Search book information based on isbn
    Returns the title and the number of pages.
    """
    result = requests.get(SEARCH_URL.format(isbn))
    if result.status_code == 200:
        return result.json()["docs"]
