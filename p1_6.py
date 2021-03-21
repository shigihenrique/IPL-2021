#Henrique Shigihara
#IPL-2021
#Problema 1.6: A Slice of Pi
    
p_d = 5
cells_square = 0
cells_circle = 0

matriz = [[0 for i in range(p_d)] for j in range(p_d)]

#considerar cada célula da grade
centro = p_d//2

for i in range(p_d):
    for j in range(p_d):
        cells_square += 1
        if i <= centro:
            matriz[i][j] = (i-centro, centro-j)
        elif i > centro:
            matriz[i][j] = ((centro-i) * -1, (j-centro) * -1)

#calcular as distâncias entre as células da grade e a célula central
for j in range(p_d):
    for i in range(p_d):
        xy = [] 
        xy = matriz[i][j]
        x = xy[0]
        y = xy[1]
        
        dist = (x**2+y**2)**0.5
        #usar esse resultado para verificar se a célula em questão está dentro do círculo
        if dist <= p_d / 2:
            cells_circle += 1

#acompanhar quantas células estão no círculo e quantas estão no quadrado
estimate = cells_circle / cells_square

out = estimate * 4
print(out)
