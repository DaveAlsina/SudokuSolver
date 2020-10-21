from tkinter import*
from math import sqrt

class Sudoku:
    def __init__(self, root,dic, size,squareDim=35):

        #coordenadas por defecto al inicializar
        self.cordx = 10
        self.cordy = 10

        #clases como atributos
        self.dic = dic

        self.game = root
        self.table = Canvas(root, height= squareDim*size + 20, width=squareDim*size + 20)

        #variables clave para construir la GUI
        self.sz = size               #nxn sudoku (tamaño)
        self.squaredim = squareDim   #ancho y alto del cuadrado
        self.numRange = ""           #string con el rango de números validos
        for i in range(1,size+1):
            self.numRange += str(i)

        #funciones que son corridas una sola vez
        self.createGrid(size, squareDim)      #creacion de la rejilla del juego
        self.table.pack()

        self.solve = Button(root, text = "Solve", command = self.solveSudoku) #boton para solucionar el sudoku
        self.solve.pack()

        self.solve = Button(root, text = "Clear all", command = self.clearCells) #boton de refrescar sudoku
        self.solve.pack()

        #eventos a los que la interfaz está atenta
        self.table.bind('<Button-1>', self.click)                        #click izq
        self.game.bind('<Key>', lambda ev: self.keypressed(ev, "write")) #cualquier tecla
        self.game.bind('<Delete>', lambda ev: self.keypressed(ev, "supr")) #boton de 'supr'
        self.game.bind('<BackSpace>', lambda ev: self.keypressed(ev, "del")) #boton de 'del'


    def createGrid(self, sz, squaredim):

        """estos dos primeros for se encargan de crear la rejilla de filas"""

        for i in range (0, int(sqrt(sz)) + 1): # (int(sqrt(sz)) + 1
            x0 = 10                               #(margen)
            y0 = (10 + squaredim*int(sqrt(sz))*i) #(alto de cuadrado) * (no. cuadrados por subregión) * (iteración) + margen
            x1 = ( squaredim*sz +10 )             #(ancho de cuadrado) * (no. cuadrados por fila) + margen
            y1 = y0                               #(misma posición en y0)

            self.table.create_line( x0, y0, x1, y1, width=2.5)

            if(i!= int(sqrt(sz))):
                for i2 in range(0, int(sqrt(sz))):     # (int(sqrt(sz)) - 1) + 1
                    y2 = squaredim*i2
                    self.table.create_line( x0, y0+y2, x1, y0+y2, width = 1.25)

        """estos dos for se encargan de crear la rejilla de columnas"""

        for i in range (0, int(sqrt(sz)) + 1): # (int(sqrt(sz)) + 1
            x0 = ( 10 + i*squaredim*sqrt(sz) )     # (ancho del cuadrado) * (no. cuadrados por subregión)* (iteración) + margen
            x1 =  x0                           # (misma posicion de x0)
            y0 =  10                           # (margen)
            y1 = (10 + squaredim*sz)              # (alto del cuadrado) * (no. cuadrados por columna) + (margen)

            self.table.create_line( x0, y0, x0, y1, width=2.5)

            if(i!= int(sqrt(sz))):
                for i2 in range(0, int(sqrt(sz))):     # (int(sqrt(sz)) - 1) + 1
                    x2 = squaredim*i2
                    self.table.create_line( x0 + x2, y0, x0 + x2, y1, width = 1.25)

    def click(self, event):

        posx = int( (event.x - 10)/self.squaredim ) + 1 #encuentra el indice(int) en x de la casilla clicada
        posy = int( (event.y - 10)/self.squaredim ) + 1 #encuentra el indice(int) en y de la casilla clicada
        #desde (1,1) hasta (n,n)

        cond1 = ((event.x - 10) > 0) and ((event.y - 10) > 0) #si no está cliclando en los margenes
        cond2 =  (1<= posx <=self.sz) and (1<= posy <=self.sz)  #Si está clicando en una de las casillas del sudoku

        if ( cond1 and cond2 ):
            print("Todo en orden -> ", "casilla: ", "(" , posx , "," , posy ,")")

            #sobreescritura de valores de posiciones 'cordx', 'cordy'
            #lo cual permite tomar entradas de numeros desde el teclado y modificar la interfaz
            self.cordx = posx
            self.cordy = posy
            #ejecuta funcion que marca en rojo la casilla clicada
            self.clickedOnCell()

        else:
            print("click no válido")

    def keypressed(self, event, operation):

        """recibe la <key> input y analiza si es una input válida para el juego o no
           y ejecuta los comandos necesarios en caso de ser una input válida"""

        if (operation=="del" or operation == "supr"):

            """****punto de conexión con la estructura de datos****"""
            self.dic.valueWrite( self.cordx-1, self.cordy -1 )
            print("borrado en  el dict")

            self.writeinGUI("del")

        elif (event.char in self.numRange):

            """****punto de conexión con la estructura de datos****"""
            self.dic.valueWrite(self.cordx-1, self.cordy -1, int(event.char)- 1 )
            print("escritura en el dict en:", "casilla: ", "(" , self.cordx , "," , self.cordy, ")", event.char, operation)

            #ejecuta funcion que marca el numero seleccionado
            self.writeinGUI(event.char)

        else:
            print("por favor ingrese valores válidos")

    def writeinGUI(self,order):

        #busca la coordenada x  y y del punto medio de la celda clicada por última vez
        x = ( 10 + (self.cordx * self.squaredim) - (self.squaredim)/2 )
        y = ( 10 + (self.cordy * self.squaredim) - (self.squaredim)/2 )
        print(int(x/self.squaredim) + 1, int(y/self.squaredim) + 1)

        #identificador del texto que va a ser creado
        tag = str(x) + str(y) #misteriosamente si se cambia el tag todo falla

        if (order == "del"):
            self.table.delete(tag)
        else:
            self.table.delete(tag)
            self.table.create_text( x, y, text=order, tag=tag, fill="black", activefill="blue", font=("Arial", 16) )

    def clickedOnCell(self):

        """funcion que encierra un recuadro cuando es clicado"""
        self.table.delete("cellclicked")

        #coordenadas del recuadro que se va a dibujar
        x1 = 10 + (self.cordx * self.squaredim)
        x0 = 10 + ( (self.cordx - 1) * self.squaredim)
        y1 = 10 + (self.cordy * self.squaredim)
        y0 = 10 + ( (self.cordy - 1) * self.squaredim)

        #dibujo del recuadro que indica click
        self.table.create_rectangle(x0, y0, x1, y1, outline= "blue", tags="cellclicked")

    def solveSudoku(self):
        """****punto de conexión con la estructura de datos****"""
        #[antes de eso necesito una función que me envie una lista de listas con la tupla (x,y) y el numero]
        #[ ((x,y), NUM), ((x,y), NUM)]

        solution = self.dic.solve()

        for numAndCoord in solution:
            coord = numAndCoord[0]
            num = numAndCoord[1] +1

            self.cordx = coord[0] + 1
            self.cordy = coord[1] + 1
            self.writeinGUI(num)


        print("WINTER IS COMMING")

    def clearCells(self):
        """****punto de conexión con la estructura de datos****"""
        for i in range(1, self.sz+1):
            x = ( 10 + (i * self.squaredim) - (self.squaredim)/2 )

            for j in range(1, self.sz+1):

                y = ( 10 + (j * self.squaredim) - (self.squaredim)/2 )
                tag = str(x) + str(y) #misteriosamente si se cambia el tag todo falla
                self.table.delete(tag)
                self.dic.clearData()

class StartWindows():

    def __init__(self, root):
        self.root = root
        self.size = -1
        self.startMenu()

    def startMenu(self):
        self.root.title("Sudoku solver")
        self.root.geometry("300x300")

        Label(self.root, text= "What sudoku size do you want?",font=("Agency FB", 18)).pack()
        Button(self.root, text="2 x 2",command= lambda: self.endStart(4), font=("Agency FB", 18)).pack()
        Button(self.root, text="3 x 3",command= lambda: self.endStart(9), font=("Agency FB", 18)).pack()

    def endStart(self,sz):
        self.size = sz
        self.root.destroy()
