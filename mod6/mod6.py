#funktio esm
def say_hello():
    print("Moi")
    print("sinä")
#print(say_hello) missä tallennus on
#print(say_hello()) suorittaa funktion ja tulostaa sen paluuarvon  none

say_hello() #ei parametriä = syötettä tai return valueta = palauta mitään

#funktio joka ottaa vastaan parametrejä = argumentteja
def say_hello_v2(username,age):
    print("Moi")
    print(username)
    print(f"ikäsi: {age}")

say_hello_v2("matti", 5)
'''
#funktio joka ottaa vastaan parametrejä ja antaa palautetta = return value
def say_hello_v2(username,age):
    #print("Moi")
    #print(username)
    #print(f"ikäsi: {age}")
    return f"hello {username}, age {age}"

print(say_hello_v2(maija, 6)

number
'''

#listojen kanssa funktio vaikuttaa pääkoodiin