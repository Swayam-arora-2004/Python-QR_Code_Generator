from tkinter import *
from tkinter import messagebox
import pyqrcode

ws=Tk()
ws.title("QR CODE GENERATOR")

def generate_qr():
    if len(user_input.get())!=0:
        global qr,img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data = qr.xbm(scale = 8))
    else:
        messagebox.showwarning("Warning","All Fields are Required !")
    try:
        display_code()
    except:
        pass

def display_code():
    img_lb1.config(image = img)
    output.config(text = "QR Code of " + user_input.get())

lb1 = Label(
    ws,
    text = "Enter URL"
)
lb1.pack()
user_input = StringVar()
entry = Entry(
    ws,
    textvariable = user_input
)
entry.pack(padx = 20)

button = Button(
    ws,
    text = "Generate QR",
    width = 15,
    command = generate_qr
)
button.pack(pady = 20)

img_lb1 = Label(
    ws,
    bg = '#1dacd6'
)
img_lb1.pack()

output = Label(
    ws,
    bg = '#cf3476'
)
output.pack()

ws.mainloop()
