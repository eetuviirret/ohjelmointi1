#while-toistolause eli silmukka eli looppi

#Älä ikinä tulee, ikuinen silmukka'
'''while True:
    print("Totta")
    print("on"'''

suorita_silmukka = True

while suorita_silmukka:
    suorita_silmukka = False
    print("Totta")
    print("on vain kerran")

print("silmukan suoritus loppui")

#iteraattori/laskukone ja while
toistojen_lukumaara = 10
i = 0

while i < toistojen_lukumaara:
    i = i+ 1 # sijoituslause
    # i += 1 toinen tapa kirjoittaa
    print(f"toistuva silmukka, in:arvo:{i}") #pitää olla näin paljon tai i alkaa nollasta ja päättyy 10:neen mutta
    #While ehto ei toteudu joten ei tulostu

print(f"i:arvo lopuksi:{i}")

toistojen_lukumaara = 10
i = 0

while i < toistojen_lukumaara:
    i = i + 2 # joka toinen numero
    print(f"toistuva silmukka, in:arvo:{i}")

print(f"i:arvo lopuksi:{i}")

# komentokehote
'''while True:
    comand = input("Komento:") #pysähtyy tähän odottamaan, ei kykene itse lopettamaan
    print(f"Komentosi oli: {comand}")
    if comand == "lopeta": #tämä osuus lopettaa simukan
            break
# continue lopettaa silmukan lopuksi'''

#tämä koodi on ruma, parempi:

app_running = True
#main loop
while app_running:
    comand = input("Komento:") #pysähtyy tähän odottamaan, ei kykene itse lopettamaan
    print(f"Komentosi oli: {comand}")
    if comand == "lopeta": #tämä osuus lopettaa simukan
            app_running = False
    elif comand == "laskukone":
        luku1 = float(input("anna ensimmäinen luku:"))
        luku2 = float(input("anna toinen luku:"))
        tulos_yhteenlasku = luku1 + luku2
        print("Yhteenlaskutoimituksen tulos:" + str(tulos_yhteenlasku))

# kolikonheitto n kertaa, kuinka monta kertaa kolikko jää pystyyn
import random

n = 10000
i = 0
kolikko_pystyssa_lukumaara = 0

while i < n:
    i += 1
    satunnaisluku = random.randint(0, 100)
    print(f"Arvottu luku:{satunnaisluku}")
    if satunnaisluku < 500:
        print("Kruuna!")
        print("kuuluu samaan koodilohkoon")
    elif satunnaisluku > 500:
        print("Klaava!")
    else:  # toteutuu muissa tapauksissa eli silloin kun satunnaisluku on 50
        print("Kolikko jäi pystyyn")
print(f"Kolikko jäi pystyyn {kolikko_pystyssa_lukumaara} kertaa")
'''
# muokattu noppaesimerkki 3 materiaalista
pelikerrat = 0
heittojen_lkm = 0
app_running = True
while app_running:
    noppa1 = noppa2 = heitot = 0
    while noppa1 != 6 or noppa2 != 6:
        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        heitot = heitot + 1
    print(f"Kahteen kutoseen tarvittiin {heitot:d} heittoa.")
    pelikerrat = pelikerrat + 1
    heittojen_lkm = heittojen_lkm + heitot
    komento = input("Pelataanko uudestaan (k/e)? ")
    if komento != "k":
        app_running = False
print(f"Kaksi kutosta saatiin keskimäärin {heittojen_lkm/pelikerrat} heitolla.")
'''
