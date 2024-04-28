'''Main Module'''
#importing other python files

import dt                   #for datetime
import Borrow               #for Borrow function
import Return               #for Return function            
import BookIndex            #for list of books



#title
def title():
    print()
    print("               ======================================================")
    print("                      Welcome to The Library Management System")
    print("               ======================================================")
    print()
    print()
title()

def tob():
#for table of books

#sub-title (book index)

    print()
    print ("                                  [BOOK INDEX]")
    dict = BookIndex.bDex()
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
tob()


#main class
def main():

    print()
    print("[INSTRUCTIONS]:")
    print()
    print("Please Enter '1' to Borrow a Book.")
    print("Please Enter '2' to Return the Book.")
    print("Please Enter '3' to Exit.")
    print()
    print("[WARNING]: Any other Value will be considered 'Invalid'.")
    print()

    #exception handling

    #when user input valid input
    try:
        a = int(input("Please Enter a Value: "))    #asking for value

        #when user inputs '1' (Borrow) 
        if(a == 1):
            Borrow.borrowBook()
            main()      #restarting after borrow

        #when user inputs '2' (Reutrn)    
        elif(a == 2):
            Return.returnBook()
            main()      #restarting after return

        #when user inputs '3' (Exit)     
        elif(a == 3):
            import time
            print(" ********** Thank you for using The Library Management System **********")
            time.sleep(2)       #time delay before exiting 
            
            
        #for invalid input (but int only)
        else:
            print("       ----- [INVALID INPUT] ----- ")
            print("Please Enter Value According to the Instructions.")
            main()      #for restarting program after invalid input

    #when user inputs invalid input (not int i.e., string or any other)        
    except ValueError:
        print("       ----- [INVALID INPUT] ----- ")
        print("Kindly follow the Instructions.")
        main()      #for restarting program after invalid input

main()
