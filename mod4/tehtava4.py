import random

ohjelma_paalla = True
vastaus = random.randint(1,10)

while ohjelma_paalla:
    arvaus = int(input("Syötä arvaus: "))
    if arvaus < vastaus:
        print("Liian pieni arvaus")
    elif arvaus > vastaus:
        print("Liian suuri arvaus")
    else:
        print("Oikein!")
        ohjelma_paalla = False