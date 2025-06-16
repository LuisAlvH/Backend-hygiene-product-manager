from db import get_db


def getAlerts():
    db = get_db()
    return db.execute('SELECT * FROM alertas').fetchall()
