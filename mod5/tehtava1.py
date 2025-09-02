'''
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.
'''

import random

n = int(input("Anna arpakuutioiden määrä")) #numeroita laitetaan intiksi
heitot = []

for i in range(n):
    heitto = random.randint(1,6)
    print(f"heitit tällä kierroksella luvun:{heitto}")
    heitot.append(heitto)

heittojensumma = sum(heitot)

print(heittojensumma)


print("---------TAI-----------------")

n = int(input("Anna arpakuutioiden määrä")) #numeroita laitetaan intiksi
total = 0

for i in range(n):
    heitto = random.randint(1,6)
    print(f"heitit tällä kierroksella luvun:{heitto}")
    total= total + heitto
    # tai total += heitto

print(f"Arpakuutioiden yhteistulos on {total}")