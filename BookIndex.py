
'''Module for BookList'''

def bDex():#short for book index

    
    #reading the txt file
    file = open("books.txt","r")

    #creating dictionary
    dictionary ={}

    #for bookID
    bookID = 1
    for line in file:
        line = line.replace("\n","")
        dictionary[bookID] = line.split(",")
        bookID = bookID + 1
    file.close()
        
    return dictionary


