import tkinter as tk

root = tk.Tk()


# create a fuction to do something
def myClick():
    myLabel = tk.Label(root, text="Look I clicked the Button!")
    myLabel.pack()


# create a button with px size of 50 x 50 and a tex, fg=foreground color
myButton = tk.Button(root, text="Don't click it!", fg="red", bg="blue",
                     padx=50, pady=50, command=myClick)

myButton.pack()

root.mainloop()
