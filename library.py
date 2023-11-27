class Book:
    def __init__(self, id, name, quantity) -> None:
        self.name = name
        self.quantity = quantity
        self.id = id

class User:
    def __init__(self, id, name, password) -> None:
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
        print(f'Book {name} Added successfully! ')

    def addUser(self, id, name, password):
        user = User(id, name, password)
        self.users.append(user)
        print('Registration Sucfully Completed !')

    def borrowBook(self, user, book_name):
        for book in self.books:
            if book.name == book_name:
                if book in user.borrowedBooks:
                    print('You have already Taken this book')
                    return
                elif book.quantity == 0:
                    print('No Copy available ')
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quantity -= 1
                    print('Borrowed Book successfully')
                    return
        print(f'Not found any book with this name {book_name}')

    def returnBook(self, user_name, book_name):
        for book in self.books:
            if book.name == book_name:
                if book in user.borrowedBooks:
                    user.returnBooks.append(book)
                    user.borrowedBooks.remove(book)
                    book.quantity += 1
                    print('Returned Book successfully')
                    return
        print(f'Not found any book with this name {book_name}')        



usl = Library('UIU Smart Library')
admin = usl.addUser(1, 'Admin', 'admin')

currentUser = admin 

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
                if user.password == password:
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
        print(f'Welcom Back {currentUser.name} ')
        if currentUser.name == 'Admin':
            print('Options: ')
            print('1: Add Book')
            print('2: Add User')
            print('3: Show All Book')
            print('4: LogOut')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                id = int(input('Enter Book id: '))
                book = input('Enter Book Name: ')
                quantity = int(input('Enter Quantity: '))
                usl.addBooks(id, book, quantity)
            elif choice == 3:
                for book in usl.books:
                    print(f'Book Name: {book.name} ID: {book.id}')
            elif choice == 4:
                currentUser = None
        else:
            print('Options: ')
            print('1: Borrow Book')
            print('2: Return Book')
            print('3: Show all borrowed book')
            print('4: Show History')
            print('5: LogOut')
            choice = int(input())
            if choice == 1:
                name = input('Enter Book Name: ')
                usl.borrowBook(currentUser, name)
            elif choice == 2:
                name = input('Enter Book Name: ')
                usl.returnBook(currentUser, name)
            elif choice == 3:
                for book in currentUser.borrowedBooks:
                    print(book.name)
            elif choice == 4:
                for book in currentUser.returnBooks:
                    print(book.name)
            elif choice == 5:
                currentUser = None









        

        
        

        