class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
    def addbooks(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)
    
    def showInfo(self):
        print(f"the library has {self.noBooks} books. The Books are")
        for book in self.books:
            print(book)

l1 = Library()
l1.addbooks("Harry Potter")
l1.addbooks("FBI")
l1.addbooks("Suits")
l1.addbooks("BodyGuard")
l1.addbooks("Family Man")
l1.addbooks("Sherlock Homes")
l1.showInfo()



