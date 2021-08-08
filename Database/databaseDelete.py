from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

root = Tk()
root.title('Message Box')
root.iconbitmap('E:/images/global.ico')

#Databases

# Create a databases or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

'''
# Create table
c.execute(""" CREATE TABLE addresses(
      first_name text,
      last_name text,
      address text,
      city text,
      state text,
      zipcode integer
) """)
'''

# Creating a function to delete a record

def delete():
    # create database
    conn = sqlite3.connect('address_book.db')

    #create cursor
    c = conn.cursor()

    #delete a record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
    print('Deleted Successfully')

    # query of the database
    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()
    # print(records)

    # Loop through the results
    print_record = ''
    for record in records:
        # str(record[6]) added for displaying the id
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=11, column=0, columnspan=2)

    conn.commit()

    conn.close()







# Create submit button for databases

def submit():
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zipcode.get()
    })
    # showinfo messagebox
    messagebox.showinfo("Adresses", "Inserted Successfully")

    conn.commit()

    conn.close()

    # clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)



def query():
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # query of the database
    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()
   # print(records)

    # Loop through the results
    print_record=''
    for record in records:
        #str(record[6]) added for displaying the id
        print_record += str(record[0]) + ' ' + str(record[1]) + ' '+ '\t' + str(record[6]) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=11, column=0, columnspan=2)


    conn.commit()
    conn.close()




# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create textbox labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10,0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)


zipcode_label = Label(root, text="Zip Code")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Delete ID")
delete_box_label.grid(row=9, column=0, pady=5)


# Create submit button

submit_btn = Button(root, text="Add Records", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create query button

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# Create a delete button
delete_btn = Button(root, text="Delete", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx =10, ipadx=120)



# commit change
conn.commit()

# close connection
conn.close()





mainloop()

