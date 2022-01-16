# Andrey Alexandrov, CYBR 410 (Database Security)
# January 16, 2022
# Purpose:
# This program allows users to insert new documents into the
# "pytech" database and print confirmations that the relevant
# documents have been inserted, together with their ObjectIDs.

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

# Student documents with the IDs 1007, 1008, and 1009,
# assigned to the variables Bob, Tom, and Daniel, respectively
Bob = {
   "student_id": 1007,
   "first_name": "Bob",
   "last_name": "Bush",
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

Tom = {
   "student_id": 1008,
   "first_name": "Tom",
   "last_name": "Big",
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

Daniel = {
   "student_id": 1009,
   "first_name": "Daniel",
   "last_name": "Good",
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

# Access the "students" collection
students = db.students

# Print an introductory (explanatory) message
print("-- INSERT STATEMENTS --\n")

# Three statements that insert the above documents and
# print the relevant confirmations with ObjectIDs converted to
# strings for the purposes of concatenation
bob_student_id = students.insert_one(Bob).inserted_id
print("\nInserted student record Bob Bush into the students collection with document_id " + str(bob_student_id))

tom_student_id = students.insert_one(Tom).inserted_id
print("\nInserted student record Tom Big into the students collection with document_id " + str(tom_student_id))

daniel_student_id = students.insert_one(Daniel).inserted_id
print("\nInserted student record Daniel Good into the students collection with document_id " + str(daniel_student_id))

# Print an end-of-program message
print("\n\nEnd of program, press any key to exit...")