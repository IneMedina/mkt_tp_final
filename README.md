# 📊 Proyecto Data Warehouse: EcoBottle AR
### Introducción al Marketing Online y los Negocios Digitales

Este proyecto se enfoca en el diseño e implementación de un **mini-ecosistema de datos comercial (online + offline)**, utilizando el modelado dimensional (Kimball) y Python, con el objetivo de construir un **Dashboard en Looker Studio** para el área comercial de EcoBottle AR.

---

## 🎯 Objetivos del Proyecto

[cite_start]El ecosistema de datos está diseñado para monitorear los siguientes KPIs clave[cite: 6]:

* **Ventas** ($M) y **Ticket Promedio** ($K).
* **Usuarios Activos** (nK).
* [cite_start]**NPS** (Net Promoter Score)[cite: 6].
* [cite_start]**Ventas por Provincia**[cite: 6].
* [cite_start]**Ranking Mensual por Producto**[cite: 6].

> [cite_start]🚀 **Meta del Trimestre:** Crecer 15% en ventas en Córdoba y reducir los tiempos de entrega en Mendoza[cite: 56].

---

## ⚙️ Estructura del Repositorio

| Carpeta | Contenido |
| :--- | :--- |
| **`RAW/`** | [cite_start]Datos fuente originales en formato `.CSV` (ventas, clientes, sesiones, etc.)[cite: 15]. |
| **`src/`** | Scripts de Python (`.py`) para la lógica de **ETL (Extract, Transform, Load)**. |
| **`DW/`** | Archivos de salida `.CSV` que representan el **Data Warehouse** (Tablas de Hechos y Dimensiones). |
| **`Esquemas/`** | Diagramas del Modelo Estrella (FactVentas, FactActividad, FactNPS). |
| **`venv/`** | Entorno virtual de Python (buenas prácticas). |
| **`requirements.txt`**| [cite_start]Dependencias necesarias para ejecutar los scripts (principalmente `pandas`)[cite: 38]. |

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

python src/dim_loader.py

python src/fact_ventas.py


python src/fact_actividad.py
python src/fact_nps.py