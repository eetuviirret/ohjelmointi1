'''Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus,
huippunopeus, tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja,
joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.'''

class Car:
    def __init__(self, register_number, top_speed):
        self.speed = 0
        self.trip = 0
        self.register_number = register_number
        self.top_speed = top_speed

    def accelerate(self, acceleration):
        self.speed = self.speed + acceleration
        if self.speed > self.top_speed:
            self.speed = self.top_speed
        elif self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed

car1 = Car("ABC-123", 142)

print(car1.speed)
print(car1.trip)
print(car1.top_speed)
print(car1.register_number)

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

car1.accelerate(30)
car1.accelerate(70)
print(f"Auton 1 nopeus on {car1.speed}km/h")

car1.accelerate(-200)

print(f"Auton 1 nopeus on {car1.speed}km/h")

'''
cars = [Car(), Car()]
cars[0].accelerate()
cars[0].accelerate()

cars = []
for c in range (9):
    cars.append(Car())
for car in Cars:
    print(f"Auto {car.register_number} nopeus on {car.speed}km/h")
'''
