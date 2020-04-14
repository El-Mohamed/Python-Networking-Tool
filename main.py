import socket
from tkinter import *


target = "127.0.0.1"


def scanport(port):
    global target
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


window = Tk()

window.title("MM Network Tool")

window.geometry('600x600')

window.mainloop()


for port in range(1, 1024):
    result = scanport(port)
    if (result):
        print("Port {} is open".format(port))
    else:
        print("Port {} is closed".format(port))
