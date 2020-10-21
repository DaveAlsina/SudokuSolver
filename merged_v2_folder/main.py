import GUI_v2 as gui
import DataStruct as dt


root = gui.Tk()
begin = gui.StartWindows(root)
root.mainloop()

if(begin.size != -1):

    rootGame = gui.Tk()
    rootGame.title("Sudoku solver {0}x{0}".format(int(gui.sqrt(begin.size))))
    data = dt.SudokuDataStruct(begin.size)
    for i in range(data.No):
        for j in range(data.No):	
            data.valueWrite(i,j,0)

    game = gui.Sudoku(rootGame,data,begin.size)

    rootGame.mainloop()
"""Nunca usen tk"""
