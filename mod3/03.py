#valintarakenne esimerkkejä
#onko_totta = True
#onko_totta = 3 == 3
import random
satunnaisluku = random.randint(0,100)

print(f"Arvottu luku:{satunnaisluku}")

#kolikonheittosimulaatio
if satunnaisluku < 50:
    print("Kruuna!")
    print("kuuluu samaan koodilohkoon")
elif satunnaisluku > 50:
    print("Klaava!")
else: #toteutuu muissa tapauksissa eli silloin kun satunnaisluku on 50
    print("Kolikko jäi pystyyn")

print ("Ohjelman suoritus if lauseen jälkeen jatkuu tästä.")

# dummy-kirjautuminen
oikea_salasana = "salakala"
tunnus = "matti"
input_tunnus = input("Käyttäjätunnus: ")
input_salasana = input("Anna salasana: ")

if input_tunnus == tunnus:
    if input_salasana == oikea_salasana and input_tunnus == tunnus:
        print("Tervetuloa!")
        kehote = input("Mitäs haluat tehdä? ")
        if kehote == "tervehtiä":
            print("No morjes!")
        else:
            print("En ymmätänyt kehotetta")
    else:
        print("Väärä salasana")

print("Ohjelma suljettu. Heippa!")

print(True and False)

