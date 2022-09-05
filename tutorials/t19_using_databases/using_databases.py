from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3

root = Tk()
root.title("Learn To Code at codemy.com")
root.iconbitmap('C:/temp/python/tkinter_tutorials/tutorials/t8_images/icon2.ico')
root.geometry("400x400")

# databases
conn = sqlite3.connect('address_book.db')

root.mainloop()

