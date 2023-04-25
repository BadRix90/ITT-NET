# Erstelle eine neue datenbank
# exit(1): Verbindungsfehler
# exit(1): Ausführungsfehler
# DB-Modul einbinden
import mysql.connector

# Verbindung zum DB-Server herstellen
try:
    conn = mysql.connector.connect(user="root",
                                   host="localhost")
except mysql.connector.Error as e:
    print(f"Verbindung konnte nicht hergestellt werden: {e}")
    exit(1)

# DB-Cursor-Objekt bereitstellen
cur = conn.cursor()

# SQL-Anweisung zum Erstellen der DB ausführen
# CREATE DATABASE schule_neu
try:
    cur.execute("CREATE DATABASE Schule3")
except mysql.connector.Error as e:
    print(f"Fehler bei der Ausführung der SQL-Anweisung: {e}")
    exit(2)

# Verbindung zum DB-Server herstellen
conn.close()
