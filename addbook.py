import random
import json



def addBook():
    with open('bookdb.json', 'r') as conn:
        books = json.load(conn)
    def newBook():
        _id = random.randint(0, 100)
        _name = input("Book Name: ")
        _price = int(input("Book Price: "))
        _author = input("Book Author: ")

        book = {
            "id": _id,
            "name": _name,
            "price": _price,
            "author": _author
        }
        books.append(book)



    i = 0
    while True:
        i += 1
        print(f"{i}-ci kitabin melumatlarini daxil edin: ")
        newBook()
        Davam = int(input("Yeni kitab elave elemek isteyirsiz?(1-e basin)\n (eks halda 0-ra basin)"))
        if Davam == 1:
            continue
        else:
            break

    with open('bookdb.json', 'w') as connection:
        json.dump(books, connection)


