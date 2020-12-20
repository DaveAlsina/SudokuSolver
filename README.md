# SudokuSolver
----------------------------

_Soluciona el sudoku planteado en la interfaz de usuario_ (propia de este módulo 'SudokuSolver') 
usando **lógica proposicional**, transformación de **'Tseitin'** y el algoritmo **'DPLL'**.

# Modo de uso: 
----------------------------

Escriba en la terminal según el tamaño del Sudoku que va a resolver: 

			$	python3 guardar_reglas_3x3.py 
o escriba:

			$	python3 guardar_reglas_2x2.py

Posteriormente ejecute: 

			$	python3 main.py

Seleccione el tamaño del sudoku, rellénelo y oprima **'solve'**, si existe solución la interfaz mostratrá en 
_verde_  **'Satisfiable'** y rellenará el recuadro de sudoku, de lo contrario pondrá en _rojo_ **'Unsatisfiable'**. 

Por cada ejecución recuerde oprimir _'clear all'_, si se producen errores, pare la ejecución con 'CNTRL + C' 
y reincie el programa.
