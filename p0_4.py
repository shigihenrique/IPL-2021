#Henrique Shigihara
#IPL-2021
#Problema 0.4: Algoritmo de Zeller

year = 2021
month = 2  # 1 = janeiro, 2 = fevereiro, ..., 12 = dezembro
day = 2

y = year
m = month
d = day

if m == 1 or m == 2:
    y1 = y - 1
    m1 = m + 12
else:
    y1 = y
    m1 = m

y2 = y1 % 100

c = y1 / 100

w = (d + (13 * (m1 + 1)//5) + y2 + (y2//4) + (c//4) - 2 * c) % 7
out = round(w)

print(out)
