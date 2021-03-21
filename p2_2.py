#Henrique Shigihara
#IPL-2021
#Problema 2.2: Optimus Prime

def prime(x):
    isprime = True
    if x == 0 or x == 1:
        isprime = False
    
    if isprime == True:
        for i in range(2, x):
            if x % i == 0:
                isprime = False
                break
                    
    if isprime == True:
        return True
    else:
        return False
