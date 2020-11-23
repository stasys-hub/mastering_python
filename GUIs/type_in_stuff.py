import tkinter as tk

root = tk.Tk()

# create a filed to enter text in
e = tk.Entry(root, width=50, borderwidth=5)
e.pack()
# get the text.entered
e.get()
e.insert(0, "Enter your Namehere !")


# create a fuction to do something -> get input
def myClick():
    myLabel = tk.Label(root, text=e.get())
    myLabel.pack()


# create a button with px size of 50 x 50 and a tex, fg=foreground color
myButton = tk.Button(root, text="Enter your name and press the button",
                     padx=50, pady=50, command=myClick)

myButton.pack()

root.mainloop()
