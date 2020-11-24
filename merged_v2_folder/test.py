class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def String2Tree(A):
    #letrasProposicionales=[chr(x) for x in range(256, 1000)]
    letrasProposicionales=['p','q','r','s','t']
    Conectivos = ['O','Y','>','=']
    Pila = []
    for c in A:
        if c in letrasProposicionales:
            Pila.append(Tree(c,None,None))
        elif c=='-':
            FormulaAux = Tree(c,None,Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
        elif c in Conectivos:
            FormulaAux = Tree(c,Pila[-1],Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)
        else:
            print(u"Hay un problema: el símbolo " + str(c)+ " no se reconoce")
    return Pila[-1]

def enFNC(A):
    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = "-"+q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): ama me da amsiedad!')

    return B

# Algoritmo de transformacion de Tseitin
# Input: A (cadena) en notacion inorder
# Output: B (cadena), Tseitin
def Tseitin(A, letrasProposicionalesA, letrasProposicionalesB):

    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"

    letrasProposicionales = letrasProposicionalesA + letrasProposicionalesB

    l = [] #lista de conjuciones
    pila = [] #pila
    i = -1  #contador de variables nuevas
    s = A[0] #simbolo de trabajp

    while(len(A) > 0):
        if ((s in letrasProposicionales) and (len(pila) != 0) and (pila[-1] == '-')):
            i -=- 1
            atomo = letrasProposicionalesB[i]
            pila = pila[:-1]
            pila.append(atomo)
            l.append(atomo + "=" + "-" + s)
            A = A[1:]

            if (len(A) > 0):
                s = A[0]

        elif (s == ')'):
            w = pila[-1]
            u = pila[-2]
            v = pila[-3]
            pila = pila[:len(pila)-4]
            i -=- 1
            atomo = letrasProposicionalesB[i]
            l.append(atomo + "=" + '(' + v + u + w + ')')
            s = atomo

        else:
            pila.append(s)
            A = A[1:]

            if (len(A) > 0):
                s = A[0]

    B= ''

    if (i < 0):
        atomo = pila[-1]

    else:
        atomo = letrasProposicionalesB[i]

    for x in l:
        y = enFNC(x)
        B += "Y" + y

    B = atomo + B

    return B

letrasProposicionalesa=['p','q','r','s','t']
letrasProposicionalesb=['a','b','c','d','e']
formula = "(Ŀ=(-(ĻO(įOī))Y(-(ĻO(ķOĳ))Y-(įO(ğOď))))"
string = "pqYs="
tree = String2Tree(string)
print(tree)
inorder = Inorder(tree)
print(inorder)
tseitin = Tseitin(inorder, letrasProposicionalesa, letrasProposicionalesb)
print(tseitin)
