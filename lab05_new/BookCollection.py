from Book import Book
from BookCollectionNode import BookCollectionNode
class BookCollection():
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def getNumberOfBooks(self):
        temp = self.head
        counter = 0
        while temp != None:
            counter +=1
            temp = temp.getNext()
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
            book = temp.getData().getAuthor()
            if book.lower() == author.lower():
                author_list += temp.getData().getBookDetails() + '\n'
                temp = temp.getNext()
            else:
                temp = temp.getNext()
        return author_list
    
    def getAllBooksInCollection(self):
        temp = self.head
        book_list = ''
        while temp != None:
            book_list += temp.getData().getBookDetails() + '\n'
            temp = temp.getNext()
        return book_list
    
    def removeAuthor(self, author):
        current = self.head
        previous = None
        if current == None:
            return
        else:
            while current != None:
                book = current.getData().getAuthor()
                if previous == None and (book.lower() == author.lower()):
                    self.head = current.getNext()
                    current = self.head
                    previous = None
                elif previous != None and (book.lower() == author.lower()):
                    current = current.getNext()
                    previous.setNext(current)
                else:
                    previous = current
                    current = current.getNext()
            return 
            
    def recursiveSearchTitle(self, title, bookNode):
        if bookNode == None:
            return False
        else:
            book = bookNode.getData().getTitle()
            if book.lower() == title.lower():
                return True
            else:
                bookNode = bookNode.getNext()
                return self.recursiveSearchTitle(title, bookNode)

'''b0 = Book("Cujo", "King, Stephen", 1981)
b1 = Book("The Shining", "King, Stephen", 1977)
b2 = Book("Ready Player One", "Cline, Ernest", 2011)
b3 = Book("Rage", "King, Stephen", 1979)

bc = BookCollection()
bc.insertBook(b0)
bc.insertBook(b1)
bc.insertBook(b2)
bc.insertBook(b3)
bc.removeAuthor("King, Stephen")
print(bc.getAllBooksInCollection())'''