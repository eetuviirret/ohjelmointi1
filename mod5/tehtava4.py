n = 5 #kun n voi vaihtaa kysymysten määrää
# tyhjä lista
kaupungit = []

for i in range(n):
    print(i)
    nimi = input(f"Anna {i+1}. kaupungin nimi: ")
    kaupungit.append(nimi)

for kaupunki in kaupungit:
    print(kaupunki)

