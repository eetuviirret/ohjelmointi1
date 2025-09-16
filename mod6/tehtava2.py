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