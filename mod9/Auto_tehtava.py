import random
from operator import truediv

'''Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus,
huippunopeus, tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja,
joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.'''

class Car:
    def __init__(self, register_number, top_speed, speed = 0, trip = 0):
        self.register_number = f"ABC-{register_number}"
        self.top_speed = top_speed
        self.speed = speed
        self.trip = trip


    def accelerate(self, acceleration):
        self.speed = self.speed + acceleration
        if self.speed > self.top_speed:
            self.speed = self.top_speed
        elif self.speed < 0:
            self.speed = 0

    def car_run(self, time):
        self.trip = self.trip + self.speed * time

class race:
    def __init__(self, race_name, length):
        self.race_name = race_name
        self.length = length
        self.race_cars = []

    def hour_pass(self):
        for r in self.race_cars:
            r.accelerate(random.randint(-10, 15))
            r.car_run(1)
            '''print(r.trip)'''


    def print_present_situation(self):
        for r in self.race_cars:
            print(f"Car's register number is {r.register_number}")
            print(f"Car's top speed is {r.top_speed}km/h")
            print(f"Car's current speed is {r.speed}km/h")
            print(f"Car's trip is {r.trip}km")
            print(f"----------------------------------------")

    def race_over(self):
        winner = False
        for i in self.race_cars:
            if i.trip >= self.length:
                winner = True
        return winner


'''
car1 = Car("123", 142)

print(car1.speed)
print(car1.trip)
print(car1.top_speed)
print(car1.register_number)'''

'''Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
joka saa parametrinaan nopeuden muutoksen (km/h).
Jos nopeuden muutos on negatiivinen, auto hidastaa.
Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi
eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten,
 että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h
ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h
ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.
'''
'''
car1.accelerate(30)
car1.accelerate(70)
print(f"Auton 1 nopeus on {car1.speed}km/h")

car1.accelerate(-200)

print(f"Auton 1 nopeus on {car1.speed}km/h")'''

'''Laajenna ohjelmaa siten, että mukana on kulje-metodi,
joka saa parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa sen verran
kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.'''
'''
car2 = Car("ABC-456", 142, 60, 2000)
car2.car_run(1.5)
print(car2.trip)'''

'''Nyt ohjelmoidaan autokilpailu. 
Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
Tämä tehdään kutsumalla kiihdytä-metodia.

Kaikkia autoja käsketään liikkumaan yhden tunnin ajan.
Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.m
'''
'''print("---------------------------------")
print("Race begins!")
print("---------------------------------")
race_cars =  []
competition = True
for c in range (9):
    register_number = c + 1
    race_cars.append(Car(f"{register_number}", random.randint(100,200), 0, 0))

while competition:
    for r in race_cars:
        r.accelerate(random.randint(-10,15))
        r.car_run(1)
        if r.trip >= 10000:
            competition = False


winner = 0
for r in race_cars:
    print(f"Car's register number is {r.register_number}")
    print(f"Car's top speed is {r.top_speed}km/h")
    print(f"Car's current speed is {r.speed}km/h")
    print(f"Car's trip is {r.trip}km")
    print(f"----------------------------------------")
    if r.trip >= 10000:
        winner = r.register_number


print(f"Winner is {winner}")'''

'''Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. 
Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja,
joka saa parametreinaan nimen, kilometrimäärän ja autolistan
ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut
tunnin välein tehtävät toimenpiteet eli arpoo kunkin auton
nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.

tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset
tiedot selkeäksi taulukoksi muotoiltuna.

kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa
eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.
Muussa tapauksessa palautetaan False.

Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä
"Suuri romuralli". Luotavalle kilpailulle annetaan kymmenen 
auton lista samaan tapaan kuin aiemmassa tehtävässä.
Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa
tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan 
kilpailu_ohi-metodin avulla, onko kilpailu ohi.
Ajantasainen tilanne tulostetaan tulosta tilanne-metodin
avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen,
kun kilpailu on päättynyt.'''

print("------Suuri romuralli----------------")

romuralli = race("Suuri romuralli", 1000)

for c in range (9):
    register_number = c + 1
    romuralli.race_cars.append(Car(f"{register_number}", random.randint(100,200), 0, 0))

while romuralli.race_over() == False:
    romuralli.hour_pass()
    romuralli.print_present_situation()

