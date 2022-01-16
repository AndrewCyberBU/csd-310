# Andrey Alexandrov, CYBR 410 (Database Security)
# January 16, 2022
# Purpose:
# This program allows users to query a database for
# existing documents. In particular, it returns the
# student_id, first_name, and last_name fields of each
# document, and also returns the same fields from a
# particular document searched for by the user.

# Import MongoClient
from pymongo import MongoClient

# Create a variable named "url" and assign it the
# connection string value copied from MongoDB Atlas
url = "mongodb+srv://admin:admin@cluster0.zmze1.mongodb.net/pytech?retryWrites=true&w=majority"

# Create a variable named "client" and call the
# MongoClient passing-in the "url" variable
client = MongoClient(url)

# Create a variable named "db" and assign it to the
# pytech database instance
db = client.pytech

# Access the "students" collection
students = db.students

# Create the "docs" variable, find all the students in the 
# "students" collection, and assign them to the "docs" 
# variable
docs = db.students.find({})

# Print an introductory (explanatory) message
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --\n")

# A for loop through "docs" that prints student_id, first_name, and
# last_name from each document in the collection. Student IDs in my
# database are integers. They are converted to strings for the
# purposes of concatenation.
for doc in docs:
     print("Student ID: " + str(doc["student_id"]) + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")

# Print the second introductory (explanatory) message
print("\n-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --\n")

# Create a variable named "a_student", find the document with the
# 1008 student_id, and assign it to the "a_student" variable
a_student = students.find_one({"student_id": 1008})

# Print the student_id, first_name, and last_name from the
# document with the 1008 student_id. Student IDs in my database are
# integers. They are converted to strings for the purposes of 
# concatenation.
print("Student ID: " + str(a_student["student_id"]) + "\nFirst Name: " + a_student["first_name"] + "\nLast Name: " + a_student["last_name"])

# Print an end-of-program message
print("\n\nEnd of program, press any key to continue...")