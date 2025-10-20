'''Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.'''

class Car:
    def __init__(self):
        self.speed = 0
        self.trip = 0
        self.top_speed = 100
        self.register_number = "abc-123"
    def accelerate(self):
        seld.speed += 1

car1 = Car()
car2 = Car()
car1.accelerate()
car1.accelerate()

print(f"Auto 1 nopeus on {car.speed}km/h")

cars = [Car(), Car()]
cars[0].accelerate()
cars[0].accelerate()

cars = []
for in the range (9):
    cars.append(Car())
far car in cars:
    print(f"Auto {car.register_number} nopeus on {car.speed}km/h")
