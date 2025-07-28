import sqlite3

# connecting to sqlite
connection = sqlite3.connect('Student.db')

# create a cursor object to execute SQL commands
cursor = connection.cursor()

#create a table
table_info = """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25), ROLL_NO INT, MARKS INT);
"""

cursor.execute(table_info)

# insert data into the table
cursor.execute("INSERT INTO STUDENT VALUES('John Doe', '10th', 'A', 1, 85)")
cursor.execute("INSERT INTO STUDENT VALUES('Jane Smith', '10th', 'B', 2, 90)")  
cursor.execute("INSERT INTO STUDENT VALUES('Alice Brown', '9th', 'A', 3, 88)")
cursor.execute("INSERT INTO STUDENT VALUES('Bob White', '9th', 'B', 4, 92)")

# display all the recors
print("All records in STUDENT table:")

data = cursor.execute("SELECT * from STUDENT")

for row in data:
    print(row)
    
# close the connection
connection.commit()
connection.close()


