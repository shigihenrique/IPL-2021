#Henrique Shigihara
#IPL-2021
#Problema 1.2.2: Médias，Parte 2: Média Geométrica

numbers = []
produto = 1

if numbers == []:
    out = None
else:
    for i in numbers:
        produto *= i
    out = produto**(1/(len(numbers)))

print(out)
