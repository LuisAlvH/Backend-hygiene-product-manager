from db import get_db
from modelos.venta import Venta
def getSales():
    db = get_db()
    return db.execute('SELECT * FROM ventas').fetchall()




def addSale(venta):  
    db = get_db()
    cursor = db.execute(
        'INSERT INTO ventas (total_venta, codigo_factura, fk_usuario) VALUES (?,?,?)', 
        (venta.get_total_venta(), venta.get_codigo_factura(),venta.get_fk_usuario())
    )
    db.commit()

    return cursor.lastrowid  


