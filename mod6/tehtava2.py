'''Kirjoita parametriton funktio,
joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
 Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

Muokkaa edellistä funktiota siten,
että funktio saa parametrinaan nopan tahkojen yhteismäärän.
 Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes
saadaan nopan maksimisilmäluku,
joka kysytään käyttäjältä ohjelman suorituksen alussa.'''

import random
how_many_sided_dice = int(input("Nopan sivut: "))

def roll_dice():
    roll = random.randint(1,how_many_sided_dice)
    return roll
throws = []
app_on = True
while app_on:
    throw = roll_dice()
    if throw != how_many_sided_dice:
        throws.append(throw)
    elif throw == how_many_sided_dice:
        app_on = False
        throws.append(throw)
        print(throws)