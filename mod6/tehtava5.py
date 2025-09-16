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

luvut = [8,4,5,3,5,1,7,9]

def parilliset_luvut(luvut):
    parilliset = []
    for l in luvut: #käy lista läpi
        if l%2 == 0: # jos tämä
            parilliset.append(l)
    print(parilliset)
    return

parilliset_luvut(luvut)
