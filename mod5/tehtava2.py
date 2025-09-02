'''
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta
suuruusjärjestyksessä suurimmasta alkaen.
Vihje: listan alkioiden lajittelujärjestyksen voi
kääntää antamalla sort-metodille argumentiksi reverse=True.
'''
luvut = []

syöte = input("Anna luku, tyhjä lopettaa kyselyn ")
while syöte != "":
    # lisätään syöte listaan
    print(int(syöte))
    luvut.append(syöte)
    syöte = input("Anna luku, tyhjä lopettaa kyselyn "):

luvut.sort(reverse = True)
print(luvut)

viisi_suurinta = luvut[0:5]
print(viisi_suurinta)


print("-------------tai----------------")
#uusi lista kopio olemassa olevasta listasta
viisi_suurinta = luvut[0:5]

for v in viisi_suurinta:
    print(v)

print("-------------tai----------------")
for l in range(5):
    print(luvut[l])