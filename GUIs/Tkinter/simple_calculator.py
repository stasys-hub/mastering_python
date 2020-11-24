import tkinter as tk

# define main window
root = tk.Tk()
root.title("Simple Calculator")

# define Field to Enter Calculations
myEntry = tk.Entry(root, width=20, borderwidth=5)
myEntry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)


def button_click(number):
    myEntry.delete(0, 20)
    myEntry.insert(0, number)


# define buttons - numbers
button_1 = tk.Button(root, text="1", padx=40, pady=15, command=lambda: button_click(0))
button_2 = tk.Button(root, text="2", padx=40, pady=15, command=lambda: button_click(1))
button_3 = tk.Button(root, text="3", padx=40, pady=15, command=lambda: button_click(2))
button_4 = tk.Button(root, text="4", padx=40, pady=15, command=lambda: button_click(3))
button_5 = tk.Button(root, text="5", padx=40, pady=15, command=lambda: button_click(4))
button_6 = tk.Button(root, text="6", padx=40, pady=15, command=lambda: button_click(5))
button_7 = tk.Button(root, text="7", padx=40, pady=15, command=lambda: button_click(6))
button_8 = tk.Button(root, text="8", padx=40, pady=15, command=lambda: button_click(7))
button_9 = tk.Button(root, text="9", padx=40, pady=15, command=lambda: button_click(8))
button_0 = tk.Button(root, text="0", padx=40, pady=15, command=lambda: button_click(9))

# define buttons - operators
button_add = tk.Button(root, text="+", padx=39, pady=15)
button_mult = tk.Button(root, text="*", padx=39, pady=15)
button_div = tk.Button(root, text="/", padx=39, pady=15)
button_minus = tk.Button(root, text="-", padx=39, pady=15)
button_clear = tk.Button(root, text="clear", padx=22, pady=15)
button_equal = tk.Button(root, text="=", padx=41, pady=15)

# Get buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=1)

button_add.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_clear.grid(row=4, column=3)
button_equal.grid(row=3, column=3)
button_mult.grid(row=4, column=0)
button_div.grid(row=4, column=2)

root.mainloop()
