import GUI_v2 as gui
import DataStruct as dt
from dpll import *
import json


root = gui.Tk()
begin = gui.StartWindows(root)
root.mainloop()

if(begin.size != -1):

	with open('regla_fila.json', 'r') as file:
	    regla_fila = json.load(file)
	with open('regla_columna.json', 'r') as file:
	    regla_columna = json.load(file)
	with open('regla_region.json', 'r') as file:
	    regla_region = json.load(file)
	with open('regla_celda.json', 'r') as file:
	    regla_celda = json.load(file)

	regla = regla_celda + regla_region + regla_columna + regla_fila
	#regla = regla_columna + regla_celda
	#regla= regla_region
	#regla = regla_fila
	#regla = regla_celda

	rootGame = gui.Tk()
	rootGame.title("Sudoku solver {0}x{0}".format(int(gui.sqrt(begin.size))))
	data = dt.SudokuDataStruct(begin.size,regla)

#	for i in range(data.No):
#		for j in range(data.No):
#			data.valueWrite(i,j,2)

	game = gui.Sudoku(rootGame,data,begin.size)

#	regla ,data.data = dpll(regla ,data.data)
#	print(data.data)

	rootGame.mainloop()

#	print(data.coordenadasColumna(1))
#	print(data.coordenadasFila(1))
#	data.rules()


"""Nunca usen tk"""
