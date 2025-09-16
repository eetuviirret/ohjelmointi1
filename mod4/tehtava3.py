
ohjelma_paalla = True
luku = input("Anna luku: ")
suurin = int(luku)
pienin = int(luku)

while ohjelma_paalla:
    luku = input("Anna luku: ")
    if luku == "":
        ohjelma_paalla = False
    else:
        luku = int(luku)
        if luku > suurin:
            suurin = luku
        if luku < pienin:
            pienin = luku
print(suurin)
print(pienin)