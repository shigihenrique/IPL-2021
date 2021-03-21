#Henrique Shigihara
#IPL-2021
#Problema 1.3: divmod

dividend = 15
divisor = 4
temp_dividend = dividend
temp_divisor = divisor

quociente = 0
while temp_dividend >= divisor:
    temp_dividend -= temp_divisor
    quociente += 1
resto = temp_dividend
out = (quociente, resto)

print(out)
