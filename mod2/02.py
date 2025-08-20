#tuntiesimerkki

'''
Monirivinen kommentti
'''



kommentti = '''
monirivinen kommentti (merkkijono,string) 
voidaan myös sijoittaa muuttujaan
'''
#näkyykö tallennus

nimi = input('anna nimesi') # palauttaa merkkijonon (str)
ika='20' #kokonaisluku (int)
ika_ensi_vuonna = ika + 1 #int
str_ika_ensi_vuonna = str(ika_ensi_vuonna) # tulee '21' int muuttamine str

tervehdys = "moi" + nimi
1+2
#muuttuja määritellään

print(tervehdys)

tervehdys= 'moi' + nimi + '' + ika_ensi_vuonna
1+2
#tyhjä'' on välilyönti

#simppeli laskukone

#Lasketaan tulos numeerisilla arvoilla
luku1=input('anna ensimmäinen luku:')
luku2=input('anna toka luku:')

#tulos= int(luku1) + int(luku2) #kokonaisluvuilla
tulos_yhteenlasku= float(luku1) + float(luku2) #liukuluvuilla

#tulos = 1+2 koodattu arvo test
print('yhteenlaskutoimituksen tulos'+ str(tulos_yhteenlasku)) # int muuttaminen str str(tulos)