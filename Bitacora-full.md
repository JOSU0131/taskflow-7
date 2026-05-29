# Fase 7

## Paso 1: Setup del Entorno y Menú CLI Estricto
Vamos a preparar el terreno en tu máquina para que la estructura del código sea modular y profesional desde el primer minuto.

1. Estructura de Carpetas Recomendada
Para mantener todo limpio como te pide el entregable, crea esta estructura en tu espacio de trabajo:

    taskflow-7/
    │
    ├── docs/
    │   └── python-sysadmin.md
    │
    ├── src/
    │   ├── __init__.py
    │   ├── sys_toolkit.py
    │   ├── os_utils.py
    │   ├── log_parser.py
    │   ├── network_models.py
    │   ├── threat_intel.py
    │   ├── generate_inventory.py
    │   └── inventory_manager.py
    │
    ├── tests/
    │   └── test_toolkit.py
    │
    ├── .gitignore
    └── requirements.txt

### 1.2. Aislamiento del Entorno (.gitignore y venv)
El Entorno Virtual (venv)
    Qué es: Es como crear una "burbuja aislada" o un laboratorio cerrado dentro de tu ordenador dedicado única y exclusivamente a este proyecto.

    Para qué sirve: Python viene instalado en tu sistema operativo, pero si instalas librerías globales, a la larga se rompen unas a otras. Con python3 -m venv venv creas una mini-bifurcación limpia de Python. Al activarlo (source venv/bin/activate), todo lo que instales ahí dentro se queda ahí dentro y no ensucia tu ordenador. Cuando borres la carpeta del proyecto, el entorno virtual desaparece con ella sin dejar rastro.

    1. Crear el entorno virtual:
    Abrimos terminal en la raíz del proyecto (taskflow-7/) y ejecutamos los siguientes comandos para crear el entorno virtual:
        
        En terminal vs code PowerShell
        python -m venv venv --without-pip

            ## 1. Instalar PIP manualmente dentro del entorno
            python -m ensurepip --default-pip

            ## 2. Instalar mypy e inicializar el requirements.txt
            pip install mypy
            pip freeze > requirements.txt

        # Activar el entorno virtual (Windows - si usas PowerShell)
        # .\venv\Scripts\Activate.ps1

### 1.2. Creamos el archivo .gitignore
    Porque el entorno virtual (venv) pesa mucho y contiene miles de archivos que Python genera automáticamente. Subir eso a GitHub es una mala práctica pésima porque ralentiza todo

        Qué era: Una lista de "guardias de seguridad" para GitHub. Le dice a Git qué carpetas tiene prohibido subir a internet.
        Sirve para: .gitignore le dice a Git: "Ignora la carpeta venv y las cachés, solo sube los archivos de código que he escrito".

        codigo: 
            venv/
            __pycache__/
            *.pyc
            .pytest_cache/
            .mypy_cache/

### 1.3. Creamos el Código Base con Type Hints (Tipado Estricto)
Creamos el esqueleto del menú interactivo (el panel de control). Los Type Hints son etiquetas que le ponemos a las funciones para avisar qué tipo de datos entran y salen (por ejemplo, decir que una variable va a ser de tipo texto str o que una función no devuelve nada None).

Incluimos el Type Hints estrictos (como None o str) para que mypy no nos llame la atención.

    Creamos el archivo src/sys_toolkit.py:
   
