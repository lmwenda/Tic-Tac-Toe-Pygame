from tkinter import *
from tkinter import messagebox
import pygame

root = Tk()
root.title("Tic Tac Toe")
root.iconbitmap()


print("[CONNECTED] The User has joined Tic Tac Toe.")

# Progression Bar
loading = ttk.Progressbar(orient=horizontal, length=50, mode=determinate, maximum=200,  

# Label on the Top of the Screen (Title)
title = Label(root, sticky=N).grid(row=5, column=5).pack()


# UI for Tic Tac Toe
Entry(root).grid(sticky=center, row=5, column=5).pack()
Entry(root).grid()


# Menu
'''
menubar = Menu(menubar)
menubar.add_cascade(root, text="File")
'''

# AI
def AI():
    pass

# Player
def player():
    pass


loop = mainloop()
