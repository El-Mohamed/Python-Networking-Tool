from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import *
import socket
import threading
import re as regex

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
    getTarget()
    message = None
    isValid = checkIP(targetHost)
    if(isValid):
        for port in range(1, 1024):
            portIsOpen = scanSinglePort(port, targetHost)

            if (portIsOpen):
                message = "Port {} is open".format(port) + "\n"
            else:
                message = "Port {} is closed".format(port) + "\n"

            addToScroller(message)
    else:
        messagebox.showinfo('Error', 'IP Is not valid')


def addToScroller(message):
    global scroller
    scroller.insert(INSERT, message)


def handleButton():
    x = threading.Thread(target=startScanning, args=())
    x.start()


def getTarget():
    global textField, targetHost
    targetHost = textField.get()


def checkIP(ipaddres):
    res = regex.search(
        "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ipaddres)
    return res

# Main


targetHost = ""

window = Tk()
window.title("MM Network Tool")
window.geometry('600x600')

label = Label(window, text="Scanner Results")
label.grid(column=0, row=0)

scroller = scrolledtext.ScrolledText(window, width=40, height=10)
scroller.grid(column=0, row=0)

startButton = Button(window, text="Start Scanning", command=handleButton)
startButton.grid(column=1, row=0)

textField = Entry(window, width=10)
textField.grid(column=2, row=0)

window.mainloop()
