import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
dbpassword = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")

def dbInit():
    conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=dbpassword,
            host=host,
            port=port
            )
    cursor = conn.cursor()

    cursor.execute("SELECT to_regclass('public.main')")
    result = cursor.fetchone()
    if result[0] != None:
        pass
    else:
        cursor.execute("CREATE TABLE main (user_id TEXT PRIMARY KEY, mugs INT, sorry_count INT, jailed INT)")
        conn.commit()
    cursor.close()
    conn.close()

def getRows(user_id):
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=dbpassword,
        host=host,
        port=port
        )
    c = conn.cursor()
    
    c.execute("SELECT * FROM main WHERE user_id=%s", (str(user_id),))
    data=c.fetchall()
    c.close()
    conn.close()
    return data


def getMugs(user_id):
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=dbpassword,
        host=host,
        port=port
        )
    c = conn.cursor()
    
    c.execute("SELECT mugs FROM main WHERE user_id=%s", (str(user_id),))
    data=c.fetchone()
    c.close()
    conn.close()
    return data

def initUser(user_id):
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=dbpassword,
        host=host,
        port=port
        )
    c = conn.cursor()
    c.execute("INSERT INTO main VALUES (%s,0,0,0)", (str(user_id),))
    conn.commit()
    c.close()
    conn.close()

def initUserMugs(user_id):
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=dbpassword,
        host=host,
        port=port
        )
    c = conn.cursor()
    c.execute("INSERT INTO main VALUES (%s,1,0,0)", (str(user_id),))
    conn.commit()
    c.close()
    conn.close()

def initUserJail(user_id):
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=dbpassword,
        host=host,
        port=port
        )
    c = conn.cursor()
    c.execute("INSERT INTO main VALUES (%s,0,0,1)", (str(user_id),))
    conn.commit()
    c.close()
    conn.close()

def addMugs(user_id):
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=dbpassword,
        host=host,
        port=port
        )
    c = conn.cursor()
    c.execute("SELECT mugs FROM main WHERE user_id=%s", (str(user_id),))
    mugs=c.fetchone()
    newMugs = mugs[0] + 1
    c.execute("UPDATE main SET mugs = %s WHERE user_id = %s", (newMugs, str(user_id)))
    conn.commit()
    c.close()
    conn.close()

def jailUser(user_id):
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=dbpassword,
        host=host,
        port=port
        )
    c = conn.cursor()
    c.execute("UPDATE main SET jailed = %s WHERE user_id = %s", (1, str(user_id)))
    conn.commit()
    c.close()
    conn.close()

def getJailed(user_id):
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=dbpassword,
        host=host,
        port=port
        )
    c = conn.cursor()
    
    c.execute("SELECT jailed FROM main WHERE user_id = %s", (str(user_id),))
    data=c.fetchone()
    c.close()
    conn.close()
    return data

def updateSorryCount(user_id):
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=dbpassword,
        host=host,
        port=port
        )
    c = conn.cursor()
    c.execute("SELECT sorry_count FROM main WHERE user_id = %s", (str(user_id),))
    sorry_count=c.fetchone()
    new_sorry_count = sorry_count[0] + 1
    c.execute("UPDATE main SET sorry_count = %s WHERE user_id = %s", (new_sorry_count, str(user_id)))
    conn.commit()
    c.close()
    conn.close()

def getSorryCount(user_id):
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=dbpassword,
        host=host,
        port=port
        )
    c = conn.cursor()
    c.execute("SELECT sorry_count FROM main WHERE user_id = %s", (str(user_id),))
    sorry_count=c.fetchone()
    c.close()
    conn.close()
    return sorry_count

def resetSorryCount(user_id):
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=dbpassword,
        host=host,
        port=port
        )
    c = conn.cursor()
    c.execute("UPDATE main SET sorry_count = %s WHERE user_id = %s", (0, str(user_id)))
    conn.commit()
    c.close()
    conn.close()

def setUserFree(user_id):
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=dbpassword,
        host=host,
        port=port
        )
    c = conn.cursor()
    c.execute("UPDATE main SET jailed = %s WHERE user_id = %s", (0, str(user_id)))
    conn.commit()
    c.close()
    conn.close()