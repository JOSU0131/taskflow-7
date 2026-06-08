# 🛠️ Sysadmin Automation Toolkit - Fase 7

Kit de herramientas modular en Python desarrollado para la automatización de tareas de sistemas, auditoría de redes, parseo de logs de seguridad y análisis masivo de inventarios. Diseñado bajo estándares de tipado estricto y modularidad para administración de sistemas moderna.

---
##
## 🚀 Características Principales
* **Módulo de Redes:** Escaneo de puertos y consulta de geolocalización de IPs mediante API externa con control de fallos.
* **Auditoría de Seguridad:** Parseo automatizado de archivos de log (`auth.log`) para detectar ataques de fuerza bruta por SSH.
* **Gestión Masiva de Inventarios:** Generación programática de 1,000 registros ficticios (`Faker`) y análisis de datos optimizado con `Pandas`.
* **Informes Ejecutivos:** Exportación automatizada de datos críticos a hojas de cálculo reales de Microsoft Excel (`openpyxl`).
* **Garantía de Fiabilidad:** Cobertura de pruebas unitarias con `Pytest` y tipado estricto verificado mediante `MyPy`.
* **Automatización Continua:** Demonio de ejecución programada (`Schedule`) en segundo plano para tareas cíclicas.

---

## 🛠️ Tecnologías y Librerías Utilizadas

| Herramienta / Librería | Uso Principal |
| :--- | :--- |
| **Python 3.10+** | Lenguaje base del Toolkit y scripts de automatización. |
| **Pandas** | Carga, filtrado y agrupación analítica del inventario. |
| **OpenPyXL** | Motor de generación y escritura de reportes ejecutivos `.xlsx`. |
| **Faker** | Generación masiva de datos aleatorios para simulaciones de sistemas. |
| **Pytest** | Laboratorio de pruebas unitarias para asegurar la fiabilidad del código. |
| **MyPy** | Supervisor de análisis estático y tipado estricto de datos. |
| **Schedule** | Orquestador de tareas en segundo plano (Simulación de Demonio). |

---

## 📁 Estructura Final del Proyecto
    ```text
    taskflow-7/
    │
    ├── data/               # Archivos de entrada y reportes generados (.csv, .xlsx)
    │   ├── inventory.csv
    │   └── informe_mensual_gerencia.xlsx
    │
    ├── docs/               # Documentación técnica, bitácoras e informes de pruebas
    │   ├── pruebas menu python.md
    │   └── python-sysadmin.md
    │
    ├── src/                # Código fuente del Toolkit modular
    │   ├── __init__.py
    │   ├── data_utils.py       # Procesamiento y analítica con Pandas
    │   ├── generate_inventory.py # Generador masivo de 1,000 servidores con Faker
    │   ├── inventory_manager.py  # Filtros de seguridad y reportes ejecutivos
    │   ├── log_utils.py        # Parseador de logs de autenticación SSH
    │   ├── net_utils.py        # Auditoría de puertos y geolocalización API
    │   ├── scheduler_daemon.py # Demonio de ejecución y planificación horaria
    │   └── sys_toolkit.py      # Menú CLI e interfaz principal por consola
    │
    ├── tests/              # Pruebas unitarias automatizadas
    │   └── test_toolkit.py     # Test de lógica de logs e IPs
    │
    ├── .gitignore          # Exclusiones de Git (burbuja .venv, cachés de pytest)
    └── requirements.txt    # Lista oficial de dependencias instaladas

---

## Guia para Descargar y Ejecutar el Proyecto

1. Clonar el repositorio e ingresar
        PowerShell
        git clone [https://github.com/tu-usuario/taskflow-7.git](https://github.com/tu-usuario/taskflow-7.git)
        cd taskflow-7

2. Activar el entorno virtual e instalar dependencias
        PowerShell
        # Activar entorno virtual (Windows)
        .venv\Scripts\Activate.ps1

        # Instalar todas las librerías del proyecto de un solo golpe
        pip install -r requirements.txt

3. Ejecutar el menú interactivo principal
        PowerShell
        python src/sys_toolkit.py

4. Lanzar el laboratorio de pruebas unitarias (Pytest)
        PowerShell
        $env:PYTHONPATH="." ; pytest

5. Arrancar el demonio de automatización en segundo plano
        PowerShell
        python src/scheduler_daemon.py

