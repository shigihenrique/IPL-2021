#Henrique Shigihara
#IPL-2021
#Problema 0.1.2: Distâncias, Parte 2: Ponto a Linha

px = 1
py = 2
a = 3
b = 4
c = 5

numerador = a * px + b * py + c
denominador = (a**2 + b**2)**0.5
out = numerador/abs(denominador)

print(out)
