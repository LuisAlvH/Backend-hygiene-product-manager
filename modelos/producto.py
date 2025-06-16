class Producto:
    def __init__(self,  nombre, marca, precio_venta, cantidad_producto, stock_minimo ,id_producto=None):
        self._nombre = nombre
        self._marca = marca
        self._precio_venta = precio_venta
        self._cantidad_producto = cantidad_producto
        self._stock_minimo = stock_minimo
        self._id_producto = id_producto

    # Getter y Setter para id_producto
    def get_id_producto(self):
        return self._id_producto

    def set_id_producto(self, id_producto):
        self._id_producto = id_producto

    # Getter y Setter para nombre
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    # Getter y Setter para marca
    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    # Getter y Setter para precio_venta
    def get_precio_venta(self):
        return self._precio_venta

    def set_precio_venta(self, precio_venta):
        self._precio_venta = precio_venta

    # Getter y Setter para cantidad_producto
    def get_cantidad_producto(self):
        return self._cantidad_producto

    def set_cantidad_producto(self, cantidad_producto):
        self._cantidad_producto = cantidad_producto

    # Getter y Setter para stock_minimo
    def get_stock_minimo(self):
        return self._stock_minimo

    def set_stock_minimo(self, stock_minimo):
        self._stock_minimo = stock_minimo
