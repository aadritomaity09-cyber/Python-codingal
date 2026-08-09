class Book:
    def __init__(self,title,author,is_borrowed=False):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
    def borrow(self):
        is_borrowed=True
        print("is_borrwoed is true")
    def return_book(self):
        is_borrowed=False
        print("is_borrowed is false")
lego=Book("Lego","Jake Nathan")
harry_potter=Book("Harry Potter","J.K.Rowling")
percy_jackson=Book("Percy jackson","Rick Riordan")
lego.borrow()
lego.return_book()
