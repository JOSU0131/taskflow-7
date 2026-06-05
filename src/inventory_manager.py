import os
import pandas as pd

def run_inventory_analysis(input_csv: str, output_excel: str) -> None:
    """Carga el inventario, aplica filtros avanzados, agrupa datos y exporta a Excel."""
    if not os.path.exists(input_csv):
        print(f"❌ Error: No se encuentra el archivo de origen {input_csv}. Ejecuta primero generate_inventory.py")
        return

    print(f"[i] Cargando inventario masivo desde {input_csv} con Pandas...")
    df = pd.read_csv(input_csv)
    
    print("\n🔍 --- APLICANDO FILTROS DE SEGURIDAD (Paso 6) ---")
    # Filtro: Contiene 'Windows Server' O tiene menos de 4GB de RAM
    condicion_so = df["SO"].str.contains("Windows Server", na=False)
    condicion_ram = df["RAM_GB"] < 4
    
    df_filtrado = df[condicion_so | condicion_ram]
    print(f"⚠️ Se han detectado {df_filtrado.shape[0]} servidores que requieren atención (Windows o <4GB RAM).")
    print(df_filtrado.head(10)) # Mostramos los 10 primeros por consola
    
    print("\n📊 --- AGRUPACIÓN POR DEPARTAMENTO (Paso 6) ---")
    # Agrupamos por departamento y contamos cuántos servidores tiene cada uno en total
    conteo_departamentos = df.groupby("Departamento")["ID"].count().reset_index()
    conteo_departamentos.columns = ["Departamento", "Total_Servidores"]
    print(conteo_departamentos.to_string(index=False))
    
    print("\n📊 --- GENERACIÓN DE INFORME EJECUTIVO EN EXCEL (Paso 7) ---")
    # Guardamos el DataFrame filtrado (los de riesgo) en un archivo Excel real
    os.makedirs(os.path.dirname(output_excel), exist_ok=True)
    df_filtrado.to_excel(output_excel, index=False)
    print(f"✅ Informe mensual para gerencia generado en: {output_excel}")

if __name__ == "__main__":
    run_inventory_analysis("data/inventory.csv", "data/informe_mensual_gerencia.xlsx")