# LashStock gRPC

Sistema distribuido de gestión de inventario para lashistas desarrollado con Python, gRPC, Protocol Buffers y MongoDB.

## Descripción

LashStock gRPC es una aplicación distribuida que permite administrar productos utilizados en servicios profesionales de extensiones de pestañas.

El sistema implementa operaciones CRUD mediante llamadas remotas gRPC, permitiendo registrar, consultar, actualizar y eliminar productos almacenados en una base de datos MongoDB.

Este proyecto fue desarrollado como práctica de la materia Arquitectura de Software.

---

## Arquitectura del Sistema

```text
Postman / Cliente gRPC
        ↓
Servidor gRPC (Python)
        ↓
MongoDB
```

El cliente realiza solicitudes remotas utilizando gRPC.

El servidor procesa las peticiones y ejecuta las operaciones correspondientes sobre MongoDB.

La persistencia de la información se mantiene en una base de datos NoSQL MongoDB.

---

## Tecnologías Utilizadas

- Python 3.9
- gRPC
- Protocol Buffers
- MongoDB
- PyMongo
- Postman
- Git
- GitHub
- Visual Studio Code

---

## Estructura del Proyecto

```text
LashStock-gRPC/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   └── server.py
│
├── generated/
│   ├── productos_pb2.py
│   └── productos_pb2_grpc.py
│
├── proto/
│   └── productos.proto
│
├── docs/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Operaciones CRUD Implementadas

El servicio ProductoService implementa las siguientes operaciones remotas:

### CrearProducto

Permite registrar nuevos productos dentro del inventario.

### ObtenerProducto

Permite consultar un producto específico mediante su identificador.

### ListarProductos

Obtiene la lista completa de productos almacenados.

### ActualizarProducto

Modifica la información de un producto existente.

### EliminarProducto

Elimina un producto de la base de datos.

---

## Archivo Protocol Buffers

El contrato de comunicación se encuentra definido en:

```text
proto/productos.proto
```

Este archivo contiene:

- Definición de mensajes
- Definición de servicios
- Operaciones CRUD
- Estructura de intercambio de datos

---

## Base de Datos

Base de datos utilizada:

```text
lashstock_db
```

Colección principal:

```text
productos
```

MongoDB es utilizado como motor de persistencia para almacenar la información de los productos.

---

## Ejecución del Proyecto

### Activar entorno virtual

```bash
source venv/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Iniciar MongoDB

```bash
brew services start mongodb/brew/mongodb-community
```

### Ejecutar servidor gRPC

```bash
cd app
python server.py
```

Servidor:

```text
localhost:50051
```

---

## Pruebas

Las pruebas fueron realizadas mediante Postman utilizando soporte nativo para gRPC.

Archivo utilizado:

```text
proto/productos.proto
```

Operaciones verificadas:

- CrearProducto
- ObtenerProducto
- ListarProductos
- ActualizarProducto
- EliminarProducto

---

## Repositorio GitHub

Repositorio oficial del proyecto:

```text
https://github.com/StefyFerrer/LashStock-gRPC
```

---

## Autora

Estefanía Ferrer Espinoza

Carrera: Desarrollo de Software

Materia: Arquitectura de Software

Centro de Enseñanza Técnica Industrial (CETI)

---

## Conclusión

Se desarrolló exitosamente un sistema distribuido basado en gRPC y MongoDB para la gestión de inventario de productos utilizados por lashistas.

Durante el desarrollo se implementaron y validaron las operaciones CRUD mediante pruebas realizadas en Postman, comprobando la correcta comunicación entre cliente y servidor, así como la persistencia de la información dentro de MongoDB.

El proyecto permitió aplicar conceptos relacionados con arquitecturas distribuidas, Protocol Buffers, servicios remotos y bases de datos NoSQL, fortaleciendo las competencias adquiridas durante la materia de Arquitectura de Software.