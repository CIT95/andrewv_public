from tkinter import *

root = Tk()
root.title("dev_2")

frame = Frame(root)
scrollBar = Scrollbar(frame)
messages = Listbox(frame, height=20, width=50, bg='white', yscrollcommand=scrollBar)
scrollBar.pack(side=RIGHT, fill=Y)
messages.pack()
frame.pack()

entryFrame = Frame(root)
input = Entry(entryFrame)
input.grid(row=0, column=0)
send = Button(entryFrame, text='Send')
send.grid(row=0, column=1)
entryFrame.pack()

mainloop()
