import os
import csv
from faker import Faker

def generate_massive_csv(output_path: str, num_rows: int = 1000) -> None:
    """Genera un archivo CSV con filas de servidores ficticios para la auditoría."""
    fake = Faker()
    
    # Nos aseguramos de que la carpeta contenedora exista
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Definimos las columnas que pide la rúbrica implícitamente
    headers = ["ID", "Hostname", "SO", "RAM_GB", "Departamento"]
    
    sistemas_operativos = ["Windows Server 2019", "Windows Server 2022", "Ubuntu Server 22.04", "Debian 12", "RedHat RHEL 9"]
    departamentos = ["IT", "RRHH", "Finanzas", "Operaciones", "Desarrollo", "Seguridad"]
    
    print(f"[i] Fabricando {num_rows} filas de servidores ficticios con Faker...")
    
    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers) # Escribimos la cabecera
        
        for i in range(1, num_rows + 1):
            dev_id = f"SRV-{i:04d}"
            hostname = f"{fake.word()}-lnx" if "Ubuntu" in sistemas_operativos else f"{fake.word()}-win"
            so = fake.random_element(elements=sistemas_operativos)
            # Forzamos un rango de RAM que incluya equipos de menos de 4GB (ej: 2GB) para el filtro posterior
            ram = fake.random_element(elements=(2, 4, 8, 16, 32, 64, 128))
            depto = fake.random_element(elements=departamentos)
            
            writer.writerow([dev_id, hostname, so, ram, depto])

if __name__ == "__main__":
    ruta_destino = "data/inventory.csv"
    generate_massive_csv(ruta_destino, 1000)
    print(f"✅ Archivo generado con éxito en: {ruta_destino}")