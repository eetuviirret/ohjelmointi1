#fuktiot

'''Kirjoita funktio, joka saa parametrinaan bensiinin määrän
Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä
ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.'''

def usa_gal_to_l(gal):
    litre = gal*3.78541
    return litre

'''gal = 0
while gal >= 0:
    gal = int(input("Anna gallonit: "))
    print(usa_gal_to_l(gal))'''

#tai

gal = int(input("Anna gallonit: "))
while gal >= 0:
    print(usa_gal_to_l(gal))
    gal = int(input("Anna gallonit: "))

