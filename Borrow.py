'''Module for Borrow Function'''
#importing other python files

import dt           #for datetime 
import BookIndex    #for lists of books
import math
#class for borrowing books function
def borrowBook():

#book ID
    
    i = 0
    dict = BookIndex.bDex()
    print()
    print("[NOTICE]: Please Enter the BookID of the Book to be borrowed.")
    print()
    
    while(True):
        bID =  int(input("Please Enter the Book ID: "))
        print()
        if bID <= len(dict) and bID > 0:  #for when book ID is entered wrong
            break
        print()
        print("       ----- [INVALID INPUT] ----- ")
        print("Please Enter the Book ID properly.")
        print()
        
   #for when quantity is not zero       
    if int(dict[bID][2]) >= 1:
        print("[NOTICE]: The Book is Available to be Borrowed.")
   #for when quantity is zero     
    elif int(dict[bID][2]) == 0:
        print("[NOTICE]: The Book is Currently Out of Stock.")
        print("Please try at a Later Date.")
#using 'isalpha' method to compare whether input is string or not.
        #for first name 
    while(True):
        print()
        firstName = input("Please Enter the First Name of the Borrower: ")
        if firstName.isalpha():
            break
        print("       ----- [INVALID INPUT] ----- ")
        print("Please Enter the Name properly.")

    #for last name    
    while(True):
        lastName = input("Please Enter the Last Name of the Borrower:  ") 
        if lastName.isalpha():
            print()
            print("[Book Borrowed Successfully]!!!")
            print()
            break
        print()
        print("       ----- [INVALID INPUT] ----- ")
        print("Please Enter the Name properly.")

#decreasing quantity after borrowing
    dict1 = int(dict[bID][2]) - 1
    with open("books.txt","r") as f:
        filedata = f.read()
    filedata = filedata.replace(str(dict[bID][2]),str(dict1))
    with open("books.txt","w") as f:
        f.write(filedata)
    dict[bID][2] = dict1
    
#name of books
    NOB = dict[bID][0]
    
    cost = dict[bID][3]                 
    POB = int(cost.replace("$",""))     #stripping '$' & converting into 'int' for adding




        

            
    #refreshed dictionary
    print()
    print("[NOTICE]: Dictionary has been Updated!!!")
    print()
    print("                          Dictionary (UPDATED)")
    print("--------------------------------------------------------------------------------")
    print(str(dict))
    print("--------------------------------------------------------------------------------")
    
        #refreshed book index
    print()
    print ("                         [BOOK INDEX](UPDATED)")


    print("--------------------------------------------------------------------------------")
    print(" {:<10} {:<20} {:<16} {:<12} {:<12} ".format('Book ID', 'Book Name', 'Author', 'Quantity', 'Price'))
    print("--------------------------------------------------------------------------------")

#assigning bookID as key and others as value
    for key,value in dict.items():
        bookID = key
        BookName, Writer, Quantity, Price = value
        print(" {:<10} {:<18} {:<20} {:<10} {:<12} ".format(bookID,BookName , Writer, Quantity, Price))
    print("--------------------------------------------------------------------------------")
    print()

#borrowing multiple books
    nob = []            #using list to store name of borrowed books
    nob.append(NOB)     #appending the name of first borrowed book
    dup = []            #list storing bookID
    dup.append(bID)
    while(True):
        print()
        con = input ("Do you want to Borrow Another Book? (Y/N): ")
        if con == "y" or con == "Y" or con == "Yes" or con == "yes" :
            while(True):
                print()
                print("[NOTICE]: Please Enter the BookID of the Book to be Borrowed.")
                print()
                bID1 =  int(input("Please Enter the Book ID: "))
                    
                    
                #for finding duplicate books while borrowing multiple books
                l1 = 0
                for x in range (len(dup)):
                    if dup[x] == bID1 or dict[bID1][2] == 0:
                        l1 = 1
                if bID1 <= len(dict) and bID1 != 0 and bID1 != bID and l1 == 0:  #when book ID is entered wrong
                    print("[Book Borrowed Successfully]!!!")
                    dup.append(bID1)
                    break
                print()
                print("[WARNING]: One person cannot Borrow the Same Book.")
                print("Please Enter Book ID Correctly.")
 
              #decreasing quantity after borrowing     
            dict2 = int(dict[bID1][2]) - 1
            with open("books.txt","r") as f:
                filedata = f.read()
            filedata = filedata.replace(str(dict[bID1][2]),str(dict2))
            with open("books.txt","w") as f:
                f.write(filedata)
            dict[bID1][2] = dict2
    

            #appending names of books in the list
            NOB1 = dict[bID1][0]
            nob.append(NOB1)

            #calculating total price
            cost1 = dict[bID1][3]
            pob = int(cost1.replace("$","")) #stripping $ and converting into 'int' for adding
            POB = POB + pob

            #refreshed dictionary
            print()
            print("[NOTICE]: Dictionary has been Updated!!!")
            print()
            print("                          Dictionary (UPDATED)")
            print("--------------------------------------------------------------------------------")
            print(str(dict))
            print("--------------------------------------------------------------------------------")
            print()
            
            #refreshed book index
            print()
            print ("                        [BOOK INDEX](UPDATED)")


            print("--------------------------------------------------------------------------------")
            print(" {:<10} {:<20} {:<16} {:<12} {:<12} ".format('Book ID', 'Book Name', 'Author', 'Quantity', 'Price'))
            print("--------------------------------------------------------------------------------")

#assigning bookID as key and others as value
            for key,value in dict.items():
                bookID = key
                BookName, Writer, Quantity, Price = value
                print(" {:<10} {:<18} {:<20} {:<10} {:<12} ".format(bookID,BookName , Writer, Quantity, Price))
            print("--------------------------------------------------------------------------------")
            print()

        else:
            print()
            print()
            print("------------------------- Customer Burrow Details ------------------------------")
            print("Name of the Customer: " + firstName + " " + lastName)
            print("Toatl price: " + "$" + str(POB))
            print("Date and time of Borrow: " + dt.getDate() + "  " + dt.getTime())
            print("Final Date to Return: " + dt.retdat() + "   - (After 10 Days)" )
            print("Name of the Borrowed Book: " , *nob, sep = "\n")
            print("----------------------------------- END ----------------------------------------")
            break


    print("          ************** Thank you for your Patronage ***************")
    print()
    #billing (receipt)
    t = "Borrow-" + firstName + "(" + dt.getDat() + ")" + ".txt"                #for unique name of borrowing receipt/bill
    with open (t,"w+") as f:       #w+ is for both reading and writing
        f.write("               ====================================================== \n")
        f.write("                            The Library Management System \n")
        f.write("               ====================================================== \n")
        f.write("\n\n\n")
        f.write("------------------------- Customer Burrow Details ------------------------------\n\n")
        f.write("Name of the Customer: " + firstName + " " + lastName + "\n")
        f.write("The Price for Borrowed Books is: " + "$" + str(POB) + "\n")
        f.write("Date and time of Borrow: " + dt.getDate() + "  " + dt.getTime() + "\n")
        f.write("Final Date to Return:    " + dt.retdat() + "\n" )
        f.write("Name of the Borrowed Books: ")
        for element in nob:
            f.write(element + "\n")
        f.write("----------------------------------- END ----------------------------------------")



