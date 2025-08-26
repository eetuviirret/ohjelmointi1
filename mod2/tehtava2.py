import math

'''
tai sade = int(input("Kirjoita ympyran säde"))
'''
sade = input("Kirjoita ympyrän säde: ")
int_sade = int(sade)

ympyran_pinta_ala = math.pi * int_sade ** 2
print(ympyran_pinta_ala)