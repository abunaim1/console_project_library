class Book:
    def __init__(self, name, quantity, id) -> None:
        self.name = name
        self.quantity = quantity
        self.id = id

class User:
    def __init__(self, name, id, password) -> None:
        self.name = name
        self.id = id
        self.password = password
        self.borrowedBooks = []
        self.returnBooks = []

class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.users = []
        self.books = []
    def addBooks(self,id, name, quantity):
        book = Book(id, name, quantity)
        self.books.append(book)
    def addUser(self, id, name, password):
        user = User(id, name, password)
        self.users.append(user)
    

        
        

        