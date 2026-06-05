import os
import pandas as pd
from faker import Faker
from typing import Tuple

def process_massive_inventory(output_path_csv: str) -> Tuple[bool, str]:
    """
    Genera un inventario masivo con Faker, lo procesa con Pandas
    y lo exporta a formatos CSV y Excel (usando openpyxl de fondo).
    """
    try:
        # Inicializamos Faker para generar datos aleatorios realistas
        fake = Faker()
        
        # Definimos las rutas para ambos formatos
        output_path_excel = output_path_csv.replace(".csv", ".xlsx")
        
        # 1. Generamos 100 filas de datos 100% realistas usando Faker en un bucle
        ids = [f"DEV-{i:03d}" for i in range(1, 101)]
        tipos = [fake.random_element(elements=("Servidor", "Router", "Switch", "Firewall")) for _ in range(100)]
        rams = [fake.random_element(elements=(8, 16, 32, 64, 128)) for _ in range(100)]
        estados = [fake.random_element(elements=("Activo", "Mantenimiento", "Inactivo")) for _ in range(100)]
        
        datos_inventario = {
            "ID": ids,
            "Tipo": tipos,
            "RAM_GB": rams,
            "Estado": estados
        }
        
        # 2. Creamos el DataFrame de Pandas
        df = pd.DataFrame(datos_inventario)
        
        # Aseguramos que la carpeta data/ exista
        os.makedirs(os.path.dirname(output_path_csv), exist_ok=True)
        
        # 3. Exportamos a CSV
        df.to_csv(output_path_csv, index=False, encoding="utf-8")
        
        # 4. Exportamos a Excel (aquí es donde Python usa openpyxl de forma automática por debajo)
        df.to_excel(output_path_excel, index=False)
        
        # 5. Análisis estadístico con Pandas
        total_equipos = int(df.shape[0])
        conteo_estados = df["Estado"].value_counts().to_dict()
        promedio_ram = float(df["RAM_GB"].mean())
        
        reporte = (
            f"✅ ¡Archivos de inventario generados con éxito!\n"
            f"   📁 CSV:   {output_path_csv}\n"
            f"   📁 Excel: {output_path_excel}\n"
            f"📊 Resumen del análisis de datos con Pandas & Faker:\n"
            f" 🏢 Total de dispositivos inventariados: {total_equipos} equipos creados aleatoriamente.\n"
            f" 🧠 Capacidad promedio de memoria RAM: {promedio_ram:.2f} GB.\n"
            f" 🛠️  Desglose por estado de operación:\n"
            f"    - Activos: {conteo_estados.get('Activo', 0)}\n"
            f"    - En Mantenimiento: {conteo_estados.get('Mantenimiento', 0)}\n"
            f"    - Inactivos: {conteo_estados.get('Inactivo', 0)}"
        )
        
        return True, reporte
        
    except Exception as e:
        return False, f"❌ Error en el procesamiento de datos masivos: {str(e)}"