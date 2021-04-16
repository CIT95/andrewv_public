from tkinter import *
from typing import Match
import re
root = Tk()
root.title("Simple Calculator")
e = Entry(root, borderwidth=5, width=20, font=("Helvetica", 24))
e.grid(row=0, column=0, columnspan=4)
ans = ""
lastExpression = ""
lastNumber = ""
operatorRx = re.compile(r'^[+-/*]{1}$')
numberRX = re.compile(r'([0-9]+([.][0-9]*)?|[.][0-9]+)')


def get_last_command():
    global lastExpression
    aPos = lastExpression.rfind("+")
    sPos = lastExpression.rfind("-")
    dPos = lastExpression.rfind("/")
    mPos = lastExpression.rfind("*")
    if lastExpression.rfind("**") == mPos - 1:
        mPos -= 1
    index = max(aPos, sPos, mPos, dPos)
    return "+0" if index == -1 else lastExpression[index:]


def button_click(number):
    global lastNumber, ans
    if operatorRx.search(number):
        if not len(e.get()) and number != "-":
            return
        elif len(lastNumber):
            input = e.get()
            input = input[:-len(lastNumber)]
            lastNumber = lastNumber.lstrip("0")
            input += lastNumber
            lastNumber = ""
            e.delete(0, END)
            e.insert(0, input)
    else:
        lastNumber += number
    if ans == e.get() and number.isdigit():
        e.delete(0, END)
        ans = ""
    e.insert(END, number)


def square():
    global lastNumber
    if len(e.get()):
        if len(lastNumber):
            e.insert(END, "**2")
        elif numberRX.search(e.get()):
            e.insert(END, "**2")


def squareRoot():
    global lastNumber
    if len(e.get()):
        e.insert(END, "**.5")


def clear():
    global display
    display = ""
    e.delete(0, END)


def equal():
    global ans, lastExpression, lastNumber
    if not len(e.get()):
        return
    if ans == e.get():
        lastCMD = get_last_command()
        total = "{:g}".format(eval(ans + lastCMD))
    else:
        lastExpression = e.get()
        total = "{:g}".format(eval(e.get()))
    ans = total
    lastNumber = ""
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
button_dot = Button(
    root, text=".", width=5, height=4, command=lambda: button_click("."))
button_add = Button(
    root, text="+", width=5, height=4, command=lambda: button_click("+"))
button_subtract = Button(
    root, text="-", width=5, height=4, command=lambda: button_click("-"))
button_multiply = Button(
    root, text="*", width=5, height=4, command=lambda: button_click("*"))
button_divide = Button(
    root, text="/", width=5, height=4, command=lambda: button_click("/"))
button_equal = Button(
    root, text="=", width=14, height=4, command=equal)
button_clear = Button(
    root, text="Clear", width=5, height=4, command=clear)
button_square = Button(
    root, text="^2", width=5, height=4, command=square)
button_sqrt = Button(
    root, text="sqrt", width=5, height=4,command=squareRoot)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=1)
button_dot.grid(row=5, column=0)

button_clear.grid(row=1, column=2)
button_equal.grid(row=5, column=2, columnspan=2)

button_divide.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_add.grid(row=4, column=3)
button_square.grid(row=1, column=1)
button_sqrt.grid(row=1, column=0)
root.mainloop()
