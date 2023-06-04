from tkinter import *
from tkcalendar import Calendar, DateEntry

def get_data():
    print("First Name is :%s" % fname.get())
    print("Middle Name is :%s" % mname.get())
    print("Last Name is :%s" % lname.get())
    print("Order-Item Name is :%s" % oitem.get())
    print("Total Amount is :%d" % total.get())
    print("Contact Number is :%d" % cont.get())
    print("Email Address is :%s" % email.get())
    print("Receiving Address is :%s" % addr.get())

root = Tk()
root.geometry("900x800")

# Title Label
Label(text="ONLINE ORDER FORM", font="comissansms 25 bold").grid(row=0, column=1)

# First Name
Label(text="First Name:", font="comissansms 15 bold italic").grid(row=1, column=0, sticky=E)
fname = StringVar()
Entry(root, textvariable=fname, font="calibre 9 normal").grid(row=1, column=1, pady=5)

# Middle Name
Label(text="Middle Name:", font="comissansms 15 bold").grid(row=2, column=0, sticky=E)
mname = StringVar()
Entry(root, textvariable=mname, font="calibre 9 normal").grid(row=2, column=1, pady=5)

# Last Name
Label(text="Last Name:", font="comissansms 15 bold").grid(row=3, column=0, sticky=E)
lname = StringVar()
Entry(root, textvariable=lname, font="calibre 9 normal").grid(row=3, column=1, pady=5)

# Gender
Label(text="Gender", font="comissansms 15 bold").grid(row=4, column=0, sticky=E)
var = IntVar()
Radiobutton(text="Male", variable=var, value=0).grid(row=4, column=1, sticky=W)
Radiobutton(text="Female", variable=var, value=1).grid(row=4, column=2, sticky=W)
Radiobutton(text="Others", variable=var, value=2).grid(row=4, column=3, sticky=W)

# Order Item
Label(text="Order Item:", font="comissansms 15 bold").grid(row=5, column=0, sticky=E)
oitem = StringVar()
Entry(root, textvariable=oitem, font="calibre 9 normal").grid(row=5, column=1, pady=5)

# Total Amount
Label(text="Total Amount:", font="comissansms 15 bold").grid(row=6, column=0, sticky=E)
total = IntVar()
Entry(root, textvariable=total, font="calibre 9 normal").grid(row=6, column=1, pady=5)

# Contact
Label(text="Contact:", font="comissansms 15 bold").grid(row=7, column=0, sticky=E)
cont = IntVar()
Entry(root, textvariable=cont, font="calibre 9 normal").grid(row=7, column=1, pady=5)

# Email Address
Label(text="Email Address:", font="comissansms 15 bold").grid(row=8, column=0, sticky=E)
email = StringVar()
Entry(root, textvariable=email, font="calibre 9 normal").grid(row=8,column=1, pady=5)
root.mainloop()
