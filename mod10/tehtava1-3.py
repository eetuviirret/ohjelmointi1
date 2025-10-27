'''Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
Uusi hissi on aina alimmassa kerroksessa.
Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
että hissi päätyy viidenteen kerrokseen.
Viimeksi mainitut metodit ajavat hissiä yhden kerroksen
ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi
kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.'''

class Hissi:
    def __init__(self, alin_kerros , ylin_kerros):
        self.alin_kerros = 0
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = self.alin_kerros

    def kerros_alas(self):
        if self.nykyinen_kerros > 0:
            self.nykyinen_kerros = self.nykyinen_kerros - 1
        else:
            self.nykyinen_kerros = 0

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros = self.nykyinen_kerros + 1
        else:
            self.nykyinen_kerros = self.ylin_kerros

    def siirry_kerrokseen(self, haluttu_kerros):
        if self.nykyinen_kerros > haluttu_kerros:
            while self.nykyinen_kerros != haluttu_kerros:
                self.kerros_alas()
        elif self.nykyinen_kerros < haluttu_kerros:
            while self.nykyinen_kerros != haluttu_kerros:
                self.kerros_ylos()


hissi_h = Hissi(0, 10)
hissi_h.kerros_ylos()
print(hissi_h.nykyinen_kerros)
hissi_h.kerros_alas()
print(hissi_h.nykyinen_kerros)
hissi_h.siirry_kerrokseen(5)
print(hissi_h.nykyinen_kerros)
hissi_h.kerros_ylos()
print(hissi_h.nykyinen_kerros)
hissi_h.siirry_kerrokseen(5)
print(hissi_h.nykyinen_kerros)


