tuumat = int(input("Anna tuumat: "))
while tuumat > 0:
    sentit = tuumat * 2,54
    print(sentit)
    tuumat = int(input("Anna tuumat: "))


#tai
ohjelma_paalla = True
while ohjelma_paalla == True:

    tuumat = int(input("Anna tuumat: "))
    if tuumat < 0:
        ohjelma_paalla = False
    else:
        sentit = tuumat * 2,54
        print(sentit)

