import Tkinter as tk
import os
import struct
import Tkinter, Tkconstants, tkFileDialog

def Kill(offset,name):
    f.seek(offset, os.SEEK_SET)
    print name, "is dead."
    return f.write(struct.pack('b', 0x09))

def End(root):
    print "Closing"
    f.close()
    root.destroy()

class MMSE_GUI:
    def __init__(self, window):
        self.window = window
        window.title('MMSE')
        window.geometry("500x318")
        image0 = tk.PhotoImage(file="res/bumbmem.gif")
        self.bumbmem = tk.Button(window, width=125, height=62, image=image0, command=lambda: Kill(0x1e, "BUMBMEM"))
        self.bumbmem.image = image0
        self.bumbmem.place(x=8)
        image1 = tk.PhotoImage(file="res/glutzmem.gif")
        self.glutzmem = tk.Button(window, width=125, height=62, image=image1, command=lambda: Kill(0x22, "GLUTZMEM"))
        self.glutzmem.image = image1
        self.glutzmem.place(x=360)
        image2 = tk.PhotoImage(file="res/kutmem.gif")
        self.kutmem = tk.Button(window, width=125, height=62, image=image2, command=lambda: Kill(0x26, "KUTMEM"))
        self.kutmem.image = image2
        self.kutmem.place(x=8, y=125)
        image3 = tk.PhotoImage(file="res/leckmem.gif")
        self.leckmem = tk.Button(window, width=125, height=62, image=image3, command=lambda: Kill(0x2A, "LECKMEM"))
        self.leckmem.image = image3
        self.leckmem.place(x=360, y=125)
        image4 = tk.PhotoImage(file="res/icmem.gif")
        self.icmem = tk.Button(window, width=125, height=62, image=image4, command=lambda: Kill(0x2E, "ICMEM"))
        self.icmem.image = image4
        self.icmem.place(x=8, y=250)
        image5 = tk.PhotoImage(file="res/farmem.gif")
        self.farmem = tk.Button(window, width=125, height=62, image=image5, command=lambda: Kill(0x32, "FARMEM"))
        self.farmem.image = image5
        self.farmem.place(x=360, y=250)
        self.quit = tk.Button(window, text='QUIT', width=25, command=lambda: End(root))
        self.quit.place(x=158,y=145)
root = tk.Tk()
name = tkFileDialog.askopenfilename(filetypes = (("Meegah Mem Save", "*.arr"),("All Files","*.*")), title = "Choose a file.")
gui = MMSE_GUI(root)

f = open(name,"r+b")
magic = f.read(0x09)
if magic != "CNC ARRAY":
    raise ValueError("Incorrect header")
f.seek(0x00, os.SEEK_END)
size = f.tell()
if size != 0x36:
    raise ValueError("Incorrect save size")

root.mainloop()
