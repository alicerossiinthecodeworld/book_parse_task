import json
import csv
from parser import get_people_data, get_book_data
from sorting import get_equals_books, add_books_to_people

people_list = []
with open("users.json", "r") as file:
    people = json.load(file)
for person in people:
    people_list.append(get_people_data(person))


books_list = []
with open("books.csv", "r") as file:
    books = list(csv.DictReader(file))
for book in books:
    books_list.append(get_book_data(book))

equals_books_gen = get_equals_books(books_list, len(people_list))

people_with_books = []
for person in people_list:
    people_with_books.append(add_books_to_people(person, next(equals_books_gen)))

with open("result.json", "w") as outfile:
    json.dump(people_with_books, outfile)
