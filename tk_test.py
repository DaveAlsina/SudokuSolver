from tkinter import * 
from math import sqrt

size=0

def sudokuNxN(ventana2,sz):
    ventana2.destroy()
    size = sz
    ventana3=Tk()
    ventana3.title("Sudoku solver 3000")
    ventana3.geometry("400x400")
    label2=Label(text="Your Sudoku is:",font=("Agency FB", 20)).place(x=60, y=140)
    label2=Label(text="{0} X {1}".format(int(sqrt(size)),int(sqrt(size))),font=("Agency FB", 20)).place(x=60, y=180)
    botonSig1=Button(ventana3, text="ok",command=ventana3.destroy,font=("Agency FB", 20)).place(x=60, y=300) 
    
def New_window():
    ventana.destroy()
    ventana2=Tk()
    ventana2.title("Sudoku solver 3000")
    ventana2.geometry("400x400")
    labelQuestion1=Label(text= "What sudoku size do you want?",font=("Agency FB", 20)).place(x=60, y=140)
    botonSig1=Button(ventana2, text="2 x 2",command=lambda x= (ventana2): sudokuNxN(ventana2,2*2),font=("Agency FB", 20)).place(x=70, y=300)
    botonSig1=Button(ventana2, text="3 x 3",command=lambda x= (ventana2): sudokuNxN(ventana2,3*3),font=("Agency FB", 20)).place(x=150, y=300)
    botonSig1=Button(ventana2, text="4 x 4",command=lambda x= (ventana2): sudokuNxN(ventana2,4*4),font=("Agency FB", 20)).place(x=230, y=300)
    ventana2.mainloop()

ventana=Tk()
ventana.title("Sudoku solver 3000")
ventana.geometry("400x400")
labelWelcome=Label(text= "WELCOME TO SUDOKU SOLVER 3000",font=("Agency FB", 20)).place(x=60, y=140)

botonSig1=Button(ventana, text="Next",command=New_window,font=("Agency FB", 20)).place(x=60, y=300)

ventana.mainloop()


#sudoku=PhotoImage(file="sudoku.png")
#fondo=Label(ventana,image=sudoku).place(x=15,y=15)