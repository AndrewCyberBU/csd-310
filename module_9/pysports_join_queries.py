# Andrey Alexandrov
# February 12, 2022
# CYBR 410 (Database Security)
# Module 9.2 Assignment
# 
# Purpose:
# This program connects to MySQL (with the 'pysports' database) on localhost
# and queries the database to return certain player and team records using SQL joins

# Import MySQL connector module
import mysql.connector

# Define connection parameters
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# Establish a connection using the 'connect' method and pass the
# above connection parameters to this method
db = mysql.connector.connect(**config)

# Create the 'cursor' object using the cursor() method. The cursor
# object is used to execute queries and retrieve rows (OverIQ.com, 2020)  
cursor = db.cursor()

# Use the execute() method to execute the query (OverIQ.com, 2020) and pass
# a SQL statement as argument
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player\
    INNER JOIN team ON player.team_id = team.team_id")

# Call the fetchall() method that returns all of the rows from the result set
# (OverIQ.com, 2020) and assign the result to the 'players' variable
players = cursor.fetchall()

# Print a message
print("\n-- DISPLAYING PLAYER RECORDS --\n")

# A 'for' loop that iterates over the cursor and displays the results
for player in players:
    print("Player ID: {}".format(player[0])   + "\n" +
          "First Name: {}".format(player[1])  + "\n" +
          "Last Name: {}".format(player[2])   + "\n" +
          "Team Name: {}".format(player[3])   + "\n")
    
# Print a final message
print("\nPress any key to continue...\n")

# Disconnect the database using the 'close' method
db.close()
    
# Reference:
# OverIQ.com. (July 27, 2020). Executing Queries using Connector/Python.
# OverIQ.com. Retrieved February 4, 2022, at
# https://overiq.com/mysql-connector-python-101/executing-queries-using-connector-python/


