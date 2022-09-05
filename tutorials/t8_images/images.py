from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn To Code at codemy.com")
root.iconbitmap('C:/temp/python/tkinter_tutorials/tutorials/t8_images/icon2.ico')

# there are 3 steps to add an image
my_img = ImageTk.PhotoImage(Image.open('C:/temp/python/tkinter_tutorials/tutorials/t8_images/icon.png'))
my_label = Label(root, image=my_img)
my_label.pack()

button_quit = Button(root, text = "Exit Program", command = root.quit)
button_quit.pack()

root.mainloop()

