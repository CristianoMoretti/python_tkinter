from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Learn To Code at codemy.com")
root.iconbitmap('C:/temp/python/tkinter_tutorials/tutorials/t8_images/icon2.ico')

frame = LabelFrame(root, text="This is my frame...    xx")

def open(): 
    root.filename = filedialog.askopenfilename(initialdir = "C:/", title = "select a file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_label = Label(root, text = root.filename).pack()

    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image)
    my_image_label.pack()

my_btn = Button(root, text = "Open File", command = open).pack()

root.mainloop()

