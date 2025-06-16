from db import get_db


def addSaleDetail(detalle):  
    db = get_db()
    cursor = db.execute(
        'INSERT INTO detalles_ventas (cantidad, precio_unitario, subtotal, fk_venta, fk_producto) VALUES (?, ?, ?, ?, ?)',
        (detalle["cantidad"], detalle["precio_unitario"], detalle["subtotal"], detalle["fk_venta"], detalle["fk_producto"]) 
    )
    db.commit()
    return cursor.lastrowid  