# Andrey Alexandrov
# March 5, 2022
# CYBR 410 (Database Security)
# Final Assignment: WhatABook
# 
# Purpose:
# This program is a simple bookstore app developed in accordance with
# WhatABook Requirements

# Import MySQL connector module
import mysql.connector
# Import the sys module (for the purposes of using the exit() function)
import sys
# Import the numpy module (for the purposes of converting tuples)
import numpy as np

# Define connection parameters and assign them to the 'config' variable
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# Establish a connection using the 'connect' method and pass the
# above connection parameters to this method
db = mysql.connector.connect(**config)

# Create the 'cursor' object using the cursor() method.  
cursor = db.cursor()


# The show_menu function
def show_menu():
    # Print messages
    print('\nMain Menu:')
    print('[l] View Books') 
    print('[2] View Store Locations')
    print('[3] My Account')
    print('[4] Exit Program')
    
    # A try-except block    
    try:
        # Take user input  
        option = int(input('Enter your option: '))
                
        # A while loop that checks if user input is in the range 1-4
        while option not in range(1, 5):
            # Print a message
            print('Invalid option')
            # Take user input
            option = int(input('Enter your option: '))
        
        # If - elif statements that direct the flow of control in accordance with user input
        if option == 1:
            # Call the show_books function
            show_books()
        elif option == 2:
            # Call the show_locations function
            show_locations()
        elif option == 3:
            # Call the validate_user function
            validate_user()
        elif option == 4:
            # Print a message
            print('\nThank you for using our app. Goodbye!\n')
            # Call the exit function of the sys module
            sys.exit()

        # Return option
        return option
    
    # An except statement
    except ValueError:
        # Print a message
        print("\nInvalid input. Exiting the program.\n")
        # Call the exit function of the sys module
        sys.exit(0)


# The show_books function    
def show_books():
    # Call the execute() method and pass an SQL statement as argument 
    cursor.execute("SELECT book_id, book_name, author, details FROM book\
                    ORDER BY book_id")
    # Call the fetchall() method that returns all of the rows from the result set
    # and assign the result to the 'books' variable
    books = cursor.fetchall()
    # A 'for' loop that iterates over the cursor and displays the results
    for book in books:
        # Print the output returned by the above SQL statement
        print("\nBook ID: {}".format(book[0]) + "\n" +
            "Book Name: {}".format(book[1])  + "\n" +
            "Author: {}".format(book[2])   + "\n" +
            "Details: {}".format(book[3])   + "\n")
    # Call the show_menu function
    show_menu()


# The show_locations function    
def show_locations():
    # Call the execute() method and pass an SQL statement as argument 
    cursor.execute("SELECT store_id, locale FROM store\
                    ORDER BY store_id")
    # Call the fetchall() method and assign the result to the 'stores' variable 
    stores = cursor.fetchall()
    # A 'for' loop that iterates over the cursor and displays the results
    for store in stores:
        # Print the output returned by the above SQL statement
        print("\nStore ID: {}".format(store[0]) + "\n" +
            "Locale: {}".format(store[1])  + "\n")
    # Call the show_menu function
    show_menu()


# The validate_user function        
def validate_user():
    # A try-except block
    try:
        # Take user input, convert it to int, and assign it to the _user_id variable
        _user_id = int(input('\nPlease enter your user ID: '))

        # Call the execute() method and pass an SQL statement as argument 
        cursor.execute("SELECT user_id FROM user")
                    
        # Call the fetchall() method and assign the result to the 'user_ids' variable 
        user_ids = cursor.fetchall()
        
        # Declare variable x (used as a counter in the while loop below)
        x = 0
        
        # A while loop that validates user ID
        while _user_id not in range(1, (len(user_ids)+1)):
            # Print a message
            print('Invalid user ID.')       
            #Increment the counter
            x += 1
            # Print a message
            print('You have ' + str(3-x) + ' attempts left')
            
            # An if statement that exists the program after 3 incorrect attempts
            if x == 3:
                # Print a message
                print('Exiting. Goodbye!')
                # Call the exit method of the sys module
                sys.exit()
        
            # Take user input
            _user_id = int(input('Please enter a valid user ID: '))  
        
        # Call the show_account_menu function        
        show_account_menu(_user_id)
        # Return _user_id
        return _user_id
        
    # An except statement
    except ValueError:
        # Print a message
        print("\nInvalid input. Exiting the program.\n")
        # Call the exit function of the sys module
        sys.exit(0)

# The show_account_menu function           
def show_account_menu(_user_id):
    # Call the execute() method and pass an SQL statement as argument                   
    cursor.execute("SELECT first_name, last_name FROM user\
                    WHERE user_id = %s", (_user_id,))
    
    # Call the fetchall() method and assign the result to the 'username' variable
    username = cursor.fetchall()            
    
    # A 'for' loop that iterates over the cursor and displays the results 
    for name in username:
        # Print the output returned by the above SQL statement
        print("\nWelcome {} ".format(name[0]) + "{}!".format(name[1])  + "\n")
    # Call the account_menu function
    account_menu(_user_id)


