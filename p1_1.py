#Henrique Shigihara
#IPL-2021
#Problema 1.1: Juros compostos

interest_rate = 0
interest = 1 + interest_rate
valor = 1
cont = 0

if interest_rate > 0:
    while valor <= 2:
        valor *= interest
        cont += 1
    out = cont
else:
    out = "NEVER"
    
print(out)
