from tkinter import *
import sqlite3

root = Tk()
root.title('Database Address Book')
root.iconbitmap('E:/images/global.ico')

#Databases

# Create a databases or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
# Cursor class is an instance using which
# you can invoke methods that execute SQLite statements,
# fetch data from the result sets of the queries.
c = conn.cursor()

# Create table
c.execute(""" CREATE TABLE addresses(
      first_name text,
      last_name text,
      address text,
      city text,
      state text,
      zipcode integer
) """)
print("Table created successfully")

# commit change
conn.commit()

# close connection
conn.close()





mainloop()

