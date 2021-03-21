#Henrique Shigihara
#IPL-2021
#Problema 1.5: Festa de Pizza

size = 'small'
toppings = ['presunto', 'abacaxi']

total = 0
taxa_extra = False

if size == 'small':
    total += 14
elif size == 'medium':
    total += 16
elif size == 'large':
    total += 18

for i in range(len(toppings)):
    n = i 
    m = len(toppings[i]) 
    formula = 12 + n + m
    add = total * (formula / 100)
    total += add
    if toppings[i] == 'bacon' or toppings[i] == 'anchovas':
        taxa_extra = True
           
if taxa_extra == True:
    total *= 1.1

out = round(total, 2)

print(out)
