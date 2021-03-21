#Henrique Shigihara
#IPL-2021
#Problema 2.4: Segundo Maior

#Parte 1:
def largest_number(input_list):
    size = len(input_list)
    if  size == 0 or size == 1:
        return None
    else:
        best_so_far = 1000**1000 * -1000

        for i in input_list:
            if i > best_so_far:
                best_so_far = i
        
        return best_so_far

#Parte 2:
def second_largest_number(input_list):
    size = len(input_list)
    if  size == 0 or size == 1:
        return None
    else:
        lista = input_list
        best = 1000**1000 * -1000
        best_2 = 1000**1000 * -1000
        
        for i in input_list:
            if i > best:
                best = i
        lista.remove(best)

        for i in lista:
            if i > best_2:
                best_2 = i

        return best_2
