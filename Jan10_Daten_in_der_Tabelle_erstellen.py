# Erstellen in die Tabelle Klasse einfügen
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

# SQL-Anweisung zum einfügen eines Datensatzes ausführen
# INSERT INTO klasse (name, klassenlehrer_id) VALUES("8A", 2)
sql_insert_into_table = "INSERT INTO klasse (name, klassenlehrer_id) VALUES('9A',1), ('9B',2), ('9C',3), ('9D',4) "
try:
    cur.execute(sql_insert_into_table)
except mysql.connector.Error as e:
    print(f"Fehler bei der Ausführung der SQL-Anweisung: {e}")
    exit(2)
conn.commit()
# Verbindung zum DB-Server herstellen
conn.close()
