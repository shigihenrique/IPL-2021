#Henrique Shigihara
#IPL-2021
#Problema 2.5: Cifra de César

import string

def caesar_cipher(texto, shift):
    abc = string.ascii_lowercase
    digits = string.digits 
    text = texto.lower()
    out = ''

    for i in text:
        if i in digits: #numeros
            num = digits.find(i)
            chave = num + shift
            while chave > 9:
                chave -= 10
            while chave < 0:
                chave += 10
            out += digits[chave]

        elif i in abc: #letras
            letra = abc.find(i)
            chave = letra + shift
            while chave > 25:
                chave -= 26
            while chave < 0:
                chave += 26
            out += abc[chave]

        else:
            out += i

    return out
