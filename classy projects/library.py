#library
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return True
        else:
            return False
    
    def bring_back(self):
        self.available = True

    def get_book_info(self):
        return f'Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nAvailable: {self.available} \n'
    

    
class Client:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []



class Library:
    def _init_(self):
        self.books = {}
        self.clients = {}
        self.history = []

    def add_book(self, title, author, year):
        print(f'Book {title} adding \n')
        self.books[title] = Book(title, author, year)
        self.history.append(f'Book {title} added')

    def borrow_book(self, title, name):
        if self.books[title].available == True:
            self.clients[name]= Client(name)
            self.clients[name].borrowed_books.append(title)
            self.books[title].borrow()
            self.history.append(f'{name} borrowed {title}')
        else:
            return f'Book {title} is not available \n'

    def return_book(self, title, name):

        self.books[title].bring_back()
        self.clients[name].borrowed_books.remove(title)
        self.history.append(f'{name} returned {title} \n')
        
    def get_available_books(self):
        print('----AVAILABLE----')
        for n, book in self.books.items():
            if book.available:
                print(book.get_book_info() ,'\n')

    def get_not_available(self):
        print('----NOT AVAILABLE----')
        for n, book in self.books.items():
            if not book.available:
                print(book.get_book_info(), '\n')

    def get_history(self):
        for entry in self.history:
            print(entry)

    def get_user_borrowed_Books(self, name):
        print(f'Books borrowed by {name}:')
        for book in self.clients[name].borrowed_books:
            print(book)





bashat = Library()

bashat.add_book('KG', 'Atabek', 2022)
bashat.add_book('KG2', 'Atabek', 2022)

bashat.get_available_books()


bashat.borrow_book('KG', 'Akbar')
bashat.get_not_available()
bashat.get_history()