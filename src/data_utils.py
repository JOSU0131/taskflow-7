import os
import pandas as pd
from typing import Tuple

def process_massive_inventory(output_path: str) -> Tuple[bool, str]:
    """
    Genera un inventario masivo de dispositivos en un DataFrame de Pandas,
    lo exporta a un archivo CSV y luego demuestra cómo leerlo y analizarlo.
    Devuelve:
    - Un booleano indicando el éxito de la operación.
    - Un texto con el resumen estadístico de los datos procesados.
    """
    try:
        # 1. Creamos un diccionario con datos masivos simulados de servidores y routers
        datos_inventario = {
            "ID": [f"DEV-{i:03d}" for i in range(1, 101)], # Genera DEV-001 hasta DEV-100 (100 equipos)
            "Tipo": ["Servidor", "Router", "Switch", "Firewall"] * 25, # Repite los tipos equitativamente
            "RAM_GB": [16, 32, 64, 128, 8, 4] * 16 + [16, 32, 64, 128], # Simula diferentes capacidades de RAM
            "Estado": ["Activo", "Activo", "Mantenimiento", "Inactivo"] * 25
        }
        
        # 2. Convertimos el diccionario en un DataFrame (la tabla inteligente de Pandas)
        df = pd.DataFrame(datos_inventario)
        
        # Aseguramos que la carpeta contenedora exista antes de guardar el CSV
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # 3. Exportamos toda la tabla a un archivo CSV real sin los índices numéricos
        df.to_csv(output_path, index=False, encoding="utf-8")
        
        # 4. Simulamos que volvemos a importar el archivo CSV para procesarlo (Lectura)
        df_importado = pd.read_csv(output_path)
        
        # 5. Hacemos magia analítica con Pandas: calculamos estadísticas rápidas
        total_equipos = int(df_importado.shape[0]) # Cuenta las filas totales
        conteo_estados = df_importado["Estado"].value_counts().to_dict() # Cuenta cuántos hay en cada estado
        promedio_ram = float(df_importado["RAM_GB"].mean()) # Calcula la media de RAM de toda la empresa
        
        # Construimos el reporte final resumido para mostrar por pantalla
        reporte = (
            f"✅ ¡Archivo CSV masivo generado con éxito en: {output_path}!\n"
            f"📊 Resumen del análisis de datos con Pandas:\n"
            f" 🏢 Total de dispositivos inventariados: {total_equipos} equipos.\n"
            f" 🧠 Capacidad promedio de memoria RAM: {promedio_ram:.2f} GB.\n"
            f" 🛠️  Desglose por estado de operación:\n"
            f"    - Activos: {conteo_estados.get('Activo', 0)}\n"
            f"    - En Mantenimiento: {conteo_estados.get('Mantenimiento', 0)}\n"
            f"    - Inactivos: {conteo_estados.get('Inactivo', 0)}"
        )
        
        return True, reporte
        
    except Exception as e:
        return False, f"❌ Error en el procesamiento de datos masivos: {str(e)}"