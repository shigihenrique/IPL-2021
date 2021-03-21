#Henrique Shigihara
#IPL-2021
#Problema 1.4.1: Cálculo Polinomial 1) Derivadas

poly = [0, 0, 1/2]
out = []

if poly != []:
    for i in range(len(poly)):
        if i > 0:
            res = poly[i] * (i+1)
            res = int(res)
            out.append(res)
else:
    out = None

print(out)
