from tkinter import *

root = Tk()
root.geometry("8000x7000")
root.minsize(1000, 200)
root.maxsize(10000, 300)
root.title("Hello")

a = Label(text="THE SEXIEST MAN ALIVE", bg="green", fg="yellow", font="Verdana 50 bold italic underline")
b = Label(text="NIHANGCHHA", bg="blue", fg="white", font="Verdana 50 bold italic underline")

a.pack(anchor="w")
b.pack(anchor="w")

root.mainloop()
