
i = 0
ohjelma_paalla = True

while ohjelma_paalla:
    if i < 5:
        kayttajatunnus_syote = input("Anna käyttäjätunnus:")
        salasana_syote = input("Anna salasana:")
        if kayttajatunnus_syote == "python" and salasana_syote == "rules":
            print("Tervetuloa")
            ohjelma_paalla = False
        else:
            print("Pääsy evätty")
            i = i + 1
    if i == 5:
        ohjelma_paalla = False
        print("Pääsy evätty 5 kertaa. Ohjelma sammutetaan.")
