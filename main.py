import os
import subprocess

scripts = [
    "DimCanal.py",
    "DimCliente.py",
    "DimProducto.py",
    "DimTiempo.py",
    "DimUbicacion.py",
    "DimTienda.py",
    "FactActividades.py",
    "FactNPS.py",
    "Factsalesorder.py",
    "Factsalesorderitem.py",
    "Factpayment.py",
    "Factshipment.py"
]

print("Iniciando ejecución del Data Warehouse...")

for script in scripts:
    print(f"🔹 Ejecutando {script} ...")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f" Error al ejecutar {script}:")
        print(result.stderr)

print("  ¡Ejecución completa! Todos los archivos fueron procesados.")
