from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
e.pack()
e.insert(0, "Enter your name: ")


def clickMe():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

myButton = Button(root, text = "Enter your name!", padx=50, pady=50, fg="blue", bg="#34de66", command=clickMe)
myButton.pack()
root.mainloop()

