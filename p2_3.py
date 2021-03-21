#Henrique Shigihara
#IPL-2021
#Problema 2.3: Portas

def ndoors(n):
    lista = ['closed' for porta in range(n)]
    lista2 = []

    chave = 1
    while chave < n:
        soma = chave
        for i in range(n):
            if lista[soma-1] == 'closed':
                lista[soma-1] = 'open'
            elif lista[soma-1] == 'open':
                lista[soma-1] = 'closed'
            
            soma += chave
            
            if soma > n:
                break
        chave += 1

    if lista[n-1] == 'closed':
        lista[n-1] = 'open'
    elif lista[n-1] == 'open':
        lista[n-1] = 'closed'

    for i in range(n):
        if lista[i] == 'open':
            lista2.append(i+1)
                
    return(lista2)

out = ndoors(100)
print(out)