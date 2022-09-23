# BookStore
An API for book store owners.

[![Bookstore Video](https://img.youtube.com/vi/eqKxAy7EV-0/0.jpg)](http://www.youtube.com/watch?v=eqKxAy7EV-0)

----

## Instructions

run `cd bookstore`, `python -m venv .venv` and `source .venv/bin/activate` to create and activate virtual environment.
To start server, run `python manage.py runserver` and visit `http://localhost:8000/admin`

----

## Core functionalities:

- Create book inventory
- View inventory
- Add / Delete books
- Authentication

## Planned functionalities:

- Find books

----

## API Endpoints

- `api/bookstores/` #get a list of all bookstores
- `api/bookstores/{pk}/$` #get, delete, or edit a particular book store with the - id pk
- `api/books/$` #get a list of all books
- `api/books/{pk}/$` #get, delete, or edit a particular book store with the id pk
