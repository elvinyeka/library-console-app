import json

with open('bookdb.json', 'r') as conn:
    books = json.load(conn)
def startUpdate():

    specialCommand = int(input("""
    Ashagidaki emrlerden birini daxil edin:
    1. ID-ye gore kitabin adinin deyishdirilmesi
    2. ID-ye gore kitabin qiymetinin deyishdirilmesi
    3. ID-ye gore kitabin muellifinin deyishdirilmesi
    """))

    if specialCommand == 1:
        updateForName()
        print("Kitabin adi deyishdirildi.")
    elif specialCommand == 2:
        updateForPrice()
        print("Kitabin qiymeti deyishdirildi.")
    elif specialCommand == 3:
        updateForAuthor()
        print("Kitabin muellifi deyishdirildi.")
    else:
        print("1-den 3-e qeder emr daxil edin.")

    with open('bookdb.json', 'w') as connection:
        json.dump(books, connection)


def updateForName():
    id = int(input("Type Id: "))
    for book in books:
        if book['id'] == id:
            newName = input("Change Name : ")
            book["name"] = newName

def updateForPrice():
    id = int(input("Type Id: "))
    for book in books:
        if book['id'] == id:
            newPrice = int(input("Change Price : "))
            book["price"] = newPrice

def updateForAuthor():
    id = int(input("Type Id: "))
    for book in books:
        if book['id'] == id:
            newAuthor = input("Change Author : ")
            book["author"] = newAuthor




