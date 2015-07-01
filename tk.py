import Tkinter as tk
from Tkinter import *
master = Tk()
v = StringVar()
b = StringVar()

def refresh():
	import q
	q.d()

def check():
	if(e1.get() == e2.get()):
		w = Label(master, text=" -- CORRECT -- ")
		w.grid(row=4, column=2, sticky=W, pady=4)
	else:
		w = Label(master, text="** WRONG **")
		w.grid(row=4, column=2, sticky=W, pady=4)

#Label(master, text="yo").grid(row=1)

e1 = Entry(master, textvariable=v)
e2 = Entry(master)
e1.insert(10,"Miller")
e2.insert(10,"Enter here")

e1.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Refresh', command=refresh).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Check', command=check).grid(row=3, column=2, sticky=W, pady=4)


a = Label(master, text="Enter the CAPTCHA!")
a.grid(row=0, column=1, sticky=W, pady=4)


mainloop( )
