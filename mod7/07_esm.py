#monikko eli tuple on kuin lista jota ei voi muokata
#käytetään muitinhallintaan "kiinteä muitiinhallinta"

lista = [1,2,3,4,5,6,7,8,9]
monikko = (1,2,3,4,5,6,7,8,9)

monikko2 = 1, 2, 3, 4, 5, 6,7,8, 9
print(monikko2)
#Monikon voi luoda ilman kaarisulkeita

#monikko voi sisältää erilaista tietoja
monikko3 = (1,2, "ulla", (3,4,), 88)

#luetaan listan ja monikon ensimmäinen alkio
print(lista[0])
print(monikko[0])

#Toisin kuin lista, monikko on kuitenkin muuttumaton:
# siihen ei voi lisätä alkioita eikä siitä voi poistaa alkioita monikon luonnin jälkeen.
#kokeeseen

lista[0] = 0
lista.append(7)
print("muokattu lista", lista)

#monikkoa ei voi muokata
# tämä ei toimi monikko[0] = 0
'''Monikkoa on tarkoituksenmukaista käyttää tilanteissa, joissa alkioiden jono on luonteeltaan staattinen: 
tiedetään, että muutoksille ei ole tarvetta ohjelman suorituksen aikana.'''

#esimerkki
'''
viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")
'''
#kesken yläpuolella
print("--------------------------------------------------------------")

#monikon arvojen purku muuttujiin
hedelmät = ("Appelsiini", "Banaani", "Omena")
(eka, toka, kolmas) = hedelmät
print (f"Hedelmiä ovat {eka}, {toka} ja {kolmas}.")

#moikoin voi antaa funktiolle parametrinä

def tulosta_monikko(hedelmät):
    for h in hedelmät:
        print(h)
tulosta_monikko(hedelmät)

def heitä():
    eka = random

print("--------------------------------------------------------------")
#Joukko

kayttajanimi = input("anna nimi kayttajanimi ")