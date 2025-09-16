'''Kirjoita ohjelma,
joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan
allekkain samassa järjestyksessä kuin ne syötettiin.
käytä for-toistorakennetta nimien kysymiseen ja
for/in toistorakennetta niiden läpikäymiseen.'''


n = 5 #kun n voi vaihtaa kysymysten määrää
# tyhjä lista
kaupungit = []

for i in range(n):
    print(i)
    nimi = input(f"Anna {i+1}. kaupungin nimi: ")
    kaupungit.append(nimi)

for kaupunki in kaupungit:
    print(kaupunki)

