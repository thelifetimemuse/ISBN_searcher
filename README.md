# **Project Title:** ISBN_Searcher

## **Description:**

This Python project provides an MVP (Minimum Viable Product) prototype for an API that retrieves book information (title and number of pages) based on the ISBN code. It's designed to be used by API users to access book details efficiently.

## **User Story:**

As an API user, I want to be able to request book information such as title and number of pages based on the ISBN code.

```
-Is the langauge of the books important?
-Does the genre of the book matter?
-Would it be helpful if the API could also handle requests for additional parameters in the future?
```

## **Installation:**

## 1. **Prerequisites:**

- Python 3.12.2 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
  #- Necessary dependencies (specified in `pyproject.toml`)

## **Usage:**

1. **Run the API server on dev mode**

```sh
poetry run uvicorn main:app --reload
```

2. **Make an API request:**
```sh
curl "http://127.0.0.1:8000/api/v1/books?isbn=9780007420117"
```

3. **Make an API request in the browser:**
```sh
http://127.0.0.1:8000/api/v1/books?isbn=9780007420117 
```

## **Development:**

## **Testing:**

### **License:**

### **Contributing:**

```
For any further suggestions or contributions, please follow these instructions:
-Fork the repository on GitHub.
-Create a new branch from the main branch for your changes.
-Make your changes in your branch.
-Commit your changes with descriptive commit messages. Push your branch to your fork on GitHub.
-Open a pull request to submit your changes for review. (Please use appropriate titles and detailed descriptions)
```

### **Example Code Snippet:**
