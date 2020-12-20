#letrasProposicionales = ['p', 'q', 'r','s', 'y']

def complemento(letra):
    if len(letra) == 1:
        complemento = '-' + letra
        return complemento
    elif (len(letra) > 1):
        if (letra[0] == '-'):
            return letra[1]
    else:
        # print(f"error, literal invalido {letra}")
        raise(f"error, literal invalido {letra}")

def hay_unidad(S):
    for x in S:
        if len(x) == 1:
            return x[0]
    return None

def unit_propagate(S, I):
    unidad = hay_unidad(S)
    while ([] not in S) and (unidad != None):
        Comple = complemento(unidad)
        S = [c for c in S if unidad not in c]
        count = 0
        for c in S:
            if Comple in c:
                c = [x for x in c if x != Comple]
                S[count] = c
            count += 1

        if '-' in unidad:
            I[unidad] = 0
        else:
            I[unidad] = 1
        unidad = hay_unidad(S)
    return S, I

def DPLL(S,I):
    S, I = unit_propagate(S,I)
    # print("S = ", S)
    # print("I = ", I)
    if [] in S:
        return "Insatisfacible", {}
    elif len(S) == 0:
        return "Satisfacible", I

    else:
        # print(I.keys())

        l = S[0][0]
        S2 = [x for x in S if l not in x]
        Comple = complemento(l)
        count = 0
        for c in S2:
            if Comple in c:
                c = [x for x in c if x != Comple]
                S2[count] = c
            count += 1
        count = 0
        # print("S2 = ", S2)
        I2 = I
        if len(l)==1:
            I2[l] = 1
        else:
            I2[l[1]] = 0
        # print("I2 = ", I2)
        conj2, interp2 = DPLL(S2,I2)
        # print("conj2 = ", conj2)
        # print("interp2 = ", interp2)
        if (conj2 == "Satisfacible") and (interp2 == I2):
            # print("Se ejecuta el primer if")
            return conj2, interp2


        # print("No se ejecuta primer if")
        for x in S:
            for p in x:
                if p not in I.keys():
                    l = p
                    break
        Comple = complemento(l)
        # print("l2 = ", l)
        # print("Comple = ", Comple)
        S3 = [x for x in S if Comple not in x]
        # print("S3 antes = ", S3)
        count = 0
        for c in S3:
            if l in c:
                c = [x for x in c if x != l]
                S3[count] = c
            count += 1
        count = 0
        # print("S3 despues = ", S3)
        I3 = I
        if len(l)==1:
            I3[l] = 0
        else:
            I3[l[1]] = 1
        return DPLL(S3, I3)


#
# S1 = [['p', 'q'], ['r'], ['q', '-r']]
# S2 = [['p'], ['-p','q'], ['-q', 'r', 's']]
# S3 = [['p'], ['-p','q','-r'], ['-r', 's'], ['q']]
# S4 = [['p', '-q', 'r'], ['-p','q','-r'], ['-p', '-q', 'r'], ['-p', '-q', '-r']]
# S5 = [['p'], ['-p']]
# SG = [S1,S2,S3,S4,S5]
#
# for i in SG:
#     I = {}
#     print("S = ", i)
#     conjunto, interp = DPLL(i,I)
#     print(conjunto)
#     print(interp)
#     print("")
