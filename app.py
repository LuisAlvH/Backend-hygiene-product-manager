
from flask import Flask, request, redirect,jsonify
from db import close_db
from flask_cors import CORS
from modelos.usuario import Usuario
from modelos.producto import Producto
from modelos.venta import Venta
from queries.queries_usuario import addUser,getUsers,updateUser,deleteUser
from queries.queries_producto import addProduct,getProduct,updateProduct,deleteProduct
from queries.queries_alerts import getAlerts
from queries.queries_detalles_ventas import addSaleDetail
from queries.queries_venta import addSale,getSales


import traceback
app=Flask(__name__)
CORS(app)

@app.teardown_appcontext
def cerrar_conexion(exception):
    close_db()
    
@app.route("/usuarios" ,methods=["GET"])
def listar_usuarios():
    usuarios = getUsers()

    resultado = [{
        "id": u["id_usuario"],
        "nombre": u["nombre"],
        "username": u["username"],
        "password": u["password"],
        "email": u["email"],
        "role": u["role"]
    } for u in usuarios]
    
    return jsonify(resultado)

@app.route("/productos", methods=["GET"])
def listar_productos():
    productos_data = getProduct()

    resultado = []
    for p in productos_data:
        p_dict = dict(p)  
        resultado.append({
            "id_producto": p_dict.get("id_producto"),
            "nombre": p_dict["nombre"],
            "marca": p_dict["marca"],
            "precio_venta": p_dict["precio_venta"],
            "cantidad_producto": p_dict["cantidad_producto"],
            "stock_minimo": p_dict["stock_minimo"]
        })

    return jsonify(resultado)

@app.route("/productos/<int:id_producto>", methods=["DELETE"])
def eliminar_producto(id_producto):
    try:
        filas_eliminadas = deleteProduct(id_producto)
        if filas_eliminadas == 0:
            return jsonify({"mensaje": "Producto no encontrado"}), 404
        return jsonify({"mensaje": "Producto eliminado correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/productos', methods=['POST'])
def agregar_producto():
    try:
        data = request.get_json()  
        nuevo_producto = Producto(
            nombre=data['nombre'],
            marca=data['marca'],
            precio_venta=data['precio_venta'],
            cantidad_producto=data['cantidad_producto'],
            stock_minimo=data['stock_minimo']
        )

        id_generado = addProduct(nuevo_producto)  

        return jsonify({"mensaje": "Producto agregado correctamente", "id": id_generado}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/productos/<int:id_producto>", methods=["PUT"])
def editar_producto(id_producto):
    try:
        data = request.get_json(force=True)
        required_fields = {"nombre", "marca", "precio_venta", "cantidad_producto", "stock_minimo"}

        if not required_fields.issubset(data):
            faltantes = required_fields - data.keys()
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(faltantes)}"}), 400

        producto_actualizado = Producto(
            id_producto=id_producto,  
            nombre=data["nombre"],
            marca=data["marca"],
            precio_venta=data["precio_venta"],
            cantidad_producto=data["cantidad_producto"],
            stock_minimo=data["stock_minimo"]
        )

        updateProduct(producto_actualizado)

        return jsonify({"mensaje": "Producto actualizado correctamente"}), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/ventas', methods=['POST'])
def agregar_venta():
    try:
        data = request.get_json()  

        nueva_venta=Venta(
                total_venta=data['total_venta'],
                codigo_factura=data['codigo_factura'],
                fk_usuario=data['fk_usuario']

        )

        id_generado=addSale(nueva_venta)

        return jsonify({"mensaje": "la venta se ha agregado correctamente", "id": id_generado}), 201
    except Exception as e:
        traceback.print_exc() 
        return jsonify({"error": str(e)}), 500

@app.route("/ventas", methods=["GET"])
def listar_ventas():
    dataSales = getSales()
    resultado = [dict(v) for v in dataSales]
    return jsonify(resultado)

@app.route("/detalle-venta", methods=["POST"])
def registrar_detalles_venta():
    data = request.get_json()
    if not data or not isinstance(data, list):
       
        return jsonify({"error": "Se esperaba un array de los detalles de la venta"}), 400

    ventas_procesadas = []

    for detalle in data:
        try:
            addSaleDetail(detalle)  
            ventas_procesadas.append(detalle)  
        except Exception as e:
            return jsonify({"error": f"Ocurrió un error al registrar una venta: {str(e)}"}), 500
  
    return jsonify({"mensaje": "Detalles de venta procesados correctamente", "ventas": ventas_procesadas})

@app.route("/alertas", methods=["GET"])
def listar_alertas():
    dataAlerts = getAlerts()
    resultado = [dict(v) for v in dataAlerts] 
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)







