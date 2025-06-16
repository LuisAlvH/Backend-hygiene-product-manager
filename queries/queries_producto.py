from db import get_db
from modelos.producto import Producto


def getProduct():
    db = get_db()
    return db.execute('SELECT * FROM productos').fetchall()

def addProduct(producto):  
    db = get_db()
    cursor = db.execute(
        'INSERT INTO productos (nombre, marca, precio_venta, cantidad_producto, stock_minimo) VALUES (?,?,?,?,?)',
       (producto.get_nombre(), producto.get_marca(), producto.get_precio_venta(), producto.get_cantidad_producto(), producto.get_stock_minimo())
    )
    db.commit()
    return cursor.lastrowid  # Retornás el ID generado



def updateProduct(producto):
    db = get_db()
    db.execute(
        '''
        UPDATE productos
        SET nombre = ?, marca = ?, precio_venta = ?, cantidad_producto = ?
        WHERE id_producto = ?
        ''',
        (
            producto.get_nombre(),
            producto.get_marca(),
            producto.get_precio_venta(),
            producto.get_cantidad_producto(),
            producto.get_id_producto()
        )
    )
    db.commit()


def deleteProduct(producto_id):
    db = get_db()
    cursor = db.execute(
        'DELETE FROM productos WHERE id_producto = ?',
        (producto_id,)
    )
    db.commit()
    return cursor.rowcount 
    