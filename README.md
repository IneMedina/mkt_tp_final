# 📊 Proyecto Data Warehouse: EcoBottle AR
### Introducción al Marketing Online y los Negocios Digitales

Este proyecto se enfoca en el diseño e implementación de un **mini-ecosistema de datos comercial (online + offline)**, utilizando el modelado dimensional (Kimball) y Python, con el objetivo de construir un **Dashboard en Looker Studio** para el área comercial de EcoBottle AR.

---

## 🎯 Objetivos del Proyecto

El ecosistema de datos está diseñado para monitorear los siguientes KPIs clave:

* **Ventas** ($M) y **Ticket Promedio** ($K).
* **Usuarios Activos** (nK).
* **NPS** (Net Promoter Score).
* **Ventas por Provincia**.
* **Ranking Mensual por Producto**.

.

---

## ⚙️ Estructura del Repositorio

| Carpeta | Contenido |
| :--- | :--- |
| **`RAW/`** | Datos fuente originales en formato `.CSV` (ventas, clientes, sesiones, etc.). |
| **`src/`** | Scripts de Python (`.py`) para la lógica de **ETL (Extract, Transform, Load)**. |
| **`DW/`** | Archivos de salida `.CSV` que representan el **Data Warehouse** (Tablas de Hechos y Dimensiones). |
| **`Esquemas/`** | Diagramas del Modelo Estrella (FactVentas, FactActividad, FactNPS). |
| **`venv/`** | Entorno virtual de Python (buenas prácticas). |
| **`requirements.txt`**| Dependencias necesarias para ejecutar los scripts (principalmente `pandas`). |

---

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
# 1. Cargar y transformar todas las Dimensiones (Tiempo, Cliente, Producto, etc.)
python src/dim_loader.py
# 2. Construir FactVentas
python src/fact_ventas.py
# 3. Construir FactActividad
python src/fact_actividad.py
# 4. Construir FactNPS
python src/fact_nps.py

## 📂 Estructura del proyecto

```bash
mkt_tp_final/
├── rAW/                      
├── DW/    
├── Esquemas                   
├── DimCliente.py
├── DimProducto.py
├── DimCanal.py
├── DimUbicacion.py
├── DimTiempo.py
├── Fact_Ventas.py
├── Fact_Actividad.py
├── Fact_NPS.py
├── requirements.txt
├── README.md
└── assets/
