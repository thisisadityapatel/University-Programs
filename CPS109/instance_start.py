#making a small class Books which store the deetails of the books and takes in the discount price to find the new price
#also use of the secret attribute of the class


class Books:
    #variable to count the number of books
    Count = 0
    def __init__(self, name, author, pages, price):
        self.name = name
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "Aditya Patel is the best"
    
    def show_data(self):
        print("Book Name : ", self.name)
        print("Author Name : ", self.author)
        print("Pages :", self.pages)
        print("Price : ", self.price)
    
    def set_discount(self, discount):
        self._discount = discount

    def give_price(self):
        if hasattr(self, "_discount"):
            print(self.price - (self.price * self._discount))
        else:
            print(self.price)
    
b1 = Books("Crazy life with uncle Ken.", "Ruskin Bond", "100", "120")
b2 = Books("Life is what you make it", "Peter Buffet", 1200, 500)

#using VARS to print the information of the first book
print("using the VARS method : ", vars(b1))

#printing using the inbuilt function of the book
print(b2.show_data())

#showing the secret character
print(b1._Books__secret)

#printing the number of books entered
print(Books.Count)

#printing the type of the books and comparing them
if type(b1) == type(b2):
    print(True)
else:
    print(False)

#using the dir attribute to get the location of the first book
print(dir(b1))








    
    