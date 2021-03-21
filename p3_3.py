#Henrique Shigihara
#IPL-2021
#Problema 3.3: Mapeamento de Dicionário

def dictmap(d, f):
    for index, valor in d.items():
        d[index] = f(valor)
