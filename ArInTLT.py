#+main
disk = "C:\\"
#-main +imports
import os
import sys
import pyautogui
import pymsgbox
import webbrowser as wb
import tkinter as tk
from colorama import Fore, Back, Style, init
init(autoreset=True)
from pymsgbox import *
from time import sleep
from PIL import ImageTk, Image
#-imports +start
window = tk.Tk()
window.title("ArInTLT")
window.geometry("578x968")
window.configure(background='white')
window.overrideredirect(1)
#-start +config
si = disk + "ons.png"
start = ImageTk.PhotoImage(Image.open(si))
os.system('@echo off')
os.system('title ArInTLT')
os.system('chcp 1251')
os.system('cls')
im = tk.Label(window, image = start)
im.pack(side = "bottom", fill = "both", expand = "yes")
#-config
print(Back.WHITE + Fore.RED + "Made by Maple/TerLeTzid (C) TLT 2017-2020")
sleep(1)
with open(disk + 'scenare.scn', encoding="utf-8") as f:
    scd = f.readlines()
    print(scd[1])
    sleep(1)
    print(scd[2])
#+loop
window.mainloop()
input()
#-loop
