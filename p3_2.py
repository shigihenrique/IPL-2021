#Henrique Shigihara
#IPL-2021
#Problema 3.2: Troca de Chave de Dicionário

def swap(d, k1, k2):
    temp = d[k1]
    d[k1] = d[k2]
    d[k2] = temp
