''' edellinen tehtavä:
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma, jossa luot listan,
kutsut funktiota ja tulostat sen palauttaman summan.

nykyinen tehtavä:
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina
saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota
ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.'''

'''luvut = [8,4,5,3,5,1,7,9] 

def parilliset_luvut(luvut): 
    for l in luvut: #käy lista läpi 
        print(l) 
        if l//2 != 0 and l%2 != 0: # jos tämä 
            luvut.remove(l) 
            print("l removed") 
    print(luvut) 
    return 

parilliset_luvut(luvut)

Yritetty selvittää miksi ei toimi, kysytään chatgbt:ltä

Vastaus:
Ongelma on siinä, että muokkaat listaa samalla
kun iteroit sen yli. Tämä johtaa siihen,
että osa arvoista jää tarkistamatta,
koska kun poistat alkion listasta, indeksit siirtyvät
– mutta for-silmukka ei ota tätä huomioon.

Luo uusi lista joka sisältää vain parilliset luvut

luvut = [8, 4, 5, 3, 5, 1, 7, 9]

def parilliset_luvut(luvut):
    parilliset = [l for l in luvut if l % 2 == 0]
    print(parilliset)
    return parilliset

parilliset_luvut(luvut)

Oma luettavampi versio josta saan selvää:
'''

luvut = [8,4,5,3,5,1,7,9]

def parilliset_luvut(luvut):
    parilliset = [] #pitää tehdä oma lista parillisille kos
    for l in luvut: #käy lista läpi
        if l%2 == 0: # jos tämä
            parilliset.append(l)
    print(parilliset)
    return

parilliset_luvut(luvut)
