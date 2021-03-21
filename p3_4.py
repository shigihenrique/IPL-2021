#Henrique Shigihara
#IPL-2021
#Problema 3.4: Põe na Minha Conta

def lend_money(debts, person, amount):
    chaves = debts.keys()
    if person in chaves:
        debts[person].append(amount)
    else:
        debts[person] = []
        debts[person].append(amount)

def amount_owed_by(debts, person):
    chaves = debts.keys()
    total = 0
    if person in chaves:
        for valor in debts[person]:
            total += valor
    return total

def total_amount_owed(debts):
    chaves = debts.keys()
    total = 0
    for person in chaves:
        for valor in debts[person]:
            total += valor
    return total
