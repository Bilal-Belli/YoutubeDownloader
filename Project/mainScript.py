import os
import sys
from tkinter import filedialog, ttk
from tkinter import *
import tkinter as tk
from turtle import color, width
from PIL import Image, ImageTk
from tkinter.font import Font
import pytube
from pytube import Playlist
import threading

# Get the directory of the script
script_dir = os.path.dirname(sys.argv[0])

global LaValeur
global URL
global path
LaValeur = ' Video High Quality'  # the default value
path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive\Bureau')
# print("The Desktop path is: " + path)

# Function 1
def fonction1(event):
    global LaValeur
    global URL
    LaValeur = event.widget.get()
    # print(LaValeur)

# Function 2
def download_video():
    global LaValeur
    global URL
    global path
    URL = e1.get()

    if LaValeur == " Video High Quality":
        youtube = pytube.YouTube(URL)
        video = youtube.streams.get_highest_resolution()
        video.download(path)
    elif LaValeur == " Video Low Quality":
        youtube = pytube.YouTube(URL)
        video = youtube.streams.get_lowest_resolution()
        video.download(path)
    elif LaValeur == " PlayList High Quality":
        p = Playlist(URL)
        # print(f'Downloading: {p.title}')
        for video in p.videos:
            # print(video.title)
            st = video.streams.get_highest_resolution()
            st.download(path)
    elif LaValeur == " PlayList Low Quality":
        p = Playlist(URL)
        # print(f'Downloading: {p.title}')
        for video in p.videos:
            # print(video.title)
            st = video.streams.get_lowest_resolution()
            st.download(path)
    elif LaValeur == " Sound":
        youtube = pytube.YouTube(URL)
        sound = youtube.streams.get_audio_only()
        sound.download(path)
    else:
        p = Playlist(URL)
        # print(f'Downloading: {p.title}')
        for video in p.videos:
            # print(video.title)
            st = video.streams.get_audio_only()
            st.download(path)

def fonction2():
    threading.Thread(target=download_video).start()

# Function 3
def fonction3():
    global path
    path = filedialog.askdirectory()
    # print(path)

root = Tk()
root.title('Youtube Downloader')

# Use the complete absolute path to the "logo.ico" file
icon_path = os.path.join(script_dir, 'logo.ico')
root.iconbitmap(icon_path)

# Designate Height and Width of our app
app_width = 550
app_height = 285

# The Height and Width of our pc screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

# label_1
label_1 = Label(root,width="550",height="285",bg="#101820")  # to colorate the space of application
label_1.place(x=0,y=0)
root.resizable(False,False)

# label_2
label_2=Label(root,text="Link",width=15,bg="#006B38", height=1, foreground="#101820",font=('calibre',12, 'bold'))
label_2.grid(column=0,row=0, padx=15, pady=10)

# label_3
label_3 = Label(root, text="Save In",bg="#006B38",width=15, height=1, foreground="#101820", font=('calibre',12, 'bold'))
label_3.grid(column=0,row=1, padx=15, pady=10)

# label_4
label_4 = Label(root, text="Select Option",bg="#006B38",width=15, height=1, foreground="#101820", font=('calibre',12, 'bold'))
label_4.grid(column=0,row=2, padx=15, pady=10)

# label_6
label_6 = Label(root, text="Download Now",bg="#006B38",width=15, height=1, foreground="#101820", font=('calibre',12, 'bold'))
label_6.grid(column=0,row=3, padx=15, pady=10)

# Entry_1 FOR label_2
e1 = tk.Entry(root, fg="#006B38", width=49, font=('calibre',9, 'bold'))
e1.grid(row=0, column=1, padx=0, pady=0)

# Button FOR label_3 Choose PATH
Btnpath = Button(root, fg="#006B38", text="Choose Path", borderwidth=0, width=49, font=('calibre',9, 'bold'), command=fonction3)
Btnpath.grid(row=1, column=1, padx=0, pady=0)

# Combobox
ChoixFonction = ttk.Combobox(root, width=23, state="readonly", foreground="#006B38")

# Down list
ChoixFonction['values'] = (' Video High Quality',
                           ' Video Low Quality',
                           ' PlayList High Quality',
                           ' PlayList Low Quality',
                           ' Sound',
                           ' Sound Playlist')
ChoixFonction.grid(column=1, row=2)
# Movement
ChoixFonction.current(0)
ChoixFonction.bind("<<ComboboxSelected>>", fonction1)

# Button Download
icon_path2 = os.path.join(script_dir, './download.ico')
image = Image.open(icon_path2)
img = image.resize((100, 100))
my_img = ImageTk.PhotoImage(img)
btn = Button(root, image=my_img, borderwidth=0, bg="#101820", command=fonction2)
btn.grid(column=1, row=3, padx=15, pady=10)

# Status Bar
label_5 = Label(root, text="Bilal Belli | ©2022", bg="#101820", foreground="#006B38", font=('calibre',9, 'bold'))
label_5.grid(column=1, row=4, sticky=E)

# Hover Button Module
def hoverActive(boton, color1, color2, color3):
    boton.configure(bg=color1)
    def fuera(e):
        boton.configure(bg=color1)
    def dentro(e):
        boton.configure(bg=color2)
    def activo(e):
        boton.configure(activebackground=color3)
    boton.bind("<Enter>", dentro)
    boton.bind("<Leave>", fuera)
    boton.bind("<ButtonPress-1>", activo)

hoverActive(btn, "#101820", "#006B38", "#ffffff")

root.mainloop()