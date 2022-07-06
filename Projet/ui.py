from tkinter import ttk
from tkinter import *
import tkinter as tk
from turtle import color, width
from PIL import Image, ImageTk
from tkinter.font import Font

global LaValeur
global URL
LaValeur =' Video High Quality'#la valeur par defaut

#Function 1           #####################
def fonction1(event):
    LaValeur = event.widget.get()
    print(LaValeur)
###########################################
#Function 2           #####################
def fonction2(event):
    LaValeur = event.widget.get()
###########################################
#Function 3           #####################
def fonction3(event):
    LaValeur = event.widget.get()
###########################################
#Function 4           #####################
def fonction4(event):
    LaValeur = event.widget.get()
###########################################
#Function 5           #####################
def fonction5(event):
    LaValeur = event.widget.get()
###########################################
#Function 6           #####################
def fonction6(event):
    LaValeur = event.widget.get()
###########################################
#Function 7           #####################
def fonction7(event):
    LaValeur = event.widget.get()
###########################################

root = Tk()
root.title('Youtube Downloader')
root.iconbitmap('./Projet/logo.ico')

# Designate Height and Width of our app
app_width = 550
app_height = 300

# The Height and Width of our pc screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

# label_1
label_1 = Label(root,width="550",height="300",bg="#101820")#to colorate the space of application
label_1.place(x=0,y=0)
root.resizable(False,False)

# label_2
label_2=Label(root,text = "Link",width=15,bg="#006B38", height=1, foreground= "#101820",font=('calibre',12, 'bold'))
label_2.grid(column = 0,row = 0, padx = 15, pady = 10)

# label_3
label_3 = Label(root, text = "Save In",bg="#006B38",width=15, height=1, foreground= "#101820", font=('calibre',12, 'bold'))
label_3.grid(column = 0,row = 1, padx = 15, pady = 10)

# label_4
label_4 = Label(root, text = "Select Option",bg="#006B38",width=15, height=1, foreground= "#101820", font=('calibre',12, 'bold'))
label_4.grid(column = 0,row = 2, padx = 15, pady = 10)

# label_6
label_6 = Label(root, text = "Download Now",bg="#006B38",width=15, height=1, foreground= "#101820", font=('calibre',12, 'bold'))
label_6.grid(column = 0,row = 3, padx = 15, pady = 10)

# Entry_1 FOR label_2
e1 = tk.Entry(root, fg= "#006B38", width=49,font=('calibre',9, 'bold'))
e1.grid(row=0, column=1,padx = 0, pady = 0)

# Entry_2 FOR label_3
e2 = tk.Entry(root, fg= "#006B38", width=49,font=('calibre',9, 'bold'))
e2.grid(row=1, column=1,padx = 0, pady = 0)

# Combobox
ChoixFonction = ttk.Combobox(root,width = 23, state="readonly", foreground= "#006B38")

# Down list
ChoixFonction['values'] = (' Video High Quality',
                        ' Video Low Quality',
                        ' PlayList High Quality',
                        ' PlayList Low Quality',
                        ' Sound',
                        ' Sound Playlist')  
ChoixFonction.grid(column = 1, row = 2)
# Movement
ChoixFonction.current(0)
ChoixFonction.bind("<<ComboboxSelected>>",fonction1)

# Button
image=Image.open('./Projet/download.ico')
img=image.resize(( 100, 100))
my_img=ImageTk.PhotoImage(img)
btn = Button(root, image=my_img,borderwidth=0,bg="#101820",command = root.destroy)
btn.grid(column = 1,row =3,padx = 15, pady = 10)

# Status Bar
label_5 = Label(root, text = "Bilal Belli | ©2022",bg="#101820", foreground= "#006B38", font=('calibre',9, 'bold'))
label_5.grid(column = 1,row = 4,sticky=E)


root.mainloop()