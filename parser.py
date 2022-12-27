def get_people_data(person):
    return {
        "name": person.get("name"),
        "gender": person.get("gender"),
        "address": person.get("address"),
        "age": person.get("age")
    }


def get_book_data(book):
    return {
        "title": book.get("Title"),
        "author": book.get("Author"),
        "pages": book.get("Pages"),
        "genre": book.get("Genre")
    }
