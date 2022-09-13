"""En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción 
que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al 
principio.

Al principio no tiene que haber una opción seleccionada."""

import random
import tkinter
from tkinter import ttk
window = tkinter.Tk()


window.columnconfigure(0, weight = 1)
window.columnconfigure(0, weight = 3)
def reinicio(event):
    main()
def main():
    seleccionado = tkinter.StringVar() #crea un grupo de radio buttons con la opcion de rellenar solo un epacio
    r1 = ttk.Radiobutton(window, text = "Hombre", value = "1", variable = seleccionado)
    r2 = ttk.Radiobutton(window, text = "Mujer", value = "2", variable = seleccionado)
    r3 = ttk.Radiobutton(window, text = "Otros", value = "3", variable = seleccionado)
    r1.grid(column = 0, row = 1, padx = 5, pady = 5)
    r2.grid(column = 0, row = 2, padx = 5, pady = 5)
    r3.grid(column = 0, row = 3, padx = 5, pady = 5)

    # botom
    rein_button = ttk.Button(window, text = "refrescar")
    rein_button.grid(column = 1, row = 2, sticky = tkinter.E, padx = 5, pady = 5)
    rein_button.bind("<Button-1>", reinicio)

    window.mainloop()

main()
