'''
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
Ohjelma kysyy käyttäjältä,
haluaako tämä syöttää uuden lentoaseman,
hakea jo syötetyn lentoaseman tiedot vai lopettaa.
Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
Jos käyttäjä valitsee haun,
ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
kunnes hän haluaa lopettaa.
(ICAO-koodi on lentoaseman yksilöivä tunniste.
Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
Löydät koodeja helposti selaimen avulla.)
'''
icao_list = {
    "HYP": "hyperion",
    "HOP": "Air hop lentokenttä"
}
''' lnimi = icao_list["HYP"]
    print(lnimi)
'''

ask = True
while ask:

    cmd = input("Haluatko syöttää lentoaseman (u), hakea jo syötetyn lentoaseman (h) vai lopettaa (l): ").lower()

    if cmd == "u":
        print("Lisätään uusi kenttä")
        icao = input("Anna ICAO koodi:" ).upper()
        nimi = input("Anna lentokentän nimi: ")
        icao_list[icao] = nimi #jos olemassa ylikirjoittaa edellisen
        print("Lentokenttä lisätty:", icao_list)
    elif cmd == "h":
        print("Haetaan lentokenttä")
        icao = input("Anna ICAO koodi mitä haetaan (HYP): ").upper()
        if icao in icao_list:
            print(f"Haulla {icao} löytyi lentokenttä:", icao_list[icao])
    elif cmd == "l":
        print("Lopetetaan")
        ask = False
    else:
        print("Viheellinen syöte, ohjelma lopetettaan")
        ask = False