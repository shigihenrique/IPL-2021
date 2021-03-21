#Henrique Shigihara
#IPL-2021
#Problema 3.1: Codificação Run Length

def run_length_encode_2d(array):
    lista = []
    #Unificar a lista:
    for i in range(len(array)):
        for j in array[i]:
            lista.append(j)

    repeat = 0
    lista_final = []
    atual = lista[0]
    size = len(lista)
    plus = 0
    ap = False
    for i in range(size):
        if i > 0 and ap == True:
            plus = 1
        if atual == lista[i]:
            repeat += 1
        else:
            add = (repeat + plus, atual)
            lista_final.append(add)
            atual = lista[i]
            repeat = 0
            ap = True

        if i == size - 1:
            add = (repeat + plus, atual)
            lista_final.append(add)

    return lista_final
