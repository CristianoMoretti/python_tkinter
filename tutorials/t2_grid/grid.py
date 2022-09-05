from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = "Look! I clicked a button!")
    myLabel.pack()



# we can changr the size with padx and pady
myButton = Button(root, text = "Click me!", padx=50, pady=50, command = myClick, fg="blue", bg="#fff55f")
myButton.pack()


root.mainloop()

