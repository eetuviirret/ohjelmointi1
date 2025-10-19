'''Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
että pieniä lentokenttiä on 65 kappaletta,
helikopterikenttiä on 15 kappaletta jne'''

import mysql.connector
connection = mysql.connector.connect(
    port=3306,
    host="127.0.0.1",
    database="flight_game",
    user="eetuviirret",
    password="Kuukoira2025",
    autocommit=True)
