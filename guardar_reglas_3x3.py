print("Importando paquetes...")
import FNC as F
import DataStruct as R
import json
print("Listo!")

def guardar_polaca(regla_polaca, archivo, letrasProposicionalesA, letrasProposicionalesB):
    print("Creando arbol...")
    regla_arbol = R.String2Tree(regla_polaca)
    print("Creando cadena inorder...")
    regla_inorder = R.Inorder(regla_arbol)
    print("Transformacion de Tseitin...")
    regla_fnc = F.Tseitin(regla_inorder, letrasProposicionalesA, letrasProposicionalesB)
    print("Forma clausal...")
    regla_clausal = F.formaClausal(regla_fnc)
    print(f"Guardando a archivo {archivo}...")
    with open(archivo + '.json', 'w') as outfile:
        json.dump(regla_clausal, outfile)
        #json.dump(regla_inorder, outfile)
    print("Terminado!")

def guardar_inorder(regla_inorder, archivo, letrasProposicionalesA, letrasProposicionalesB):
    print("Transformacion de Tseitin...")
    regla_fnc = F.Tseitin(regla_inorder, letrasProposicionalesA, letrasProposicionalesB)
    print("Forma clausal...")
    regla_clausal = F.formaClausal(regla_fnc)
    print(f"Guardando a archivo {archivo}...")
    with open(archivo + '.json', 'w') as outfile:
        json.dump(regla_clausal, outfile)
    print("Terminado!")

def guardar_fnc(regla_fnc, archivo, letrasProposicionalesA, letrasProposicionalesB):
    print("Forma clausal...")
    regla_clausal = F.formaClausal(regla_fnc)
    print(f"Guardando a archivo {archivo}...")
    with open(archivo + '.json', 'w') as outfile:
        json.dump(regla_clausal, outfile)
    print("Terminado!")

print("Creando reglas...")
dts = R.SudokuDataStruct(9)

regla_polaca_columna = ""
regla_polaca_fila = ""
regla_polaca_region = ""
regla_polaca_celda = dts.cellRule()
initial = True
for i in dts.letters:
    if initial:
        regla_polaca_fila += dts.rowRule(i)
        regla_polaca_region += dts.regionRule(i)
        regla_polaca_columna += dts.columnRule(i)
        initial = False
    else:
        regla_polaca_fila += dts.rowRule(i) + "Y"
        regla_polaca_region += dts.regionRule(i) + "Y"
        regla_polaca_columna += dts.columnRule(i) + "Y"

letrasProposicionalesA = dts.letters # Modificar de acuerdo a reglas
let = len(dts.letters) + 256
letrasProposicionalesB = [chr(x) for x in range(3000 , 7000*3)] # Modificar de acuerdo a reglas
guardar_polaca(regla_polaca_fila, 'regla_fila', letrasProposicionalesA, letrasProposicionalesB)

letrasProposicionalesB = [chr(x) for x in range(7000*3, 11000*3)] # Modificar de acuerdo a reglas
guardar_polaca(regla_polaca_region, 'regla_region', letrasProposicionalesA, letrasProposicionalesB)

letrasProposicionalesB = [chr(x) for x in range(11000*3, 15000*3)] # Modificar de acuerdo a reglas
guardar_polaca(regla_polaca_columna, 'regla_columna', letrasProposicionalesA, letrasProposicionalesB)

letrasProposicionalesB = [chr(x) for x in range(15000*3, 19000*3)] # Modificar de acuerdo a reglas
guardar_polaca(regla_polaca_celda, 'regla_celda', letrasProposicionalesA, letrasProposicionalesB)

print("Finalizado!")

#############################
# Las reglas se leen con:
# with open('regla0.json', 'r') as file:
#     reglas = json.load(file)
