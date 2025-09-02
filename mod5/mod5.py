nimi = "ulla"
nimi2 = "Matti"
ika = 45
ika2 = 56

print(f"Hei {nimi} ikäsi on {ika}")

lista = []

nimet = ["Anna", "Liisa", nimi, nimi2, "toni" , "Ilkka"]
print(nimet)

# lista voi sisältää useita listoja
ikalista = [45, 56, 78, [98, 4, 17]]
print(ikalista)
# Listan pituus
print(len(nimet))

# tee oma lista

#alkioon viitataan ideksinumerolla alkaen numerolla 0
print(f"Hei {nimet[0]} ja terve myös {nimet[4]}")

#listan sisäällä oleva lista lasketaan muuttujaksi
print(ikalista[3][1])

#listasta voi hakea tietoa alkion indeksin avulla
#Tai viipaloimalla

nimet2 = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary", "mary", "anna", "ulla", "pasi"]
print(nimet2[3]) #olga
print(nimet2[1]) #ahmed

print(nimet2[1:3]) #(alkupiste mukaan lukien) ja indeksiin 2 päättyen (päätepiste pois lukien)
print(nimet2[-1])
print(nimet2[1:-1]) # taksepain laskiessa alkaa numerolla 1
print(nimet2[1:-1:2]) #askel
print ("______________________")
#uusi_lista = vanha_lista[alku:loppu:askel]
uusi_lista = nimet2[2:4]
print(nimet2)
print(uusi_lista)

kaupungit =["Helsinki", "Turku", "Jyväskylä", "Oulu", "Rovaniemi", "tampere"]
print(kaupungit[0:3]) #nollaa ei ole pakko kirjoittaa jos kyse on ensimmäinen listasta kaupungit[:3]
print(kaupungit[-1])

#viittaus listan ulkopuolelle aiheuttaa virheen
#print(kaupungit[7]

kaupungit.append("uusi kaupunki")
print (kaupungit)
#kaupungit.remove("Iisalmi") virhe ei listassa

# onko ja poisto
if "tampere" in kaupungit:
    print(f"Tampere löytyi")
    kaupungit.remove("tampere")
    print(kaupungit)

#Lisätään ensimmäiseksi
kaupungit.insert(0,"tampere")
print(kaupungit)

#tutkitaan monesko indeksi
monesko = kaupungit.index("Oulu")
print(monesko)

lisaa_kaupunkeja = ["sodankylä", "sipöö", "kotka"]
kaupungit.extend(lisaa_kaupunkeja)
print(kaupungit)

kaupungit[7] = "Sipoo"
print(kaupungit)

hedelmia = ["greippi", "appelsiini", "Appelsiini", "banaani"]
numerolista = [1000, 5, 3, 8]

hedelmia.sort()
print(hedelmia)

numerolista.sort()

luvut = [2,4,6,5]
print(len(luvut))
print(sum(luvut))
print(min(luvut))
print(max(luvut))
print(luvut.count(2)) #kuinka monta lukua kaksi listassa on

print ("______________________")

i = 0
while i < len(luvut):
    print(luvut[i])
    i = i + 1
tottavaiei = True # python on dynaamisesti tyypitetty, nyt boolean
tottavaiei = "True" # nyt string
print(type(tottavaiei))

viikonpaivat = ["Maanantai", "Tiistai"]
print(viikonpaivat)

print("-----------------------")
print("Muutamia hyödyllisia funktiota tulevaisuutta varten")
print("-----------------------")

# listoille toimii mm. tämänlaiset funktiot
# len, sum, min, max, count
luvut = [2,4,6,5,2,7,2,7]
print(len(luvut)) # pituus
print(sum(luvut)) # lukujen summa
print(min(luvut)) # pienin numero
print(max(luvut)) # isoin numeroa
print(luvut.count(2)) # kuinka monta lukua 2 listassa on

print("-----------------------")
print("Miten käydään lista läpi iteroimalla")
print("-----------------------")

luvut[2]

# luvut = [2,4,6,5,2,7,2,7]

i = 0
while i < len(luvut):
    # print(i)
    print(luvut[i])
    # i = i + 1
    i += 1

print("-----------------------")
# käydä listan läpi alkio alkiolta


for kirjain in "abcdefg":
    print(kirjain)

print("-----------------------")

for alkio in [1, 2, 3, 4, 5, 6]:
    print(alkio)

print("-----------------------")

for luku in luvut:
    print(luku)

print("-----------------------")

# tässä tapauksessa kaupunki on kierrosmuuttuja
for kaupunki in kaupungit:
    print(kaupunki)

print("-----------------------")

for numero in range(5):
    print(numero)

for n in range(4,80, 2):
    print(n)

print("-----------------------")
print("Nurinpäin")

for n in range(50, 0, -2):
    print(n)

print("-----------------------")

#luvut = [2,4,6,5,2,7,2,7]
luvut_listan_pituus = len(luvut)
for n in range(luvut_listan_pituus):
    # print(n) -> tämä on iteraattori
    print(luvut[n])

print("-----------------------")
# printataan vain 3
for n in range(3):
    print(kaupungit[n])
print("-----------------------")
for luku in luvut:
    print(luku)

print ("______________________")





'''
nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while nimi!="":
    nimet.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

print(nimet)
'''