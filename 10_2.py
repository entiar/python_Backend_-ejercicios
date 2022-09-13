"""En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual
debe de contener una lista de elementos seleccionables, también debe de tener 
un label con el texto que queráis."""

import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.columnconfigure(0, weight = 1)
window.columnconfigure(0, weight = 3)

 
pais_label = ttk.Label(window, text = "Paises")
pais_label.grid(column = 0, row = 0, sticky = tkinter.W, padx = 5, pady = 5)

lista = ["Alemania", "España", "África", "Australia", "Dinamarca", "Brazil", "India"]
lista_items =tkinter.StringVar(value = lista)
listbox = tkinter.Listbox(window, height = 100, listvariable = lista_items)
listbox.grid(column = 0, row = 1, sticky = tkinter.W)

window.mainloop()
