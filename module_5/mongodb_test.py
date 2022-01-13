# Andrey Alexandrov, CYBR 410 (Database Security)
# January 13, 2022
# Purpose:
# This program allows users to connect to the Mongo
# "pytech" database and view the "students" collection

# Import MongoClient
from pymongo import MongoClient

# Create a variable named url and assign it the
# connection string value copied from MongoDB Atlas
url = "mongodb+srv://admin:admin@cluster0.zmze1.mongodb.net/pytech?retryWrites=true&w=majority"

# Create a variable named client and call the
# MongoClient passing-in the url variable
client = MongoClient(url)

# Create a variable named db and assign it to the
# pytech database instance
db = client.pytech

# Call the list_collection_names method off of the
# db variable with the print statement
print("-- Pytech Collection List --\n")
print(db.list_collection_names())

# Print a final message
print("\nEnd of program, press any key to exit...")