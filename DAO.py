from datetime import datetime
import pymysql

import pymysql


#Variablen initialisieren

IP_ADDRESS = "192.168.137.140"
LOGIN = "gast"
PASSWORD = "SECRET"
DB = "users"
raum = "9-108"


db = pymysql.connect(IP_ADDRESS, LOGIN, PASSWORD, DB)
cursor = db.cursor()


def read_prof(prof_id):
    cursor.execute("SELECT * FROM user where id=%s", [prof_id])
    records = cursor.fetchall()
    for row in records:
        return row[0]
    return 0;


def create_vorlesung(prof_id, lec_name):
    cursor.execute("INSERT INTO vorlesung (name, profID, raum) VALUES (name=%s, profID=%s, raum=%s)", [lec_name, prof_id, raum])
    return 0;

def update_vorlesung(vorlesungs_ID):
    cursor.execute("UPDATE vorlesung SET (endDatum = datetime.now()) WHERE id=%s", [vorlesungs_ID])
    return 0;

def get_prof_name(prof_ID):
    cursor.execute("SELECT * FROM user where id=%s", prof_ID)
    records = cursor.fetchall()
    for row in records:
        return row[1]
    return 0;

def get_vorlesungen(prof_ID):
    cursor.execute("SELECT * FROM Vorlesung WHERE id=%s", [prof_ID])
    return cursor.fetchall()
    return 0;

def get_bewertungen(vorlesungs_ID):
    cursor.execute("SELECT * FROM Bewertung WHERE id=%s", [vorlesungs_ID])
    return cursor.fetchall()
    return 0;

def post_bewertung(wert, vorlesungs_ID):
    cursor.execute("INSERT INTO bewertung (wert) VALUES (wert=%s) WHERE id=%s", [wert, vorlesungs_ID])
    return 0;
