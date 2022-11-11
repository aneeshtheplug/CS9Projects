from BookCollection import *

def test__getBookDetails():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    assert b.getBookDetails() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011"
    b1 = Book("The Shining", "King, Stephen", 1977)
    assert b1.getBookDetails() == "Title: The Shining, Author: King, Stephen, Year: 1977"

def test__getYear():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    assert b.getYear() == 2011

def test__getTitle():
    b1 = Book("The Shining", "King, Stephen", 1977)
    assert b1.getTitle() == "The Shining"

def test__recursiveSearchTitle():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b3 = Book("Rage", "King, Stephen", 1979)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b3)
    assert bc.recursiveSearchTitle("CUJO", bc.head) == True
    assert bc.recursiveSearchTitle("Twilight", bc.head) == False
    assert bc.recursiveSearchTitle("rAgE", bc.head) == True
    assert bc.recursiveSearchTitle("Fade", bc.head) == False

def test__removeAuthor():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1979)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    bc.removeAuthor("King, Stephen")
    assert bc.getAllBooksInCollection() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011" + '\n'

def test__getBooksByAuthor():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getBooksByAuthor("KING, Stephen") == "Title: Rage, Author: King, Stephen, Year: 1977" + '\n' + "Title: The Shining, Author: King, Stephen, Year: 1977" + '\n' "Title: Cujo, Author: King, Stephen, Year: 1981" + '\n'
    assert bc.getBooksByAuthor("Orwell, George") == ''
    assert bc.getBooksByAuthor("Cline, Ernest") == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011" + '\n'

def test__isEmpty():
    bc = BookCollection()
    assert bc.isEmpty() == True
    b1 = Book("The Shining", "King, Stephen", 1977)
    bc.insertBook(b1)
    assert bc.isEmpty() == False

def test__getNumberofBooks():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getNumberofBooks() == 3
    bc.removeAuthor("King, Stephen")
    assert bc.getNumberofBooks() == 1
    bc.insertBook(b1)
    assert bc.getNumberofBooks() == 2


