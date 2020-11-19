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
regla_polaca = dts.rules()
letrasProposicionalesA = [chr(x) for x in range(256, 1000)] # Modificar de acuerdo a reglas
letrasProposicionalesB = [chr(x) for x in range(1000, 2000)] # Modificar de acuerdo a reglas
guardar_polaca(regla_polaca, 'regla0', letrasProposicionalesA, letrasProposicionalesB)

# regla_polaca = R.regla1()
# letrasProposicionalesB = [chr(x) for x in range(2001, 3000)] # Modificar de acuerdo a reglas
# guardar_polaca(regla_polaca, 'regla1', letrasProposicionalesA, letrasProposicionalesB)

print("Finalizado!")

#############################
# Las reglas se leen con:
# with open('regla0.json', 'r') as file:
#     reglas = json.load(file)
