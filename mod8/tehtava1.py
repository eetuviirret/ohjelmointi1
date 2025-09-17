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
cursor.execute("SELECT name, iso_region FROM airport WHERE airport.ident = icao_koodi)