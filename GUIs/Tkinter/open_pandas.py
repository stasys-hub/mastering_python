import tkinter as tk
import pandas as pd #/home/leto/COVID-19

root = tk.Tk()

# create a filed to enter text in
e = tk.Entry(root, width=50, borderwidth=5)
e.pack()
# get the text.entered
e.get()


# create a fuction to do something -> get input
def myClick():
    df = pd.read_csv(e.get())
    myLabel = tk.Label(root, text="read in Data:\n{}".format(df.head()))
    myLabel.pack()


# create a button with px size of 50 x 50 and a tex, fg=foreground color
myButton = tk.Button(root, text="enter Path to csv",
                     padx=50, pady=50, command=myClick)

myButton.pack()

root.mainloop()
