import socket
from tkinter import *
from tkinter import scrolledtext
import threading


target = "127.0.0.1"


window = Tk()
window.title("MM Network Tool")
window.geometry('600x600')

scroller = scrolledtext.ScrolledText(window, width=40, height=10)
scroller.grid(column=0, row=0)


def scanport(port):
    global target
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def startScanning():
    global scroller
    message = None
    for port in range(1, 1024):
        result = scanport(port)
        if (result):
            message = "Port {} is open".format(port)

        else:
            message = "Port {} is closed".format(port)

        message += "\n"

        print(message)
        scroller.insert(INSERT, message)


def click():
    x = threading.Thread(target=startScanning, args=())
    x.start()


startButton = Button(window, text="Start Scanning", command=click)
startButton.grid(column=1, row=0)


window.mainloop()
