# Magic methods : Dunder methods (double underscore) __init__, __str__, __eq__
#They are automatically called by many of Python's built-in operation.
#They allow developers to define or customize the behaviour of objects

class Book :
    def __init__(self, title , author , num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    #dunder string method
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other): #eq = equal
        return self.title == other.title and self.author == other.author

    def __lt__(self, other): #lt = less than
        return self.num_pages < other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == 'title':
            return  self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages

book1 = Book("The Hobbit" , "J.R.R Tolkien" , 310)
book2 = Book("The Hobbit" , "J.R.R Tolkien" , 310)
book3 = Book("Harry Potter and the Philosopher's Stone" , "J.k. Rowling" , 223)



#can print by __str__
print(book1)
print(book2)

#can be done using __eq__
print(book1 == book2)

#can be done using __lt__
print(book1 > book3)
print(book1 < book2)

#can be done using __add__
print(book1 + book2)
print(book2 + book3)

#search keywords using __contain__
print("Hobbit" in book1)
print("Gwen" in book3)


#using __getItem__
print(book1['title'])
print(book2['author'])
print(book3['num_pages'])
