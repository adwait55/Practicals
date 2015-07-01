from Tkinter import *
master = Tk() #to solve StringVar() problem, this has to be at the beginning
v = StringVar()
b = StringVar()

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
   e1.delete(0,END)
   e2.delete(0,END)

def check():
	if(e1.get() == e2.get()):
		print("WOW")
	

Label(master, text="Enter here:").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master, textvariable=v)
e2 = Entry(master)
e1.insert(10,"Miller")
e2.insert(10,"Jill")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Show', command=check).grid(row=3, column=2, sticky=W, pady=4)

mainloop( )
