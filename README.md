
## 📊 TP Final – Mini Data Warehouse & Dashboard Comercial
## 👩‍💻 Carrera: Lic. en Ciencia de Datos
## 🧠 Materia: Introducción al Marketing Online y Negocios Digitales
## 📂 Proyecto: Ecosistema de datos EcoBottle AR
### 📝 Introducción

Este proyecto implementa un **mini-ecosistema de datos comercial (online + offline)** para la empresa ficticia EcoBottle AR.
El objetivo fue construir un Data Warehouse (DW) modelado en estrella y un **Dashboard**, siguiendo las mejores prácticas vistas en clase.

Se trabajó con datos RAW provistos en archivos .csv, los cuales fueron transformados mediante scripts en Python para crear tablas dimensión y de hechos, almacenadas en la carpeta DW/.


---

### 🎯 Objetivos del Proyecto

Según la consigna del TP, se debían cumplir los siguientes puntos:

| # | Tarea                                               | 
| - | --------------------------------------------------- | 
| 1 | Modelado estrella con todas las tablas              | 
| 2 | Transformación de datos RAW a DW                    | 
| 3 | Scripts Python para generar dimensiones y hechos    | 
| 4 | Script `main.py` para ejecutar todo                 | 
| 5 | Dashboard conectado al DW                           | 
| 6 | Entrega con README + requirements + entorno virtual | 

KPIs implementados en el dashboard:

✅ Ventas totales
✅ Ticket promedio
✅ Usuarios activos
✅ NPS
✅ Ventas por provincia
✅ Ranking mensual por producto

---
### 🧠 Caso de estudio: EcoBottle AR

EcoBottle AR vende botellas reutilizables online y en tiendas físicas.
Marketing genera tráfico vía redes sociales y email, y se envía NPS post-compra.

Los datos incluyen:

 Ventas y líneas de pedido
 Clientes
 Tiendas
 Sesiones web
 Pagos
 Envíos
 Encuestas NPS

### 🏗️ Arquitectura del Proyecto
  ```bash
MKT_TP_FINAL/
├── raw/                
├── DW/                  
├── esquemas/           
├── venv/               
├── *.py               
│   ├── DimCanal.py
│   ├── DimCliente.py
│   ├── DimProducto.py
│   ├── DimTiempo.py
│   ├── DimTienda.py
│   ├── DimUbicacion.py
│   ├── FactNPS.py
│   ├── FactActividades.py
│   ├── FactSalesOrder.py
│   ├── FactSalesOrderItem.py
│   └── main.py         
├── requirements.txt
└── README.md
 ```

### ⚙️ Estructura del Repositorio

| Carpeta | Contenido |
| :--- | :--- |
| **`RAW/`** | Datos fuente originales en formato `.CSV` (ventas, clientes, sesiones, etc.). |
| **`src/`** | Scripts de Python (`.py`) para la lógica de **ETL (Extract, Transform, Load)**. |
| **`DW/`** | Archivos de salida `.CSV` que representan el **Data Warehouse** (Tablas de Hechos y Dimensiones). |
| **`Esquemas/`** | Diagramas del Modelo Estrella (FactVentas, FactActividad, FactNPS). |
| **`venv/`** | Entorno virtual de Python (buenas prácticas). |
| **`requirements.txt`**| Dependencias necesarias para ejecutar los scripts (principalmente `pandas`). |

---
### ⭐ Modelado Estrella
## Dimensiones creadas

| Dimensión    | Contenido                       |
| ------------ | ------------------------------- |
| DimCliente   | Info del cliente                |
| DimProducto  | SKU, nombre, categoría          |
| DimUbicacion | Provincias y direcciones        |
| DimCanal     | Canal de venta (online/offline) |
| DimTienda    | Tiendas físicas                 |
| DimTiempo    | Año, mes, día                   |

## Hechos creados

| Hecho                | KPI                         | Fuente           |
| -------------------- | --------------------------- | ---------------- |
| FactSales_Order      | Ventas                      | sales_order      |
| FactSales_Order_Item | Detalle y ranking productos | sales_order_item |
| FactNPS              | NPS                         | nps_response     |
| FactActividades      | Usuarios activos            | web_session      |


Esquemas en /esquemas/.

## 🚀 Guía de Ejecución

Sigue estos pasos para levantar el entorno y procesar los datos:

### 1. Preparación del Entorno (Consola)

Asegúrate de estar en la carpeta raíz del proyecto (`mkt_tp_final`) y ejecuta:

1.  **Activar Entorno Virtual:**
    ```bash
    # Windows (PowerShell)
    .\venv\Scripts\Activate
    # Mac/Linux
    source venv/bin/activate
    ```
2.  **Instalar Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

### 2. Ejecución del Proceso ETL (Consola)

Una vez activo el entorno, ejecuta los scripts de transformación en el orden correcto (Dimensiones antes que Hechos):

```bash
    python main.py
```
#### Esto
lee los archivos de raw/, 
transforma los datos y
guarda las tablas en DW/

# 📊 Dashboard Power BI

### Fuentes

Conectado directamente a los archivos .csv de la carpeta DW/.

### Dashboard




