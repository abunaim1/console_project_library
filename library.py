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

usl = Library('UIU Smart Library')
admin = usl.addUser(1, 'Admin', 'Admin')
naim = usl.addUser(2, 'Abu Naim', '!@#abd')

currentUser = None

while True:
    if currentUser == None:
        print('Please, Login or Register your ID')
        print('For Login or Register press L/R: ')
        option = input()
        if option == 'L':
            id = int(input('Enter Your Id: '))
            password = input('Enter Your Password: ')

            match = False
            for user in usl.users:
                if user.id == id and user.password == password:
                    currentUser = user
                    match = True
                    break
            if match == False:
                print('No User Found! ')
        elif option == 'R':
            id = int(input('Enter Your Id: '))
            name = input('Enter your name: ')
            password = input('Enter Your Password: ')

            for user in usl.users:
                if user.id == id:
                    print('User already exist')
            user = usl.addUser(id, name, password)
            currentUser = user
    else:
        print(f'Welcom United Smart Library {currentUser.name}')
        if currentUser.name == 'Admin':
            print('Options: ')
            print('1: Add Book')
            print('2: Add User')
            print('3: Show All Book')
            print('4: LogOut')
            choice = int(input('Enter your choice: '))
            if choice == 1:



        

        
        

        