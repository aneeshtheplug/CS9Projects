from Book import Book
from BookCollectionNode import BookCollectionNode
class BookCollection():
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def getNumberofBooks(self):
        temp = self.head
        counter = 0
        while temp != None:
            counter +=1
            temp = self.getNext()
        return counter
    
    def insertBook(self, book):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if book > current.getData():
                previous = current
                current = current.getNext()
            else:
                stop = True

        temp = BookCollectionNode(book)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def getBooksByAuthor(self, author):
        temp = self.head
        author_list = ''
        while temp != None:
            book = temp.getData()
            book_1 = book.getAuthor()
            if book_1.lower() == author.lower():
                author_list += book.getBookDetails() + '\n'
                temp = temp.getNext()
            else:
                temp = temp.getNext()
        return author_list
    
    def getAllBooksInCollection(self):
        temp = self.head
        book_list = ''
        while temp != None:
            book = temp.getData()            
            book_list += book.getBookDetails() + '\n'
            temp = temp.getNext()
        return book_list
    
    def removeAuthor(self, author):
        current = self.head
        if current == None:
            return 
        else:
            while current != None:
                book = current.getData()
                book_1 = book.getAuthor()
                if book_1.lower() == author.lower():
                    current.setData(current.getNext())
                    current.next = current.next.next

b0 = Book("Cujo", "King, Stephen", 1981)
b1 = Book("The Shining", "King, Stephen", 1977)
b2 = Book("Ready Player One", "Cline, Ernest", 2011)
b3 = Book("Rage", "King, Stephen", 1977)

bc = BookCollection()
bc.insertBook(b0)
bc.insertBook(b1)
bc.insertBook(b2)
bc.insertBook(b3)
print(bc.getAllBooksInCollection())
bc.removeAuthor('King, Stephen')