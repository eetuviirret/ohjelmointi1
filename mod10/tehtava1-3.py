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
    #oletuskerros 4 viimeisen kohdan vuoksi
    def __init__(self, alin_kerros , ylin_kerros = 4):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = self.alin_kerros

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros = self.nykyinen_kerros - 1
        else:
            self.nykyinen_kerros = self.alin_kerros

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

'''Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen 
numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo
tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan
hissin numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon 
luomiseksi ja talon hisseillä ajelemiseksi.'''

print("-------------------------------------------------------------------")

class Talo:
    def __init__(self, alin_kerros , ylin_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for h in range(hissien_lukumaara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))


    def aja_hissia(self, hissin_numero, haluttu_kerros):
        #koska käyttäjä alkaa helposti laskemaan hissejä 1:stä eikä 0:sta miinustetaan suötettävästä luvusta 1
        #koska listat alkavat luvusta 0
        self.hissit[hissin_numero-1].siirry_kerrokseen(haluttu_kerros)

    def palo_halytys(self):
        for h in range(len(self.hissit)):
            self.hissit[h].siirry_kerrokseen(self.alin_kerros)

#ensimmäiseen hissiin viitataan vieläkkin indeksillä 0 koodissa
#käyttäjälle on yksi suurempi
talo1 = Talo(1, 5, 3)
print(talo1.hissit[0].nykyinen_kerros)
talo1.aja_hissia(1, 5)
print(talo1.hissit[0].nykyinen_kerros)
talo1.aja_hissia(1, 3)
print(talo1.hissit[0].nykyinen_kerros)

print(f"Hissi 1 on kerroksessa {talo1.hissit[0].nykyinen_kerros}")

'''Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on 
parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen.
Jatka pääohjelmaa siten, että talossasi tulee palohälytys.'''
print("-------------------------------------------------------")

talo1.palo_halytys()
print(talo1.hissit[0].nykyinen_kerros)
print(talo1.hissit[1].nykyinen_kerros)
print(talo1.hissit[2].nykyinen_kerros)
print("-------------------------------------------------------")

talo2 = Talo(-1, 5, 3)
talo2.aja_hissia(1, 3)
talo2.aja_hissia(2, 0)
talo2.aja_hissia(3, 5)
print(talo2.hissit[0].nykyinen_kerros)
print(talo2.hissit[1].nykyinen_kerros)
print(talo2.hissit[2].nykyinen_kerros)
talo2.palo_halytys()
print(talo2.hissit[0].nykyinen_kerros)
print(talo2.hissit[1].nykyinen_kerros)
print(talo2.hissit[2].nykyinen_kerros)

'''jos haluaa että hiisillä on esimerkiksi oletus ylinkerros, pitää antaa kaikki kysyttävät parametrit ennen oletusarvoa
huomioi että tällöin pitäisi olla myös parmetri viimeisenä talo- määrityksessä. 
Olisi siis jäkevämpää luoda talolle oletettu ylin kerros. Mutta esimerkkinä oletusarvoista kumminkin:'''
hissi4 = Hissi(1)
hissi4.siirry_kerrokseen(4)
print(hissi4.nykyinen_kerros)
