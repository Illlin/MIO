import tkinter
from tkinter import messagebox
root = tkinter.Tk()
root.wm_withdraw()

def popup(message, title="INFO"):
    messagebox.showinfo(title, message)
    root.update()

