class SudokuDataStruct():
    def __init__(self, size):

      self.size = size
      self.nums = self.createNums(size)
      self.coordinates= self.createCoordinates(size)
      self.atoms ,self.meaning = self.atomsValues(size)

    def createNums(self, size):
      numeros = [ i for i in range(1, size+1) ]   # Crea una lista por comprension con todos los posibles numeros a utilizar en el sudoku

      return numeros                # ejemplo para size=2*2    numeros=[1,2,3,4]

    def createCoordinates(self, size):
      lst = [(j+1,i+1) for j in range(size) for i in range(size)]  # Crea una lista por comprension con todas las tuplas ('coordenadas') de nuestro sudoku
      
      return lst                # ejemplo para size=2*2    lst=[(1,1),(1,2),(1,3),(1,4),(2,1),...,(4,4)]


    def createAtoms(self):
      atoms={xy : False for xy in self.coordinates}   # Crea un diccionario por comprension, basado en las (x,y), inicializado en falso
         
      return atoms                # ejemplo para size=2*2    atoms={(1,1):False,(1,2):False,(1,3):False,(1,4):False,(2,1):False,...,(4,4):False}

    def atomsValues(self, size): 
      a = [chr(x) for x in range(97, 97+size)]
      atoms = {a[i] : self.createAtoms() for i in range(size) }  # crea un diccionario por comprension, basado em las ltras proposicionales y en los diccionarios basados en (x,y)
      meaning = {i+1 : a[i] for i in range(size) }  # crea un diccionario con los significados de las letras proposicionales

      return atoms , meaning    # ejemplo para size=2*2  atoms={a:{(1,1):False,(1,2):False,(1,3):False,(1,4):False,(2,1):False,...,(4,4):False} , ...'analogamente para los demas atomos'} meaning ={1:'a',...,4:'d'} 

    def value (self,coordinate , num=-1):
      for i in range(1,self.size + 1 ):
        self.atoms[self.meaning[i]][coordinate]=False

      if num in self.nums:
        self.atoms[self.meaning[num]][coordinate]=True

    def clear (self):
      for x in range(1,self.size+1):
        for y in range(1,self.size+1):
          for z in range(1,self.size+1):
            self.atoms[self.meaning[z]][(x,y)]=False
