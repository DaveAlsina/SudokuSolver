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
dts = R.SudokuDataStruct(4)

regla_polaca_columna = ""
regla_polaca_fila = ""
regla_polaca_region = ""
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
letrasProposicionalesB = [chr(x) for x in range(1000, 2000)] # Modificar de acuerdo a reglas
guardar_polaca(regla_polaca_fila, 'regla_fila', letrasProposicionalesA, letrasProposicionalesB)

letrasProposicionalesB = [chr(x) for x in range(2000, 3000)] # Modificar de acuerdo a reglas
guardar_polaca(regla_polaca_region, 'regla_region', letrasProposicionalesA, letrasProposicionalesB)

letrasProposicionalesB = [chr(x) for x in range(3000, 4000)] # Modificar de acuerdo a reglas
guardar_polaca(regla_polaca_columna, 'regla_columna', letrasProposicionalesA, letrasProposicionalesB)

print("Finalizado!")

#############################
# Las reglas se leen con:
# with open('regla0.json', 'r') as file:
#     reglas = json.load(file)
