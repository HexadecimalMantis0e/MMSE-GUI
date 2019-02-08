import Tkinter as tk
import tkFileDialog
import os
import struct
import argparse

def Kill(offset,name):
    f.seek(offset, os.SEEK_SET)
    if args.revive == True:
        print name, "is alive"
        return f.write(struct.pack("b", 0x00))
    else:
        print name, "is dead"
        return f.write(struct.pack("b", 0x01))

def End(root):
    print "Closing"
    f.close()
    root.destroy()

class MMSE_GUI:
    def __init__(self, window):
        self.window = window
        window.title("MMSE-GUI")
        image0 = tk.PhotoImage(file="res/bumbmem.gif")
        self.bumbmem = tk.Button(window, width=125, height=62, image=image0, command=lambda: Kill(0x1E, "BUMBMEM"))
        self.bumbmem.image = image0
        self.bumbmem.grid(row=0, column=1)
        self.bumbmemlabel = tk.Label(window, text="BUMBMEM")
        self.bumbmemlabel.grid(row=1, column=1)
        image1 = tk.PhotoImage(file="res/glutzmem.gif")
        self.glutzmem = tk.Button(window, width=125, height=62, image=image1, command=lambda: Kill(0x22, "GLUTZMEM"))
        self.glutzmem.image = image1
        self.glutzmem.grid(row=0, column=2)
        self.glutzmemlabel = tk.Label(window, text="GLUTZMEM")
        self.glutzmemlabel.grid(row=1, column=2)
        image2 = tk.PhotoImage(file="res/kutmem.gif")
        self.kutmem = tk.Button(window, width=125, height=62, image=image2, command=lambda: Kill(0x26, "KUTMEM"))
        self.kutmem.image = image2
        self.kutmem.grid(row=0, column=3)
        self.kutmemlabel = tk.Label(window, text="KUTMEM")
        self.kutmemlabel.grid(row=1, column=3)
        image3 = tk.PhotoImage(file="res/leckmem.gif")
        self.leckmem = tk.Button(window, width=125, height=62, image=image3, command=lambda: Kill(0x2A, "LECKMEM"))
        self.leckmem.image = image3
        self.leckmem.grid(row=2, column=1)
        self.leckmemlabel = tk.Label(window, text="LECKMEM")
        self.leckmemlabel.grid(row=3, column=1)
        image4 = tk.PhotoImage(file="res/icmem.gif")
        self.icmem = tk.Button(window, width=125, height=62, image=image4, command=lambda: Kill(0x2E, "ICMEM"))
        self.icmem.image = image4
        self.icmem.grid(row=2, column=2)
        self.icmemlabel = tk.Label(window, text="ICMEM")
        self.icmemlabel.grid(row=3, column=2)
        image5 = tk.PhotoImage(file="res/farmem.gif")
        self.farmem = tk.Button(window, width=125, height=62, image=image5, command=lambda: Kill(0x32, "FARMEM"))
        self.farmem.image = image5
        self.farmem.grid(row=2, column=3)
        self.farmemlabel = tk.Label(window, text="FARMEM")
        self.farmemlabel.grid(row=3, column=3)
        self.quit = tk.Button(window, text='QUIT', width=5, command=lambda: End(root))
        self.quit.grid(row=4, column=2)
root = tk.Tk()
root.resizable(0, 0)

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--revive", action="store_true", help="Revive ROBAT MESTRZ")
args = parser.parse_args()
if args.revive == True:
    print "Revive mode enabled"
    
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
