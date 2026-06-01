import subprocess
import shutil
import platform
from typing import Tuple

def run_ping(hostname: str) -> Tuple[bool, str]:
    """
    Ejecuta un comando ping hacia un host determinado.
    Devuelve un booleano (True si responde) y el texto de la consola.
    """
    # Detectamos si es Windows o Linux/Mac. Windows usa '-n', Linux usa '-c'
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", hostname]
    
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return True, output
    except subprocess.CalledProcessError as e:
        return False, e.output

def check_disk_storage(path: str = "C:\\" if platform.system().lower() == "windows" else "/") -> Tuple[float, float, float, bool]:
    """
    Comprueba el uso del disco duro.
    Devuelve: (Total GB, Usado GB, Libre GB, Alerta_Menos_20%)
    """
    total, used, free = shutil.disk_usage(path)
    
    # Pasamos los bytes a Gigabytes (GB) de forma legible
    total_gb = round(total / (1024 ** 3), 2)
    used_gb = round(used / (1024 ** 3), 2)
    free_gb = round(free / (1024 ** 3), 2)
    
    # Calculamos si el espacio libre es menor al 20%
    porcentaje_libre = (free / total) * 100
    alerta_critica = porcentaje_libre < 20.0
    
    return total_gb, used_gb, free_gb, alerta_critica
