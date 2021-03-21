#Henrique Shigihara
#IPL-2021
#Problema 3.8: Compondo Funções

def composite_result(f, g, x):
    res = f(g(x))
    return res

def composite(f, g):
    def funcao(x):
        res = f(g(x))
        return res
    return funcao
    