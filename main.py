from addbook import *
from updatebook import *
from deletebook import *
from filterbook import *
from showbooks import *


def startMenu():
    menu = int(input("""
        Kitab magazasina xosh gelmisiniz!
        Ashagidaki menu-dan emrlerin birini secin:
        1. Yeni kitab elave etmek.
        2. Movcud kitabin melumatlarini deyishmek.
        3. Magazadaki kitabi silmek.
        4. Kitablari filtrelemek
        5. Magazadaki Butun Kitablar.
    """))
    if menu == 1:
        addBook()
    elif menu == 2:
        startUpdate()
    elif menu == 3:
        startDelete()
    elif menu == 4:
        startFind()
    elif menu == 5:
        showBook()
    else:
        print("Ancaq yuxaridaki emrlerden secim edin!")

startMenu()
