'''Toteuta seuraava luokkahierarkia Python-kielellä:
Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
Kirjalla on lisäksi kirjoittaja ja sivumäärä,
kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
Tee aliluokkiin metodi tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot.
Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä)
ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.'''

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

#kirjoitettaan perittävä luokka parametrinä
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        #tuodaan perittävät parametrit
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(self.nimi)
        print(self.kirjoittaja)
        print(self.sivumaara)


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(self.nimi)
        print(self.paatoimittaja)

lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")
lehti1.tulosta_tiedot()

print("--------------------------------------------")

kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
kirja1.tulosta_tiedot()