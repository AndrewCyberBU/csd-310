# Andrey Alexandrov
# February 5, 2022
# CYBR 410 (Database Security)
# Module 8.2 Assignment
# 
# Purpose:
# This program connects to MySQL (with the 'pysports' database) on localhost

# Import MySQL connector module
import mysql.connector

# Import MySQL errorcode module that contains all the MySQL-specific
# error codes (OverIQ.com, 2020)
from mysql.connector import errorcode

# Define connection parameters. The raise_on_warnings argument means
# whether to raise an exception on warnings (MySQL, n.d.)
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# Connection test code that sets up a connection with MySQL using the
# parameters assigned to the 'config' variable.
try:
    # Establish a connection using the 'connect' method and pass the
    # above connection parameters to this method
    db = mysql.connector.connect(**config)
    
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"],
          config["host"], config["database"]))
    
    input("\n\n Press any key to continue...")

# Handle connection errors using the mysql.connector.Error class that catches
# any kind of exception (OverIQ.com, 2020)      
except mysql.connector.Error as err:
    
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
        
    else:
        print(err)

# Executing the code regardless of the results of the above exception
# handling blocks
finally:
    # Disconnect the database using the 'close' method
    db.close()
    
# References:
# MySQL. (n.d.). MySQL Connector/Python Developer Guide.
# 7.1 Connector/Python Connection Arguments. MySQL. Retrieved February 4,
# 2022, at https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html

# OverIQ.com. (July 27, 2020). Exception Handling in Connector/Python.
# OverIQ.com. Retrieved February 4, 2022, at 
# https://overiq.com/mysql-connector-python-101/exception-handling-in-connector-python/