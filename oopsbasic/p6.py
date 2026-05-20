class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"The title of the book is: {self.title}")
        print(f"The author of the book is: {self.author}")
        print(f"The price of the book is: {self.price}")
    
b = Book("Harry Potter","Myself",900)
b.display()