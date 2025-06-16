class Venta:
    def __init__(self, total_venta, codigo_factura, fk_usuario,id_venta=None ,fecha_venta=None):
        self._total_venta = total_venta
        self._codigo_factura = codigo_factura
        self._fk_usuario = fk_usuario
        self._id_venta = id_venta
        self._fecha_venta = fecha_venta

    # Getters
    def get_id_venta(self):
        return self._id_venta

    def get_total_venta(self):
        return self._total_venta

    def get_codigo_factura(self):
        return self._codigo_factura

    def get_fk_usuario(self):
        return self._fk_usuario
    def get_fecha_venta(self):
        return self._fecha_venta
    
    # Setters
    def set_id_venta(self, id_venta):
        self._id_venta = id_venta

    def set_total_venta(self, total_venta):
        self._total_venta = total_venta

    def set_codigo_factura(self, codigo_factura):
        self._codigo_factura = codigo_factura

    def set_fk_usuario(self, fk_usuario):
        self._fk_usuario = fk_usuario
    def set_fecha_venta(self, fecha_venta):
        self._fecha_venta = fecha_venta