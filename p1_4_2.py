#Henrique Shigihara
#IPL-2021
#Problema 1.4.2: Cálculo Polinomial 2) Integrais 

poly = [0, 1, 2, 6]
const = 'c'
out = []

if poly != []:
    out.append(const)
    for i in range(len(poly)):
            res = poly[i] / (i+1)
            out.append(res)
else:
    out = None

print(out)
