# Andrey Alexandrov, CYBR 410 (Database Security)
# January 22, 2022
# Purpose:
# This program allows users to query a database for existing documents
# (certain fields), insert one document, find the new document in 
# the database, delete it using the delete_one method, and display the results.

# Import MongoClient
from pymongo import MongoClient

# Create a variable named "url" and assign it the connection string
# value copied from MongoDB Atlas
url = "mongodb+srv://admin:admin@cluster0.zmze1.mongodb.net/pytech?retryWrites=true&w=majority"

# Create a variable named "client" and call the MongoClient passing-in
# the "url" variable
client = MongoClient(url)

# Create a variable named "db" and assign it to the pytech database instance
db = client.pytech

# Access the "students" collection
students = db.students

# Create the "docs" variable, find all the students in the "students"
# collection, and assign them to the "docs" variable
docs = db.students.find({})

# Print a message
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --\n")

# A for loop through "docs" that prints student_id, first_name, and last_name
# from each document in the collection. Student IDs in my database are integers.
# They are converted to strings for the purposes of concatenation.
for doc in docs:
     print("Student ID: " + str(doc["student_id"]) + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")

# Create a new document with student_id 1010 and assign it to variable "Maria"
Maria = {
   "student_id": 1010,
   "first_name": "Maria",
   "last_name": "Martinez",
   "enrollments": [
                {
                    "term": 1,
                    "gpa": 4.0,
                    "start_date": "December 1, 2019",
                    "end_date": "March 1, 2020",
                    "courses": [
                        {
                            "course_id": 1,
                            "description": "Math",
                            "instructor": "Helen Lindt",
                             "grade": "A"
                        },
                        {
                            "course_id": 2,
                            "description": "English",
                            "instructor": "Samuel Jackson",
                            "grade": "A"
                        }
                    ]
                },
                {
                    "term": 2,
                    "gpa": 4.0,
                    "start_date": "March 8, 2020",
                    "end_date": "May 31, 2020",
                    "courses": [
                         {
                            "course_id": 3,
                            "description": "Biology",
                            "instructor": "Tom Little",
                             "grade": "A"
                        },
                        {
                            "course_id": 4,
                            "description": "Geography",
                            "instructor": "July Green",
                            "grade": "A"
                         }
                    ]
                }
    ]
}

# Print a message
print("\n-- INSERT STATEMENT --")

# A statements that inserts the above document into the database
maria_student_id = students.insert_one(Maria).inserted_id

# Print the relevant confirmation of the execution of the above command with an
# ObjectID converted to a string for the purposes of concatenation
print("\nInserted a student record into the students collection with document_id " + str(maria_student_id))

# Print a message
print("\n-- DISPLAYING STUDENT TEST DOC --\n")

# Create a variable named "a_student", find the document with the 1010 student_id,
# and assign it to the "a_student" variable
a_student = students.find_one({"student_id": 1010})

# Print the student_id, first_name, and last_name from the document with the
# 1010 student_id. Student IDs in my database are integers. They are converted to
# strings for the purposes of concatenation.
print("Student ID: " + str(a_student["student_id"]) + "\nFirst Name: " + a_student["first_name"] + "\nLast Name: " + a_student["last_name"])

# Call the delete_one() method by student_id 1010 in order to delete the said
# studnet record
db.students.delete_one({"student_id": 1010})

# Fnd all the students in the "students" collection, and re-assign them to the
# "docs" variable created earlier
docs = db.students.find({})

# Print a message
print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --\n")

# A for loop through "docs" that prints student_id, first_name, and last_name
# from each document in the collection. Student IDs in my database are integers.
# They are converted to strings for the purposes of concatenation.
for doc in docs:
     print("Student ID: " + str(doc["student_id"]) + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")

# Print an end-of-program message
print("\n\nEnd of program, press any key to continue...")