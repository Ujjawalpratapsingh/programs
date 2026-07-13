class Library:
    def __init__(self):
       self.num_books= 0
       self.books=[]
    def add(self,name):
       self.name=name
       self.books.append(self.name)
       self.num_books+=1
    def get(self):
       return self.books
    def numbooks(self):
        return self.num_books
print("Press A for adding a book \n P for for printing all the books \n N for getting the Number of books ")
l1=Library()
while True:
   a= input("Enter your choice: ")
   a=a.strip()
   a=a.upper()
   if a == "A":
      name_book= input("Enter the name of the Book : ")
      l1.add(name_book)
   elif a == "P":
       print(l1.get())
   elif a == "N":
      print(f"The number of books are: {l1.numbooks()}")
   elif a == "q":
      break
   else:
      print("Invalid Input")