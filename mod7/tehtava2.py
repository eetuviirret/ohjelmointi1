'''
Kirjoita ohjelma,
joka kysyy käyttäjältä nimiä siihen saakka,
kunnes käyttäjä syöttää tyhjän merkkijonon.
Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko
tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
syötettiinkö nimi ensimmäistä kertaa.
Lopuksi ohjelma luettelee
syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
Käytä joukkotietorakennetta nimien tallentamiseen.
'''

#joukkotietorakenne tulee kokeeseen
#järjestys aina muuttuu, ei voida käyttää indeksiä
#voi muokata eli lisätä ja poistaa

nimijoukko = set()

kysy = True

while kysy:
    nimi = input("Anna nimi: ").upper() #iso kirjain
    if nimi == "":
        kysy = False
    #tutki onko nimi jo listassa
    elif nimi in nimijoukko:
        print("Aiemmin syötetty nimi, löytyy jo listasta. ")
    else:
        print(f"Uusi nimi. {nimi} lisätty listaan.")
        nimijoukko.add(nimi)
print("Kaikki syötetyt nimet:❤️")
for nimi in nimijoukko:
    print(nimi)