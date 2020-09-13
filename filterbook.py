import json

with open('bookdb.json','r') as conn:
    books = json.load(conn)

def startFind():
    specialCommand = int(input("""
    Ashagidaki emrlerden birini daxil edin:
    1. Ada gore kitabin tapilmasi
    2. Muellife gore kitabin tapilmasi
    3. Qiymete gore kitabin tapilmasi
    """))

    if specialCommand == 1:
        keyword = input("Type keyword: ")
        findBookByName(keyword)

    elif specialCommand == 2:
        keywordAuthor = input("type Author: ")
        findByAuthor(keywordAuthor)
    elif specialCommand ==3:
        keyprice = int(input("Type price: "))
        findByPrice(keyprice)

    else:
        print("1-den 2-e qeder emr daxil edin.")


def findBookByName(_keyword):
    for book in books:
        if _keyword in  book["name"]:
            print(f" {book['id']} | {book['name']} | {book['price']} | {book['author']}")

def findByAuthor(_keywordAuthor):
    for book in books:
        if _keywordAuthor in book["author"]:
            print(f" {book['id']} | {book['name']} | {book['price']} | {book['author']}")


def findByPrice(keyprice):
    for book in books:
        _price = book["price"]
        if _price < keyprice:
            print(f" {book['id']} | {book['name']} | {book['price']} | {book['author']}")

