import socket
from tkinter import *
from tkinter import messagebox
import time
start=time.time()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def port_scan():
	if s.connect((ip,port)):
		print(port,"is open on: ",ip)
	else:
		print(port,"is closed on: ",ip)
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("Menu Driven Sample Program for scanning IP and ports:\n\t1.Direct Scanning\n\t2.Entering IP ans Port\n\t3.Port Range\n\t4.Terminate\n")
ch=int(input("Select from above options:"))

while True:
	match(ch):
		case 1:
			print("Selected Direct Scanning")
			IP=socket.gethostbyname('www.facebook.com')
			port=20
			result=s.connect_ex((IP,port))
			if result == 0:
				print("Port {} is open".format(port))
			print(end-start)
		
		case 2:
			print("Enter IP and ports")
		case 3:
			print("Terminating...... :(")
			break
		case _:
			print("Invalid input !! only valid input are executed :)")
		


