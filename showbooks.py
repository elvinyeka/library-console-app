import json

def showBook():
    with open('bookdb.json', 'r') as conn:
        books = json.load(conn)

    for book in books:
        print(f"{book['id']} | {book['name']} | {book['price']} | {book['author']}")
