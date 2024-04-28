'''Return Module'''


#importing Modules
import BookIndex    #bookIndex (Booklist Module)
import dt           #dt (date time module)

def returnBook():
    while(True):
        while(True):    #Name 
            print()
            a =     input("Please Enter your First Name: ")
            lName = input("Please Enter your Last Name:  ")
            print()
            if a.isalpha() and lName.isalpha():
                break
            print()
            print("       ----- [INVALID INPUT] ----- ")
            print("Please Enter the Name properly.")
            print()

        print()
        print("[INSTRUCTIONS]: ")
        print(" You are supposed to Enter the Name of Bill which was \n provided after Borrowing the Books. ")
        print()
        print("[Sample Name]: Borrow-XXXX(00000000-000000)")
        print()
        print("[WARNING]: ")
        print("1. '.txt' should not be included.")
        print("2. Space should not be Given.")
        print("3. Format should be same as Sample Name given above.")
        print()
        b = str(input("Please Enter your Name of Bill:  "))        #Asking for bill name
        print()
        print()
        print("--------------------------------------------------------------------------------")
        print("                                 [SEARCHING BILL]")        
        print("--------------------------------------------------------------------------------")
        print()

        # opening file ,reading bill and printing bill using exception handling
        try:
            c = str(b) + ".txt"
            with open(c,"r") as f:
                lines = f.readlines()
                lines = [a.strip('$') for a in lines]
            print("                             ----- [BILL FOUND]!!! -----")
            print()
            print("--------------------------------------------------------------------------------")
            print("                                  [READING BILL]")
            print("--------------------------------------------------------------------------------")
            print()
            print()
            print("[PRINTING BILL DETAILS]:")
            print()
            with open (c, "r") as f:
                data = f.read()
                print(data)
                break


        except:
            print
            print("     ----- [BILL NOT FOUND]!!! ----- ")
            print()
            print("Please Read Instructions properly and try again.")
            print()
            returnBook()        #restarting after value error


    retdict = BookIndex.bDex() # fetching book index

    #for fine using exception handling
    fine = 0
    while (True):
        late = input("Are the Books Returned Late? (Y/N): ")
        
        if(late.upper() == "Y"):
            try:
                days1 = int(input("By how many Days are the Books Returned Late? : "))
                fine = 3 * days1    # $ 3 per day
                break
            except ValueError:
                print()
                print("       ----- [INVALID INPUT] ----- ")
                print("Please Enter the Value properly.")
                print()
        else:
            break


    lob = []            #list of books
    total = 0
    z = 1

    #looping, searching for bookname in bill, increasing quantity and replacing with previous value in txt file
    while z < 8:
        string = str(retdict[z][0])     #looping book name for searching and comparing in the bill 
        with open(c,"r") as f:
                if string in f.read():
                    retdict3 = int(retdict[z][2]) + 1       #increasing quantity
                    with open("books.txt","r") as f:
                        filedata = f.read()
                    filedata = filedata.replace(str(retdict[z][2]),str(retdict3))       # replacing value
                    with open("books.txt","w") as f:
                        f.write(filedata)
                    retdict[z][2] = retdict3      #quantity updating value

                    #for total cost
                    cost = retdict[z][3]
                    pob = int(cost.replace("$",""))
                    total = total + pob

                    #appending matching book names in lob 
                    Lob = retdict[z][0]
                    lob.append(Lob)
        z = z + 1


    #printing customer details
    print()
    print()
    print("------------------------- Customer Return Details ------------------------------")
    print("Name of the Customer: " + a + " " + lName)
    print("The Price for Borrowed Books is: " + "$" + str(total))
    print("Total Fine: " + "$" + str(fine))
    print("Toatl Price: " + "$" + str(total) + "+" +"$"+ str(fine) + " = " + "$" + str(total + fine))
    print("Date and time of Return: " + dt.getDate() + "  " + dt.getTime())
    print("Name of the Returned Book: " , *lob, sep = "\n")
    print("----------------------------------- END ----------------------------------------")
              

    #return receipt
    x = "Return-" + a + "(" + dt.getDat() + ")" + ".txt"
    with open(x,"w+") as f:
        f.write("               ====================================================== \n")
        f.write("                            The Library Management System \n")
        f.write("               ====================================================== \n")
        f.write("\n\n\n")
        f.write("------------------------- Customer Return Details ------------------------------\n\n")
        f.write("Name of the Customer: " + a + " " + lName + "\n")
        f.write("The Price for Borrowed Books: " + "$" + str(total) + "\n")
        f.write("Total Fine: " + "$" + str(fine) + "\n")
        f.write("Toatl Price: " + "$" + str(total) + "+" +"$"+ str(fine) + " = " + "$" + str(total + fine) + "\n")
        f.write("Date and time of Return: " + dt.getDate() + "  " + dt.getTime() + "\n")
        f.write("Name of the Returned Books: ")
        for element in lob:
            f.write(element + "\n")
        f.write("----------------------------------- END ----------------------------------------")

    print()
    print("          ************** Thank you for your Patronage ***************")
    print()

    #refreshed dictionary
    print()
    print("[NOTICE]: Dictionary has been Updated!!!")
    print()
    print("                          Dictionary (UPDATED)")
    print("--------------------------------------------------------------------------------")
    print(str(retdict))
    print("--------------------------------------------------------------------------------")
    print()
            
    #refreshed book index
    print()
    print ("                        [BOOK INDEX](UPDATED)")


    print("--------------------------------------------------------------------------------")
    print(" {:<10} {:<20} {:<16} {:<12} {:<12} ".format('Book ID', 'Book Name', 'Author', 'Quantity', 'Price'))
    print("--------------------------------------------------------------------------------")

#assigning bookID as key and others as value
    for key,value in retdict.items():
        bookID = key
        BookName, Writer, Quantity, Price = value
        print(" {:<10} {:<18} {:<20} {:<10} {:<12} ".format(bookID,BookName , Writer, Quantity, Price))
    print("--------------------------------------------------------------------------------")
    print()
