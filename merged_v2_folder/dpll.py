def hay_unidad(S):
	"""Busca las unidades (atomos solos)
	dentro de S. 
	INPUT: -S, conjunto de cláusulas
	OUTPUT: unidad(caracter)/None
	"""
	
	for x in S:
		if len(x) == 1:
			return x[0]

	return None



def ucomplemento(letra):
	"""Genera la letra complemento de 'letra', 
	INPUT: 'letra' (caracteres de la letra proposicional)
	OUTPUT: (caracter) de la letra complemento 
	"""
	if letra in letrasProposicionales:
		complemento = '-' + letra
		return complemento

	elif (letra[0] == '-'):
		return letra[1]

	else:
		raise Exception(f"error, literal invalido {letra}")



def unit_propagate(S, I):
	"""INPUT: -S, conjunto de cláusulas,
		  -I, interpretación parcial
	   OUTPUT: -S, conjunto de cláusulas, 
		   -I, Interpretación parcial
	"""
	
	unidad = hay_unidad(S)

	while ([] not in S) and (unidad != None):

		complemento = ucomplemento(unidad)

		#altera el valor de verdad de la unidad 
		if (unidad in letrasProposicionales):
			I[unidad] = True		
		else: 
			I[complemento] = False

		#añada las sublistas (clausulas) que no contengan la unidad
		#en otras palabras quite las clausulas que contengan la unidad
		S = [c for c in S if unidad not in c]

		partial = []		

		for c in S:
		
			if complemento in c:
				c = [x for x in c if x != complemento]
				partial.append(c)
			else:
				partial.append(c)
			
			
		S = partial
		unidad = hay_unidad(S)

	return S, I


def dpll(S,I):

	S, I = unit_propagate(S,I)	
#	print(S,I)

	if ([] in S):
		return "Insatisfacible", {}

	elif(len(S) == 0):

		return "Satisfacible", I 

	else:
		unidad = ''

		for x in S:
			if len(x) != 0:
				unidad = x[0]

		complemento = ucomplemento(unidad)

		#altera el valor de verdad de la unidad 
		if (unidad in letrasProposicionales):
			I[unidad] = True		
		else: 
			I[complemento] = False

		S = [c for c in S if unidad not in c]
		for c in S:
			if complemento in c:
				c = [x for x in c if x != unidad]
		
		return dpll(S,I)			

letrasProposicionales = ['p', 'q', 'r']
S = [['p', 'q'], ['r'], ['q', '-r']]


#S = [['-p'], ['-q'], ['-r','p','q'], ['r']]
I = {}

for atom in letrasProposicionales:
	I[atom] = False

print(S)
S, I = dpll(S,I)
print(S,I)

