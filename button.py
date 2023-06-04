from tkinter import *

nihang=Tk()
Button(text='ON').pack(anchor="w")
Button(text='OFF',command=quit).pack(anchor="w")
Label(text='Volume').pack()
Button(text="+").pack()
Button(text="-").pack()

nihang.mainloop()


