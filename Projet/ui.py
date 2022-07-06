from tkinter import ttk
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

global LaValeur
global URL
#Function of call back#####################
def callbackFunc(event):
    LaValeur = event.widget.get()
#################################################
root = Tk()
root.title('My App Youtube')
#root.iconbitmap('c:/gui/codemy.ico')
# Designate Height and Width of our app
app_width = 450
app_height = 250
# The Height and Width of our pc screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
Label(root,width="450",height="250",bg="#370028").place(x=0,y=0)
root.resizable(False,False)
# label
ttk.Label(root, text = "Select the Month :",font = ("Times New Roman", 10)).grid(column = 0,row = 5, padx = 10, pady = 25)
# Combobox creation
n = tk.StringVar()
ChoixFonction = ttk.Combobox(root, width = 27, textvariable = n)
# Adding combobox drop down list
ChoixFonction['values'] = (' Video High Quality',' Video Low Quality',' PlayList High Quality',' PlayList Low Quality',' Sound',' Playlist Sound')  
ChoixFonction.grid(column = 1, row = 5)
ChoixFonction.current()
ChoixFonction.bind("<<ComboboxSelected>>", callbackFunc)
###################################
image=Image.open('./Projet/download.ico')
img=image.resize(( 283, 98))
my_img=ImageTk.PhotoImage(img)
btn = Button(root, image=my_img,borderwidth=0,bg="#370028",command = root.destroy).grid(row=4, column=0, padx=10, pady=20, ipadx=22)

root.mainloop()