from tkinter import *

root=Tk()
root.geometry("800x400")
def getdata():
	print("First name is: %s"%(fname.get()))
	print("Last name is: %s"%(lname.get()))

	print("Gender is: %s" %(var.get()))
	

Label(text="First Name: ", font="comissansms 20 bold italic").grid(row=0,column=0)
Label(text="Last Name: ",font="comissansms 20 bold italic").grid(row=1,column=0)

fname=StringVar()
lname=StringVar()
Entry(root,textvariable=fname).grid(row=0,column=1)
Entry(root,textvariable=lname).grid(row=1,column=1)
Label(text="Skills: ", font="comissansms 20 bold italic").grid(row=2,column=0)
Checkbutton(text="PickandRole").grid(row=2,column=1)
Checkbutton(text="Shooting").grid(row=2,column=2)
Checkbutton(text="Ball_Handling").grid(row=2,column=3)
Checkbutton(text="Intellegence Quotient(IQ)").grid(row=2,column=4)


var=IntVar
Label(text="Gender: ", font="comissansms 20 bold italic").grid(row=3,column=0)
Radiobutton(text="Male",variable=var,value=1).grid(row=3,column=1)
Radiobutton(text="Female",variable=var,value=2).grid(row=3,column=2)
Radiobutton(text="Others",variable=var,value=3).grid(row=3,column=3)

Button(text="Submit",command=getdata).grid(row=6,column=0)

root.mainloop()
