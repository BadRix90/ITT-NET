# Erstellen einer neuen Tabelle in der DB schule3
# exit(1): Verbindungsfehler
# exit(1): Ausführungsfehler
# DB-Modul einbinden
import mysql.connector

# Verbindung zum DB-Server herstellen
try:
    conn = mysql.connector.connect(user="root",
                                   database="schule3",
                                   host="localhost",
                                   )
except mysql.connector.Error as e:
    print(f"Verbindung konnte nicht hergestellt werden: {e}")
    exit(1)

# DB-Cursor-Objekt bereitstellen
cur = conn.cursor()

# SQL-Anweisung zum Erstellen einer neuen Tabelle Klasse B ausführen
# CREATE TABLE klasse (id INTEGER PRIMARY KEY AUTO_INCREMENT,
#                      name VARCHAR(10) NOT NULL,
#                      klassenlehrer_id INTEGER NOT NULL)
sql_create_table = "CREATE TABLE klasse ("\
                    "id INTEGER PRIMARY KEY AUTO_INCREMENT," \
                    "name VARCHAR(10) NOT NULL, " \
                    "klassenlehrer_id INTEGER NOT NULL)"
try:
    cur.execute(sql_create_table)
except mysql.connector.Error as e:
    print(f"Fehler bei der Ausführung der SQL-Anweisung: {e}")
    exit(2)

# Verbindung zum DB-Server herstellen
conn.close()
