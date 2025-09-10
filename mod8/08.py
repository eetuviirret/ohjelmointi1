#otetaan tietokantaan yhteys:
import mysql.connector
connection = mysql.connector.connect(
    port=3306,
    host="127.0.0.1",
    database="flight_game",
    user="eetuviirret",
    password="Kuukoira2025",
    autocommit=True)
#host numero viittaa omaan koneeseen voi kirjoittaa myös localhost

#tarkistetaan yhteys
print(connection)
#luodaan ositin (kursori) ja sijoitetaan viittaus siihen muuttujaan
cursor = connection.cursor()
cursor.execute("SELECT name FROM country")

#haetaan tulosjoukosta rivi kerrallaan
result = cursor.fetchone() #palauttaa rivin pyydetyt sarakkeet monikkona
print(result)
result = cursor.fetchone()
print(result)
#haetaan useampi rivi kerrallaan (3kpl), palauttaa "rivimonikot" listana
result = cursor.fetchmany(3)
print(result)
#tyypillisin tapa= haetaan kaikki (loput) tulokset
result = cursor.fetchall()
print(f"Resault listan pituus {len(result)}")

#tulostetaan ensimmäisen rivin maakoodi
print(result[0][1])

#tulostetaan tulosjoukko muotoiltuna
for country in result:
    print(f"maan {country[0]} maakoodi on {country[1]}")

#ohjelma joka hakee maan maakoodin perusteella

#funktio joka hakee sovelluksen
def get_country_name_by_code(code):
    sql = f"SELECT name FROM country WHARE iso_country = '{code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    #jos maata ei löydy
    if result == None:
    #if not result:
        return "Ei löydy"
    #else: ei pakko kirjoittaa
    return result[0]
print(get_country_name_by_code("YE"))

#käyttöliittymä samasta
country_code = input("Anna maa koodi:")
result = get_country_name_by_code(country_code)
print(f"Maakoodi: {country_code}, hakutulos: {country}")

def add_country(code, name):
    sql = f"INSERT INTO country (iso_country, name) VALUES ('{code}','{name}')"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()

    add_country()