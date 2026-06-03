import os
import re
from typing import Dict, List, Tuple

def parse_ssh_failures(log_path: str) -> Tuple[List[Tuple[str, str]], Dict[str, int]]:
    """
    Lee un archivo auth.log y extrae los intentos fallidos de SSH.
    Devuelve:
    - Una lista de tuplas con (usuario, IP) de cada ataque.
    - Un diccionario con el conteo de ataques por IP: { "IP": cantidad_de_ataques }
    """
    # Lista para guardar cada ataque individual: [('admin', '192.168.1.100'), ...]
    ataques_individuales: List[Tuple[str, str]] = []
    # Diccionario para contar cuántas veces ataca cada IP: {'203.0.113.5': 3}
    conteo_por_ip: Dict[str, int] = {}

    # Comprobamos si el archivo realmente existe antes de abrirlo para evitar que el programa explote
    if not os.path.exists(log_path):
        return ataques_individuales, conteo_por_ip

    # El patrón Regex: Busca 'Failed password for', luego captura el usuario, y tras 'from' captura la IP
    patron = re.compile(r"Failed password for (?:invalid user )?(\S+) from (\S+)")

    with open(log_path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            match = patron.search(linea)
            if match:
                usuario: str = match.group(1)
                ip: str = match.group(2)
                
                # Guardamos el ataque en la lista
                ataques_individuales.append((usuario, ip))
                
                # Sumamos 1 al contador de esa IP específica
                conteo_por_ip[ip] = conteo_por_ip.get(ip, 0) + 1

    return ataques_individuales, conteo_por_ip