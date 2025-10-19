'''Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja
sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.'''

import mysql.connector
connection = mysql.connector.connect(
    port=3306,
    host="127.0.0.1",
    database="flight_game",
    user="eetuviirret",
    password="Kuukoira2025",
    autocommit=True)

icao_koodi = input("Icao-koodi: ")

cursor = connection.cursor()
sql = f"SELECT name, municipality FROM airport WHERE airport.ident = '{icao_koodi}'"
cursor.execute(sql)
result = cursor.fetchall()
print(f"Lentokenttä: {result[0][0]}, Kunta: {result[0][1]}")

# jos tulosjoukko on tyhjä
if result:  # sama kuin result != None:
    return result[0]
return "Ei löydy"


