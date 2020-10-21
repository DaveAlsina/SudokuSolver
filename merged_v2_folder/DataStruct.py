class SudokuDataStruct():
    def __init__(self, size):
        self.size  = size
        self.data, self.letters = self.datastruct()

    def datastruct(self):
        nums = [n for n in range(self.size)]
        self.No = len(nums)
        datastrc = {}
        letras = []

        for n in nums:
            for i in range(self.size):         #codificación para las coordenadas (x,y)
                for j in range(self.size):
                    coordCode = self.codifica(i,j,self.size, self.size)          #codifica una coordenada (x,y) en un numero código
                    """charCoordCode = chr( coordCode + 256 ) #codifíca en numero código coordenada en una letra"""
                    numCode = self.codifica( coordCode, n, self.size**2, len(nums) )
                    charNumCode = chr( numCode + 256 )

                    #tupla de número y estado en tablero
                    #inicializado a falso por defecto
                    datastrc[charNumCode] = False
                    letras.append(charNumCode)

        return datastrc , letras

    def clearData(self):
        for i in list(self.data.keys()):
            self.data[i] = False

    def codifica(self, f, c, Nf, Nc):
        # Funcion que codifica la fila f y columna c
        assert((f >= 0) and (f <= Nf - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(self.size) - 1  + "\nSe recibio " + str(f)
        assert((c >= 0) and (c <= Nc - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(self.size - 1)  + "\nSe recibio " + str(c)
        n = Nc * f + c
        # print(u'Número a codificar:', n)
        return n

    def decodifica(self, n, Nf, Nc): #n es un numero
        # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla
        assert((n >= 0) and (n <= Nf * Nc - 1)), 'Codigo incorrecto! Debe estar entre 0 y' + str(self.size * self.size - 1) + "\nSe recibio " + str(n)
        f = int(n / Nc)
        c = n % Nc
        return f, c

    def decodificaLetra(self,letra):
        a,num = self.decodifica(ord(letra)-256, self.size**2 , self.No)
        x,y = self.decodifica(a , self.size , self.size)

        return ((x,y), num)

    def valueWrite(self , x , y , num = -1):

        if num == -1 :
            for i in range(self.No):
                coordinatesCode = self.codifica(x, y, self.size, self.size)
                numCode = self.codifica( coordinatesCode, i , self.size**2 , self.No)

                for j in list(self.data.keys()):
                    if j == chr(numCode+256):
                        self.data[j] = False

        else:
            coordinatesCode = self.codifica(x, y, self.size, self.size)
            numCode = self.codifica( coordinatesCode, num , self.size**2 , self.No)

            for j in list(self.data.keys()):
                if j == chr(numCode+256):
                    self.data[j] = True

    def solve(self):
        lst = []
        for i in self.data:
            if self.data[i]== True:
                (x,y),num = self.decodificaLetra(i)
                lst.append(((x,y),num))

        return lst
