def createCoordinates(sz=4):
    lst = []
    for i in range(sz):
        for j in range(sz):
            lst.append((i,j))
            
    return lst

def createAtoms(coordinates):
    atoms = {}
    for xy in coordinates: 
        atoms[xy] = False
        
    return atoms

def atomsValues(coordinates, sz=4):
    a = "abcdefghijklmnopqrstiwyxyz"
    atomos = {}
    meaning = {}
        
    for i in range(sz): 
        atomos[ a[i] ] = createAtoms(coordinates)
        meaning[ i+1 ] = a[i]
    
    return atomos, meaning 


coordinates = createCoordinates()
Atomos, meaning = atomsValues(coordinates)
meaning
