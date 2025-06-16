from db import get_db
from modelos.usuario import Usuario

def getUsers():
    db = get_db()
    return db.execute('SELECT * FROM usuarios').fetchall()

def addUser(usuario):  
    db = get_db()
    db.execute(
        'INSERT INTO usuarios (nombre, username, password,email,role) VALUES (?, ?,?,?,?)', 
        (usuario.get_nombre(), usuario.get_email(),usuario.get_password(),usuario.get_email(),usuario.get_role())
    )
    db.commit()

     
def updateUser(usuario):
    db = get_db()
    db.execute(
        '''
        UPDATE usuarios
        SET nombre = ?, username = ?, password = ?, email = ?, role = ?
        WHERE id = ?
        ''',
        (
            usuario.get_nombre(),
            usuario.get_username(),
            usuario.get_password(),
            usuario.get_email(),
            usuario.get_role(),
            usuario.get_id()
        )
    )
    db.commit()



def deleteUser(usuario_id):
    db = get_db()
    db.execute(
        'DELETE FROM usuarios WHERE id = ?',
        (usuario_id,)
    )
    db.commit()

    