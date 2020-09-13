import json

with open('bookdb.json','r') as conn:
    books = json.load(conn)
def startDelete():
    specialCommand = int(input("""
    Ashagidaki emrlerden birini daxil edin:
    1. Id -ye gore kitabin silinmesi
    2. Ada gore kitabin silinmesi
    3. Qiymete gore kitabin silinmesi
    4. Muellife gore kitabin silinmesi
    """))

    if specialCommand == 1:
        deleteForId()
        print("Kitab silindi.")
    elif specialCommand == 2:
        deleteForName()
        print("Kitab silindi.")
    elif specialCommand == 3:
        deleteForPrice()
        print("Kitab silindi.")
    elif specialCommand ==4:
        deleteForAuthor()
        print("Kitab silindi.")
    else:
        print("1-den 4-e qeder emr daxil edin.")


def deleteForId():
    id = int(input("Type Id: "))
    for book in books:
        if book['id'] == id:
            books.remove(book)

def deleteForName():
    name = input("Type Name: ")
    for book in books:
        if book['name'] == name:
            books.remove(book)

def deleteForPrice():
    price = int(input("Type Price: "))
    for book in books:
        if book['price'] == price:
            books.remove(book)

def deleteForAuthor():
    author = input("Type Author: ")
    for book in books:
        if book['author'] == author:
            books.remove(book)



with open('bookdb.json', 'w') as connection:
    json.dump(books, connection)