# The account_menu function    
def account_menu(_user_id):
    # Print menu options
    print('[l] Wishlist') 
    print('[2] Add Book')
    print('[3] Main Menu')
    
    # A try-except block
    try:    
        # Take user input, convert it to an integer and assign it to the 'option' variable
        option = int(input('Enter your option: '))

        # A while loop that validates user input
        while option not in range(1, 4):
            # Print a message
            print('Invalid option')
            # Take user input
            option = int(input('Enter your option: '))
        
        # An if-elif statement that directs the flow of control in accordance with user input
        if option == 1:
            # Call the show_wishlist function
            show_wishlist(_user_id)
            
        elif option == 2:
            # Call the show_books_to_add function
            show_books_to_add(_user_id)
            
            # A nested try-except block
            try:
                # Take user input
                _book_id = input("Please enter the ID of the book that you'd like to add to your wishlist: ")
                
                # Call the execute() method and pass an SQL statement as argument 
                cursor.execute("SELECT book_id FROM book\
                                WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = %s)", (_user_id,));                             
                # Call the fetchall() method and assign the result to the 'available_books' variable,
                # converting a tuple to an array
                available_books = np.asarray(cursor.fetchall())
                
                # Declare variable x (used as a counter in the while loop below)
                x = 0  
                
                # A while loop that validates user input
                while np.int64(_book_id) not in available_books:
                    # Take user input
                    _book_id = input("Invalid book ID. Please enter a valid book ID: ")
                    # Increment the counter
                    x += 1
                    if x == 3:
                        # Print a message
                        print("A valid book ID has not been entered. Exiting the program. Goodbye.")
                        # Call the exit method of the sys module
                        sys.exit()
                # Call the add_book_to_wishlist function        
                add_book_to_wishlist(_user_id, _book_id)
                
                # Return _book_id
                return _book_id
        
            # An except statement
            except ValueError:
                # Print a message
                print("\nInvalid input. Exiting the program.\n")
                # Call the exit function of the sys module
                sys.exit(0)    
                
        elif option == 3:
            # Call the show_menu function
            show_menu()

        # Return option
        return option
    
    # An except statement
    except ValueError:
        # Print a message
        print("\nInvalid input. Exiting the program.\n")
        # Call the exit function of the sys module
        sys.exit(0)


# The show_wishlist function
def show_wishlist(_user_id):
    # Display current wishlist
    print("\nMy Wishlist:")
    # Call the execute() method and pass an SQL statement as argument 
    cursor.execute("SELECT first_name, last_name, book.book_id, book_name, author, details\
                    FROM user\
                    INNER JOIN wishlist ON user.user_id = wishlist.user_id\
                    AND user.user_id = %s\
                    INNER JOIN book ON book.book_id = wishlist.book_id\
                    AND wishlist.user_id = %s", (_user_id, _user_id))
                    
    # Call the fetchall() method and assign the result to the 'my_wishlist' variable
    my_wishlist = cursor.fetchall()            
    
    # A 'for' loop that iterates over the cursor and displays the results 
    for a_list in my_wishlist:
        # Print the output returned by the above SQL statement
        print("\nUsername: {} ".format(a_list[0]) + "{}".format(a_list[1])  + "\n" +
                "Book ID: {}".format(a_list[2]) + "\n" +
                "Book Name: {}".format(a_list[3])   + "\n" +
                "Author: {}".format(a_list[4])   + "\n" +
                "Details: {}".format(a_list[5]) + "\n")
    # Call the account_menu function
    account_menu(_user_id)


# The show_books_to_add function        
def show_books_to_add(_user_id):
    # Print a message
    print("\nAvailable books:\n")
    # Call the execute() method and pass an SQL statement as argument 
    cursor.execute("SELECT book_id, book_name, author, details\
                    FROM book\
                    WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = %s)", (_user_id,));
                                    
    # Call the fetchall() method and assign the result to the 'available_books' variable
    available_books = cursor.fetchall()            
    
    # A 'for' loop that iterates over the cursor and displays the results
    for book in available_books:
        # Print the output returned by the above SQL statement
        print("Book ID: {}".format(book[0])   + "\n" +
                "Book Name: {}".format(book[1])   + "\n" +
                "Author: {}".format(book[2])   + "\n" +
                "Details: {}".format(book[3])   + "\n")


# The add_book_to_wishlist function    
def add_book_to_wishlist(_user_id, _book_id):

    # Call the execute() method and pass an SQL statement as argument 
    cursor.execute("INSERT INTO wishlist(user_id, book_id)\
                    VALUES(%s, %s)", (_user_id, _book_id))
    # Send a commit statement to the database 
    db.commit()
                                    
    # Display an updated wishlist
    print("\nYou have successfully entered a new record to your wishlist.\n\n\
        Here is your updated wishlist:")
    # Call the show_wishlist function
    show_wishlist(_user_id)

# Print a pattern
print("*********************")
# Print a message
print("Welcome to WhatABook!")
# Print a pattern
print("*********************")

# Call the show_menu function        
show_menu()
    
 

    




