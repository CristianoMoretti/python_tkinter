from tkinter import *

root = Tk()

def clickMe():
    myLabel = Label(root, text = "Look! You clicked me!")
    myLabel.pack()

myButton = Button(root, text = "Click me!", padx=50, pady=50, fg="blue", bg="#34de66", command=clickMe)
myButton.pack()
root.mainloop()

