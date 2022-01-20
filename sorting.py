import numpy as np


def get_equals_books(books: list, people_count: int):
    for item in np.array_split(books, people_count):
        yield list(item)


def add_books_to_people(people: dict, equal_books: list):
    people["books"] = equal_books
    return people