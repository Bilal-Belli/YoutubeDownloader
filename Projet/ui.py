from tkinter import ttk
from tkinter import *
import tkinter as tk

root = Tk()
root.title('Codemy.com - Center')
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
my_label = Label(root,width="450",height="250",bg="#370028").place(x=0,y=0)
root.resizable(False,False)


# label
ttk.Label(root, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)
# Combobox creation
n = tk.StringVar()
ChoixFonction = ttk.Combobox(root, width = 27, textvariable = n)
# Adding combobox drop down list
ChoixFonction['values'] = (' Video High Quality',' Video Low Quality',' PlayList High Quality',' PlayList Low Quality',' Sound',' Playlist Sound')  
ChoixFonction.grid(column = 1, row = 5)
ChoixFonction.current()

root.mainloop()

if ChoixFonction.current() ==" Video High Quality": 
    # label text for title
    ttk.Label(window,text="GFG Combobox Widget",background='green',foreground ="white",font=("Times New Roman",15)).grid(row = 0, column = 1)