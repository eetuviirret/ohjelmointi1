'''
Kirjoita parametriton funktio,
joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
'''

import random
def roll_dice():
    roll = random.randint(1,6)
    return roll
throws = []
app_on = True
while app_on:
    throw = roll_dice()
    if throw != 6:
        throws.append(throw)
    elif throw == 6:
        app_on = False
        throws.append(throw)
        print(throws)