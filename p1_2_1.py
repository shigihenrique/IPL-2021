#Henrique Shigihara
#IPL-2021
#Problema 1.2.1: Médias, Parte 1: Média Aritmética

numbers = []

if numbers == []:
    out = None
else:
    size = len(numbers)
    soma = sum(numbers)
    out = soma / size   
    
print(out)
