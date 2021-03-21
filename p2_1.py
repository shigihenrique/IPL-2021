#Henrique Shigihara
#IPL-2021
#Problema 2.1: It's Hip To Be Square

def square(x):
    return x**2

def fourth_power(x):
    temp = square(x)
    res = square(temp)
    return res

def perfect_square(x):
    if x == 0 or x == 1:
        return True
    else:
        return False
