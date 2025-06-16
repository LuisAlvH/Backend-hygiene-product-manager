import sqlite3


def init_db():
    conex = sqlite3.connect('DbCleanSa.db')
    cursor = conex.cursor()

    # Crear tabla usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            role TEXT NOT NULL,
            fecha_creacion TEXT NOT NULL DEFAULT (datetime('now'))
            
        )
    ''')

    

    # Crear tabla Ventas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas (
            id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
            total_venta REAL NO NULL,
            fecha_venta TEXT NOT NULL DEFAULT (datetime('now')),
            codigo_factura TEXT NOT NULL,
            fk_usuario INTEGER NOT NULL,
            FOREIGN KEY (fk_usuario) REFERENCES usuarios(id_usuario)
            
        )
    ''')

     # Crear tabla Productos

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NO NULL,
            marca TEXT NO NULL,
            precio_venta REAL NOT NULL,
            stock_minimo INTEGER NOT NULL DEFAULT 5,
            cantidad_producto INTEGER NOT NULL 
            
        )
    ''')


      # Crear tabla Alertas

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alertas (
            id_alerta INTEGER PRIMARY KEY AUTOINCREMENT,
            stock_actual INTEGER NO NULL,
            estado_alerta TEXT NO NULL,
            fk_producto  INTEGER NOT NULL,
            fecha_alerta TEXT NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (fk_producto) REFERENCES productos(id_producto)
        )
    ''')
      # Crear tabla Detalle Venta

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS detalles_ventas (
            id_detalle_venta INTEGER PRIMARY KEY AUTOINCREMENT,
            cantidad INTEGER NO NULL,
            precio_unitario REAL NO NULL,
            subtotal  REAL NOT NULL,
            fk_venta INTEGER NOT NULL,
            fk_producto  INTEGER NOT NULL,
            FOREIGN KEY (fk_venta) REFERENCES ventas(id_venta),
            FOREIGN KEY (fk_producto) REFERENCES productos(id_producto)
        )
    ''')


    cursor.execute('''
        INSERT INTO usuarios (nombre, username, password, email, role)
        VALUES 
            ('admin', 'admin', '1234', 'juanp@example.com', 'admin'),
            ('usuario', 'usuario', '1234', 'mariag@example.com', 'usuario'),
            ('usuario2', 'usuario2', '1234', 'carlosd@example.com', 'usuario')
    ''')


    cursor.execute('''
INSERT INTO productos (nombre, marca, precio_venta, cantidad_producto) VALUES
('Jabón Líquido', 'Marca X', 100.00, 40),
('Shampoo', 'Marca Y', 250.00, 30),
('Pasta Dental', 'Marca Z', 90.50, 50),
('Desodorante', 'Marca W', 120.00, 35),
('Cepillo de Dientes', 'Marca V', 75.00, 45),
('Toallas Húmedas', 'Marca U', 60.00, 60),
('Crema Corporal', 'Marca T', 180.00, 25),
('Gel Antibacterial', 'Marca S', 140.00, 40),
('Jabón en Barra', 'Marca R', 85.00, 50),
('Enjuague Bucal', 'Marca Q', 110.00, 30)
''')

    

 # Triger actualizar stock

    cursor.execute("""
    CREATE TRIGGER trg_actualizar_stock
    AFTER INSERT ON detalles_ventas
    FOR EACH ROW
    BEGIN
        UPDATE productos
        SET cantidad_producto = cantidad_producto - NEW.cantidad
        WHERE id_producto = NEW.fk_producto;
    END;
    """)
# Alerta Stock bajo

    cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS trg_alerta_stock
    AFTER UPDATE ON productos
    FOR EACH ROW
    WHEN NEW.cantidad_producto <= NEW.stock_minimo
    BEGIN
        INSERT INTO alertas (stock_actual, estado_alerta, fk_producto)
        VALUES (
            NEW.cantidad_producto,
            CASE
                WHEN NEW.cantidad_producto = 0 THEN 'SIN STOCK'
                ELSE 'STOCK BAJO'
            END,
            NEW.id_producto
        );
    END;
""")


    

    


    conex.commit()
    conex.close()
    print("Base de datos creada correctamente.")



if __name__ == '__main__':
    init_db()

    # ejecutar python init_db.py
