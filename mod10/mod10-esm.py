class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return

koira1 = Koira("Muro", 2018, "Booooof")
koira2 = Koira("Fifi", 2024, "Jip Jip")
koira3 = Koira("Spot", 2022, "Wooof")
koira4 = Koira("Lissu", 2022, "Hau hau")

    print(koira1.nimi)
    koira1.hauku(3)

class Hoitola:
    def __init__(self, nimi)
        self.nimi = nimi
        self.koiralista = []

    def koira_sisaan(self, Koira):
        print(f"Koira {Koira.nimi} kohta sisään")
        print(Koira)
        self.koiralista.append(Koira)

    def koira_ulos(self):
        print("Koira sisään")
        self.koiralista.remove(Koira)

    def printaa_koirat(self):
        for Koira in self.koiralista:
            print(f"{self.nimi}-hoitolassa on seuraavat koirat:")
            print(Koira.nimi)

    def tervehdi_koiria(self, kertaa):
        print("koirat haukahtavat iloisesti:")
        for Koira in self.koiralista:
            Koira.hauku(kertaa)

class Yritys:
    def __init__(self, nimi, osoite):
        self.nimi = nimi
        self.osoite = osoite
        self.hoitola =[]

    def lisaa_hoitola(self):
        self.hoitola.append(Hoitola)

    def anna_joululahja(self):
        print("yritys antaa joululahjan")
        for h in self.hoitola:
            for k in koiralista

    def tulosta_hoitola(self):
        for h in self.hoitola:
            print(Hoitola.nimi)

hoitola1 = Hoitola("Onnentassu")
hoitola2 = Hoitola("Tassujengi")

#lisätään koira koirahoitolaan
hoitola1.koira_sisaan(koira1)
hoitola1.koira_sisaan(koira2)
hoitola2.koira_sisään(koira3)
hoitola2.koira_sisaan(koira4)

hoitola1.printaa_koirat()
hoitola1.tervehdi_koiria(2)

yritys = Yritys("Musti ja mirri", "Onnenkuja 2")