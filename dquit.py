from tkinter import *
from tkinter import messagebox
root=Tk()
def exit():
	root.destroy()
def wc():
	messagebox.showinfo("HEllo papapapi pu", "Angela godz")
root.geometry("700x300")

Button(text="ON").pack()
Button(text="EXIT",command=exit).pack(anchor="center")
Button(root,text="I",command=wc).pack()
root.mainloop()
