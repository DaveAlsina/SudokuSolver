#letrasProposicionales = ['p', 'q', 'r','s', 'y']

def complemento(letra):
    if len(letra) == 1:
        complemento = '-' + letra
        return complemento

    elif (len(letra) > 1):
        if (letra[0] == '-'):
            return letra[1]

    else:
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

    if [] in S:
        return "Insatisfacible", {}
    elif len(S) == 0:
        return "Satisfacible", I

    else:

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

        conj2, interp2 = DPLL(S2,I2)

        if (conj2 == "Satisfacible") and (interp2 == I2):
            return conj2, interp2


        for x in S:
            for p in x:
                if p not in I.keys():
                    l = p
                    break
        Comple = complemento(l)
        S3 = [x for x in S if Comple not in x]
        count = 0

        for c in S3:
            if l in c:
                c = [x for x in c if x != l]
                S3[count] = c
            count += 1
        count = 0

        I3 = I
        if len(l)==1:
            I3[l] = 0
        else:
            I3[l[1]] = 1
        return DPLL(S3, I3)

