'''Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
Kirjoita hakukenttään geopy ja vie asennus loppuun.'''

import mysql.connector
from geopy import distance
connection = mysql.connector.connect(
    port=3306,
    host="127.0.0.1",
    database="flight_game",
    user="eetuviirret",
    password="Kuukoira2025",
    autocommit=True)

airport_1 = input("Anna ensimmäisen lentokentän icao-koodi:")
airport_2 = input("Annan toisen lentokentän icao-koodi:")

def get_airport_info(icao):
    sql = f"SELECT ident, name, latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result

'''print(get_airport_info(airport_1))
print(get_airport_info(airport_2))'''

def calculate_distance(airport_1, airport_2):
    start = get_airport_info(airport_1)
    end = get_airport_info(airport_2)
    return distance.distance((start["latitude_deg"], start["longitude_deg"]),
                             (end["latitude_deg"], end["longitude_deg"])).km


print(f"Etäisyys on {calculate_distance(airport_1, airport_2)}km")