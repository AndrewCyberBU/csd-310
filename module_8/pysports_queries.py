# Andrey Alexandrov
# February 5, 2022
# CYBR 410 (Database Security)
# Module 8.3 Assignment
# 
# Purpose:
# This program connects to MySQL (with the 'pysports' database) on localhost
# and displays team and player records

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
# the SQL SELECT/FROM statement with column and table names as argument
cursor.execute("SELECT team_id, team_name, mascot FROM team")

# Call the fetchall() method that returns all of the rows from the result set
# (OverIQ.com, 2020) and assign the result to the 'teams' variable
teams = cursor.fetchall()

# Print a message
print("\n-- DISPLAYING TEAM RECORDS --\n")

# A 'for' loop that iterates over the cursor and displays the results
for team in teams:
    print("Team ID: {}".format(team[0])   + "\n" +
          "Team Name: {}".format(team[1]) + "\n" +
          "Mascot: {}".format(team[2])    + "\n")
    
# Use the execute() method to execute the query (OverIQ.com, 2020) and pass
# the SQL SELECT/FROM statement with column and table names as argument
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

# Call the fetchall() method that returns all of the rows from the result set
# and assign the result to the 'players' variable
players = cursor.fetchall()

# Print a message
print("-- DISPLAYING PLAYER RECORDS --\n")

# A 'for' loop that iterates over the cursor and displays the results
for player in players:
    print("Player ID: {}".format(player[0])  + "\n" +
          "First Name: {}".format(player[1]) + "\n" +
          "Last Name: {}".format(player[2])  + "\n" +
          "Team ID: {}".format(player[3])    + "\n")

# Print a final message
print("\nPress any key to continue...\n")

# Disconnect the database using the 'close' method
db.close()
    
# Reference:
# OverIQ.com. (July 27, 2020). Executing Queries using Connector/Python.
# OverIQ.com. Retrieved February 4, 2022, at
# https://overiq.com/mysql-connector-python-101/executing-queries-using-connector-python/


