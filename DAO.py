IP_ADDRESS = "localhost"
LOGIN = "admin"
PASSWORD = "1234"
PROF_TABLE = "users"
VORLESUNG_TABLE = "Vorlesung"
BEWERTUNGEN_TABLE = "Bewertung"
raum = "9-108"

PROF_db = pymysql.connect(IP_ADDRESS, LOGIN, PASSWORD, PROF_TABLE)
PROF_cursor = PROF_db.cursor()

VORLESUNG_db = pymysql.connect(IP_ADDRESS, LOGIN, PASSWORD, VORLESUNG_TABLE)
VORLESUNG_cursor = VORLESUNG_db.cursor()

BEWERTUNG_db = pymysql.connect(IP_ADDRESS, LOGIN, PASSWORD, BEWERTUNGEN_TABLE)
BEWERTUNG_cursor = BEWERTUNG_db.cursor()


def read_prof(prof_id):
    PROF_cursor.execute("SELECT * FROM user where name=%s", prof_name)
    records = PROF_cursor.fetchall()
    for row in records:
        return row[0]
    return 0;

def create_vorlesung(prof_id, lec_name):
        VORLESUNG_cursor.execute("INSERT INTO vorlesung (name, profID, raum) VALUES (name=%s, startDatum=%s, profID=%s, raum=%s)"[lec_name, prof_id, raum])
    return 0;

def update_vorlesung(vorlesungs_ID):
        VORLESUNG_cursor.execute("UPDATE vorlesung SET (endDatum = now()) WHERE id=%s", [vorlesungs_ID])
    return 0;

def get_prof_name(prof_ID):
    PROF_cursor.execute("SELECT * FROM user where id=%s", prof_ID)
    records = PROF_cursor.fetchall()
    for row in records:
        return row[1]
    return 0;

def get_vorlesungen(prof_ID):
    PROF_cursor.execute("SELECT * FROM Vorlesung WHERE id=%s", [prof_ID])
    return PROF_cursor.fetchall()

    return 0;

def get_bewertungen(vorlesungs_ID):
    PROF_cursor.execute("SELECT * FROM Bewertung WHERE id=%s", [vorlesungs_ID])
    return PROF_cursor.fetchall()

    return 0;

def post_bewertung(wert, vorlesungs_ID):
    VORLESUNG_cursor.execute("INSERT INTO bewertung (wert) VALUES (wert=%s) WHERE id=%s",[wert, vorlesungs_ID])
    return 0;
