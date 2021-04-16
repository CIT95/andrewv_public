from tkinter import *
from typing import Match
root = Tk()
root.title("Simple Calculator")
e = Entry(root, borderwidth=5, width=20, font=("Helvetica", 24))
e.grid(row=0, column=0, columnspan=4)


def button_click(number):
    e.insert(END, number)


def clear():
    global input
    input = ""
    e.delete(0, END)


def equal():
    total = "{:g}".format(eval(e.get()))
    e.delete(0, END)
    e.insert(0, total)


button_1 = Button(
    root, text=1, width=5, height=4, command=lambda: button_click("1"))
button_2 = Button(
    root, text=2, width=5, height=4, command=lambda: button_click("2"))
button_3 = Button(
    root, text=3, width=5, height=4, command=lambda: button_click("3"))
button_4 = Button(
    root, text=4, width=5, height=4, command=lambda: button_click("4"))
button_5 = Button(
    root, text=5, width=5, height=4, command=lambda: button_click("5"))
button_6 = Button(
    root, text=6, width=5, height=4, command=lambda: button_click("6"))
button_7 = Button(
    root, text=7, width=5, height=4, command=lambda: button_click("7"))
button_8 = Button(
    root, text=8, width=5, height=4, command=lambda: button_click("8"))
button_9 = Button(
    root, text=9, width=5, height=4, command=lambda: button_click("9"))
button_0 = Button(
    root, text=0, width=5, height=4, command=lambda: button_click("0"))
button_add = Button(
    root, text="+", width=5, height=4, command=lambda: button_click("+"))
button_subtract = Button(
    root, text="-", width=5, height=4, command=lambda: button_click("-"))
button_multiply = Button(
    root, text="*", width=5, height=4, command=lambda: button_click("*"))
button_divide = Button(
    root, text="/", width=5, height=4, command=lambda: button_click("/"))
button_equal = Button(
    root, text="=", width=5, height=4, command=equal)
button_clear = Button(
    root, text="Clear", width=5, height=4, command=clear)

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
button_clear.grid(row=4, column=0)
button_add.grid(row=4, column=3)
button_equal.grid(row=4, column=2)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)

root.mainloop()
