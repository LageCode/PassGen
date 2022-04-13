#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Module(s) de la librairie par défaut de Python
#....

#Module(s) de Pypi
import tkinter as tk

#Module(s) de l'application
import const
import class_

BGCOL = const.COLOR_BACKGROUND

def printPassword(pwd_len_entry : tk.Entry, gen_code : list[tk.IntVar], output_entry : tk.Entry) -> None:
    
    pwd_len = getIntFromEntry(pwd_len_entry)
    if pwd_len:
        pwd_object = class_.Password(pwd_len, cryptGenCode(gen_code))
        pwd_object.printPassword(output_entry)
    

def cryptGenCode(gen_code : list[tk.IntVar]) -> int:
    return int("".join(str(b.get()) for b in gen_code), 2)

def getIntFromEntry(entry) -> int or None:
    result = entry.get()
    if result.isdigit() and int(result) > 3:
        return int(result)
    else:
        print("error")
        return None

# Création de la fenêtre
win = tk.Tk()

# Paramétrage de la fenêtre
win.title(const.WIN_TITLE)
win.geometry(const.WIN_DIM)
win.resizable(False, False)
win.iconbitmap(const.WIN_ICON_PATH)
win.config(background=const.COLOR_BACKGROUND)

# Initialisation des variables
gen_code = []

for _ in range(4):
    option = tk.IntVar()
    option.set(1)
    option.get()
    gen_code.append(option)

# Création des frames princiaples
frame = tk.Frame(win, bg=BGCOL)

top_frame = tk.Frame(frame, bg=BGCOL, height=60)
btm_frame = tk.Frame(frame, bg=BGCOL, height=420, bd=30)

# Création des éléments
title = tk.Label(top_frame, text="Password Generator", font=("Consolas", 20))
title.pack(expand=True)

btn_frame = tk.Frame(btm_frame, width=150, height=200, bg=BGCOL)

for name in const.CHECK_BUTTON_NAME_LIST:
    tk.Checkbutton(btn_frame, state=tk.ACTIVE, text="Lettres " + name if name.startswith("m") else name, variable=gen_code[const.CHECK_BUTTON_NAME_LIST.index(name)]).pack(pady=5, side=tk.TOP, anchor=tk.W)

btn_frame.pack()

len_frame = tk.Frame(btm_frame, width=200, height=50, bg=BGCOL)

len_label = tk.Label(len_frame, text="Nbr de caractères", font=("Consolas", 8))
len_label.pack(side=tk.LEFT)

len_entry = tk.Entry(len_frame, width=5)
len_entry.pack(side=tk.LEFT)

len_frame.pack(pady=30)

pwd_frame = tk.Frame(btm_frame, width=200, height=50, bg=BGCOL)

pwd_entry = tk.Entry(pwd_frame, width=200)
pwd_entry.pack(side=tk.TOP)

pwd_button = tk.Button(pwd_frame, width=28, text="Générer", font=("Consolas", 10), command=lambda:printPassword(len_entry, gen_code, pwd_entry))
pwd_button.pack(side=tk.BOTTOM)

pwd_frame.pack_propagate(False)
pwd_frame.pack(pady=20)

top_frame.pack(fill=tk.BOTH, expand=True)
top_frame.pack_propagate(False)
btm_frame.pack(fill=tk.BOTH, expand=True)
btm_frame.pack_propagate(False)
btm_frame.pack(fill=tk.BOTH, expand=True)
btm_frame.pack_propagate(False)

frame.pack(fill=tk.BOTH, expand=True)

win.mainloop()
