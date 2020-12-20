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

	rootGame = gui.Tk()
	rootGame.title("Sudoku solver {0}x{0}".format(int(gui.sqrt(begin.size))))
	data = dt.SudokuDataStruct(begin.size,regla)


	game = gui.Sudoku(rootGame,data,begin.size)


	rootGame.mainloop()



"""Nunca usen tk"""
