from tkinter import scrolledtext
from tkinter import *
import socket
import threading

# Functions


def scanSinglePort(port, target):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def startScanning():
    global scroller, targetHost
    message = None
    for port in range(1, 1024):
        portIsOpen = scanSinglePort(port, targetHost)

        if (portIsOpen):
            message = "Port {} is open".format(port) + "\n"
        else:
            message = "Port {} is closed".format(port) + "\n"
        addToScroller(message)


def addToScroller(message):
    global scroller
    scroller.insert(INSERT, message)


def handleButton():
    x = threading.Thread(target=startScanning, args=())
    x.start()


# Main

targetHost = "127.0.0.1"

window = Tk()
window.title("MM Network Tool")
window.geometry('600x600')

scroller = scrolledtext.ScrolledText(window, width=40, height=10)
scroller.grid(column=0, row=0)

startButton = Button(window, text="Start Scanning", command=handleButton)
startButton.grid(column=1, row=0)

window.mainloop()
