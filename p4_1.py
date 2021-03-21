#Henrique Shigihara
#IPL-2021
#Problema 4.1: Armazém

#Parte 1: Processo:
def warehouse_process(dicionario, transacao):
    acao, produto, valor = transacao[0], transacao[1], transacao[2]
    if acao == 'receive':
        if produto in dicionario.keys():
            dicionario[produto] += valor
        else:
            dicionario[produto] = valor
    elif acao == 'ship':
        if produto in dicionario.keys():
            dicionario[produto] -= valor
            if dicionario[produto] < 0:
                dicionario[produto] = 0
                print('not enough')
        else:
            print('not enough')

#Parte 2: Uma Solução Mais Elegante:
class Warehouse:
    def __init__(self):
        self.dic = {}

    def process(self, trans):
        warehouse_process(self.dic, trans)

    def lookup(self, prod):
        if prod in self.dic.keys():
            return (self.dic[prod])
        else:
            return 0
