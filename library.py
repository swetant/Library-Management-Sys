class Library:
    def __init__(self,name,booklist):
        self.name=name
        self.booklist=booklist
        self.lenddict={}
    def displaybooks(self):
        print("We have following books in our Library:")
        for book in self.booklist:
            print(book)
    def addbook(self,book):
        self.booklist.append(book)
        print("Book added successfully")
    def lendbook(self,user,book):
        if book in self.booklist:
            if book not in self.lenddict.keys():
                self.lenddict.update({book:user})
                print("Data has been updated")
            else:
                print(f"{book} is already taken by {self.lenddict[book]}")
        else:
            print("This book does not belongs to our Library")
    def returnbook(self,book):
        del self.lenddict[book]
        print(f"{book} has been returned successfully")
if __name__=="__main__":
    swetant=Library("Swetant",["Harry Potter","C++","History","Physics"])
    print(f"------Welcome to {swetant.name} Library Management System-----")
    while True:
        print("Your choices are:")
        print("1.Display Books")
        print("2.Lend Book")
        print("3.Add Books")
        print("4.Return Book")
        userchoice=int(input("Enter your choice: "))
        if userchoice==1:
            swetant.displaybooks()
        elif userchoice==2:
            user = input("Enter your name: ")
            book = input("Enter book name: ")
            swetant.lendbook(user,book)
        elif userchoice == 3:
            book = input("Enter book name: ")
            swetant.addbook(book)
        elif userchoice == 4:
            book = input("Enter book name: ")
            swetant.returnbook(book)
        else:
            print("Please enter valid option")
        userchoice2=input("Press c to continue and q to quit: ")
        if userchoice2=='c':
            continue
        elif userchoice2=="q":
            break
        else:
            print("Please enter a valid input")
            continue