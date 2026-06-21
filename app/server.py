import sys
import os
from concurrent import futures

import grpc
from bson import ObjectId

sys.path.append(os.path.join(os.path.dirname(__file__), "../generated"))

import productos_pb2
import productos_pb2_grpc

from database import productos_collection


class ProductoService(productos_pb2_grpc.ProductoServiceServicer):

    def CrearProducto(self, request, context):
        producto = {
            "nombre": request.nombre,
            "categoria": request.categoria,
            "marca": request.marca,
            "precio": request.precio,
            "stock": request.stock,
            "descripcion": request.descripcion
        }

        resultado = productos_collection.insert_one(producto)

        return productos_pb2.ProductoResponse(
            mensaje=f"Producto creado correctamente con ID: {resultado.inserted_id}"
        )

    def ObtenerProducto(self, request, context):
        producto = productos_collection.find_one({"_id": ObjectId(request.id)})

        if not producto:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Producto no encontrado")
            return productos_pb2.Producto()

        return productos_pb2.Producto(
            id=str(producto["_id"]),
            nombre=producto["nombre"],
            categoria=producto["categoria"],
            marca=producto["marca"],
            precio=producto["precio"],
            stock=producto["stock"],
            descripcion=producto["descripcion"]
        )

    def ListarProductos(self, request, context):
        productos = []

        for producto in productos_collection.find():
            productos.append(
                productos_pb2.Producto(
                    id=str(producto["_id"]),
                    nombre=producto["nombre"],
                    categoria=producto["categoria"],
                    marca=producto["marca"],
                    precio=producto["precio"],
                    stock=producto["stock"],
                    descripcion=producto["descripcion"]
                )
            )

        return productos_pb2.ListaProductos(productos=productos)

    def ActualizarProducto(self, request, context):
        resultado = productos_collection.update_one(
            {"_id": ObjectId(request.id)},
            {
                "$set": {
                    "nombre": request.nombre,
                    "categoria": request.categoria,
                    "marca": request.marca,
                    "precio": request.precio,
                    "stock": request.stock,
                    "descripcion": request.descripcion
                }
            }
        )

        if resultado.matched_count == 0:
            return productos_pb2.ProductoResponse(
                mensaje="Producto no encontrado"
            )

        return productos_pb2.ProductoResponse(
            mensaje="Producto actualizado correctamente"
        )

    def EliminarProducto(self, request, context):
        resultado = productos_collection.delete_one({"_id": ObjectId(request.id)})

        if resultado.deleted_count == 0:
            return productos_pb2.ProductoResponse(
                mensaje="Producto no encontrado"
            )

        return productos_pb2.ProductoResponse(
            mensaje="Producto eliminado correctamente"
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    productos_pb2_grpc.add_ProductoServiceServicer_to_server(
        ProductoService(), server
    )

    server.add_insecure_port("[::]:50051")
    server.start()

    print("Servidor gRPC de LashStock iniciado en el puerto 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()