#Henrique Shigihara
#IPL-2021
#Problema 5.1: Turmites

class Formiga:
    def __init__(self, linha, coluna, move):
        self.linha = linha
        self.coluna = coluna
        self.move = move

def run_langton(rules, size):
    cores = len(rules)
    centro = size//2
    count = 0
    matriz = [[0 for i in range(size)] for j in range(size)]
    dentro = True
    
    flik = Formiga(centro, centro, 'cima')
    
    while dentro == True:
        #mudar cor
        matriz[flik.linha][flik.coluna] += 1
        if matriz[flik.linha][flik.coluna] >= cores:
            matriz[flik.linha][flik.coluna] = 0
        
        #avancar celula
        if flik.move == 'cima':
            flik.linha -= 1
        elif flik.move == 'baixo':
            flik.linha += 1
        elif flik.move == 'direita':
            flik.coluna += 1
        elif flik.move == 'esquerda':
            flik.coluna -= 1
        count += 1

        #esta dentro?
        if flik.linha < 0 or flik.coluna < 0 or flik.linha >= size or flik.coluna >= size:
            dentro = False

        #girar
        if dentro == True:
            cor = matriz[flik.linha][flik.coluna]
            regra = rules[cor]
            if flik.move == 'cima':
                if regra == 'R':
                    flik.move = 'direita'
                elif regra == 'L':
                    flik.move = 'esquerda'
            elif flik.move == 'baixo':
                if regra == 'R':
                    flik.move = 'esquerda'
                elif regra == 'L':
                    flik.move = 'direita'
            elif flik.move == 'direita':
                if regra == 'R':
                    flik.move = 'baixo'
                elif regra == 'L':
                    flik.move = 'cima'
            elif flik.move == 'esquerda':
                if regra == 'R':
                    flik.move = 'cima'
                elif regra == 'L':
                    flik.move = 'baixo' 
        
    return (count, matriz)
