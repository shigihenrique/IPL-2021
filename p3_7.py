#Henrique Shigihara
#IPL-2021
#Problema 3.7: Hailstones

def hailstone_sequence(a_0):
    a = a_0
    
    lista = []
    lista.append(a)

    while a != 1:
        if a % 2 == 0:
            a = a/2
            lista.append(a)
        else:
            a = 3*a + 1
            lista.append(a)
    return lista
