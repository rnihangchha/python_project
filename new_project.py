import socket
from tkinter import *


root=Tk()
root.geometry("800x450")
def scanner():
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	ip=socket.gethostbyname('www.pornhub.com')
	port=21
	s.connect((ip,port))
	print("successfully connected")

Button(text="Scanner_port",command=scanner).grid(row=10,column=0)


root.mainloop()
