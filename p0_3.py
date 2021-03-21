#Henrique Shigihara
#IPL-2021
#Problema 0.3: Conta de Energia 

kwh_used = 1000
cont = 0
valor = 0

#Regras:
#Cada um dos primeiros 500 quilowatts-hora usados custa $0.45 / kWh
#Os próximos 1000 quilowatts-hora usados custam $0.74 / kWh
#Os próximos 1000 quilowatts-hora usados custam $1.25 / kWh
#Cada quilowatt-hora além de 2500 custa $2.00 / kWh

while cont < kwh_used:
    if cont <= 500:
        valor += 0.45
        cont += 1
    if 500 < cont <= 1500:
        valor += 0.74
        cont += 1
    if 1500 < cont <= 2500:
        valor += 1.25
        cont += 1
    if cont > 2500:
        valor += 2
        cont += 1

out = valor * 1.20
out = round(out)

print(out)
