from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3

root = Tk()
root.title("Learn To Code at codemy.com")
# root.iconbitmap('C:/temp/python/tkinter_tutorials/tutorials/t8_images/icon2.ico')
root.geometry("400x400")

# databases
conn = sqlite3.connect('./t19_using_databases/address_book.db')

# create a cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE addresses(
    first_name text,
    last_name text, 
    address text, 
    city text,
    state text,
    zipcode integer
)
""")

# Commit changes
conn.commit()

# Close conneciton
conn.close()

root.mainloop()

