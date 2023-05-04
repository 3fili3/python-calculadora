from tkinter import *

window = Tk()

bg_primary = "#17202A"
bg_primary_ligth = "#566573"
bg_secondary = "#8E44AD"
bg_white = "white"

numberOne = IntVar()
numberTwo = IntVar()

window.resizable(False, False)
window.eval('tk::PlaceWindow . center')
window.title("Bienvenido | Calculadora")
window.geometry("350x600")
window.configure(background=bg_primary)

labelOne = Label(window, text="Calculadora de Numeros", font= "Arial", justify="center", bg=bg_primary, fg=bg_white)
labelOne.place(y=50, x=75)

inputOne = Entry(
    window, bg=bg_primary_ligth, fg=bg_white, width=25, 
    border=0, font="Arial", justify="center", textvariable=numberOne
)
inputOne.place(y=75, x=75)

inputTwo = Entry(
    window, bg=bg_primary_ligth, fg=bg_white, width=25, 
    border=0, font="Arial", justify="center", textvariable=numberTwo
)

inputTwo.place(y=100, x=75)

buttonSum = Button(window, bg=bg_secondary, fg=bg_white, width=23, border=0, font="Arial", text="Sumar Numeros")
buttonSum.place(y=135, x=70)

window.mainloop()