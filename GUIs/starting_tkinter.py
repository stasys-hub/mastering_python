from tkinter import *
#import os
root = Tk()


# Creating a label widget with text
myLabel1= Label(root, text = "Hello World!")
myLabel2 = Label(root, text = "My second widget")

# get it on the screen
#myLabel.pack()

# if we have more than one label we need to use a grid:
# and we need to tell tkinter where to put stuff
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 1)



#  now we need an event loop 

root.mainloop()








