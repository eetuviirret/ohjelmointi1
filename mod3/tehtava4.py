vuosiluku = input("Kirjoita vuosi: ")
int_vuosiluku = int(vuosiluku)

#jakojäännöksen puuttuminen tarkistetaan käyttäen % jakaja = 0
#! kääntää merkityksen
if int_vuosiluku % 4 == 0 and (int_vuosiluku % 100 != 0 or int_vuosiluku % 400 == 0):
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")