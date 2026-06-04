# Fase 7
En este Proyecto (Taskflow-7)
Tener un entorno virtual (en este caso venv) es obligatorio y crucial por tres razones muy potentes:

1. El "Supervisor Estricto" (mypy)
Para este proyecto necesitas usar mypy, que es una herramienta que revisa que tu código no tenga errores de lógica antes de ejecutarlo. mypy no viene dentro de Python por defecto. Al instalarlo dentro de tu "venv", te aseguras de que el corrector analiza únicamente los archivos de tu proyecto y no se vuelve loco revisando carpetas de tu sistema operativo.

2. El test. O la "Lista de la Compra" (requirements.txt)
Cuando termine el proyecto, tu profesor o cualquier otra persona querrá probar tu código. Si hubieras instalado las herramientas en tu ordenador de forma global, tu archivo requirements.txt tendría una lista gigante con 200 programas que tienes instalados desde hace meses.
Al usar un venv, cuando haces pip freeze > requirements.txt, el archivo se genera limpio, conteniendo únicamente lo que tu proyecto necesita para funcionar (como mypy). Así, el profesor solo tendrá que escribir un comando para clonar tu entorno exacto.

3. El **.gitignore** con GitHub y OneDrive
Como el entorno virtual genera miles de pequeños archivos internos para que Python funcione en segundo plano. Al tenerlos todos agrupados dentro de la carpeta venv, le pudimos decir al archivo .gitignore: "Oye, no subas esto a internet

**En resumen**: Python es el motor, y el entorno virtual (venv) es la caja protectora que evita que los experimentos de tu proyecto salpiquen y estropeen tu ordenador, asegurando además que cualquiera pueda ejecutar tu código en el futuro exactamente igual que tú.


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

### 1.3. Creamos el Código "Menu Base" con Type Hints (Tipado Estricto)
Creamos el esqueleto del menú interactivo (el panel de control). Los Type Hints son etiquetas que le ponemos a las funciones para avisar qué tipo de datos entran y salen (por ejemplo, decir que una variable va a ser de tipo texto str o que una función no devuelve nada None).

Incluimos el Type Hints estrictos (como None o str) para que mypy no nos llame la atención.

Creamos el archivo: src/sys_toolkit.py
   

## Paso 2. Módulo OS - Automatización del Sistema
Creamos "os_utils.py", este archivo es un tipo "ayudante" que se encarga de hacer el trabajo sucio.

- Paso 2.1. Creamos el archivo "ayudante":  src/os_utils.py

### La perspectiva del Programador: ¿Por qué creamos os_utils.py?
    1. El Principio de Responsabilidad Única (Clean Code)
    "Un archivo debe encargarse de una sola cosa".

    El archivo "sys_toolkit.py" tiene la única misión de interactuar con el usuario (mostrar texto, leer el teclado, UN MENU para abreviar). No tiene por qué saber cómo se calcula un byte en un disco duro o cómo se envía un paquete de red. Por eso, creo un archivo "ayudante" independiente (os_utils.py) especializado en interactuar con el Sistema Operativo. Si el día de mañana el comando de Windows para el Ping cambia, solo tengo que arreglarlo en os_utils.py sin romper mi menú principal.

    2. El porqué de las librerías nativas (subprocess y shutil)
    Las herramientas de Python:

        # subprocess: Abre una pequeña "compuerta" invisible hacia la terminal de tu Windows real, ejecuta el comando ping clásico que tú escribirías a mano, captura lo que responde la máquina y nos lo devuelve en forma de texto de Python.

        # shutil: Es una librería experta en el sistema de archivos. Le pregunta directamente al disco duro cuánto espacio total tiene y cuánto le queda disponible.

    3. La rigidez de los Type Hints (Para que MyPy no nos grite)
    Las salidas deben utilizar Tuple (Tuplas), esto evita que las funciones devuelvan datos al azar.

        # run_ping devuelve una tupla Tuple[bool, str]. El bool (Verdadero/Falso) le dice al menú si la web está viva para que pinte un emoji verde ✅ o rojo ❌. El str contiene el texto técnico del ping por si queremos examinarlo.

        # check_disk_storage devuelve Tuple[float, float, float, bool]. Tres números decimales con los Gigabytes exactos y un último booleano que actúa como un disparador de alarmas si el espacio cae por debajo del 20%.

- Paso 2.2: Modificar el menú
    1. Pasamos a "conectar" los archivos. Un archivo no sabe que el otro existe hasta que no los conectas. Por eso, en la parte superior del menú (sys_toolkit.py), debemos introducir la "importacion".
        Python
        from os_utils import run_ping, check_disk_storage

    2. Tambien, debemos incluir la acción dentro del bucle (Donde pulsas las opciones)
    Tenemos que cambiar los antiguos mensajes de "pendiente" por el código real que le pide los datos al ayudante.

- Paso 2.3: Verificación

    Paso 1: La prueba real (Ejecutar el programa)
    Vamos a ver si Windows y tu Python se comunican bien. En la terminal (donde ya tienes el (.venv) activo), ejecutamos el programa con este comando:
        PowerShell
        python src/sys_toolkit.py

    Ver docs/"pruebas menu python" de python src/sys_toolkit.py.


    Paso 2: El último control antes de guardar: MyPy
    La tarea exige que el código cumpla con el tipado estricto sin errores ocultos, vamos a pasar un supervisor de calidad.

    Escribimos este comando en la terminal:
        "mypy src/os_utils.py src/sys_toolkit.py"
    Resultado:
        "(.venv) PS C:\Users\danie\OneDrive\Desktop\docs-josu-PC3-dani\JOSU0131\taskflow-7> mypy src/os_utils.py src/sys_toolkit.py
        Success: no issues found in 2 source files"
    Significa que tu código no solo funciona de maravilla, sino que además es robusto, limpio y cumple al 100% con las reglas más estrictas de Python


## Paso 3 - Módulo LOG (Analizar intentos fallidos de SSH)
Como buen System admin, tu misión ahora será crear un script que abra un archivo de registro de un servidor (`auth.log`) y busque de forma automática cuántas veces ha intentado entrar un hacker (o un usuario despistado) poniendo mal la contraseña por SSH. 

El Contexto: ¿Qué es el archivo auth.log?
    Cuando un servidor Linux está conectado a internet, miles de hackers (y bots automatizados) intentan atacarlo constantemente a través de un protocolo llamado SSH (que sirve para controlar el servidor a distancia).

    Cada vez que alguien intenta entrar a tu servidor y falla porque pone mal el usuario o la contraseña, el sistema operativo de Linux (como Ubuntu o Debian) lo anota discretamente en un diario de texto llamado auth.log (Registro de Autenticación).

    Un archivo auth.log real puede tener millones de líneas. Ejemplos:
        Plaintext
            Jun 01 12:34:56 servidor sshd[12345]: Failed password for invalid user admin from 192.168.1.50 port 54321 ssh2
            Jun 01 12:35:10 servidor sshd[12345]: Failed password for root from 203.0.113.5 port 39210 ssh2
            Jun 01 12:36:02 servidor sshd[12345]: Accepted password for dani from 192.168.1.15 port 51200 ssh2

El objetivo:
    Como no podemos leer millones de líneas a mano, vamos a programar un analizador automático que:
        1. Abra y lea ese archivo de registro.
        2. Busque las palabras clave Failed password (Contraseña fallida).
        3. Extraiga automáticamente la dirección IP del atacante y el nombre de usuario que intentaron robar (como root o admin).
        4. Cuente cuántas veces ha atacado cada IP para que podamos bloquear a los más pesados.

### 3.1 
    1. Activar la terminal
    Asegúrate de que al abrir tu VS Code, abajo en la terminal te aparezca el (.venv)

    2. Crear el archivo simulado de Logs
    Como estamosprogramando en Windows y no en un servidor Linux real con ataques en directo, tenemos que "fabricar" un archivo auth.log de prueba para que nuestro programa tenga algo que leer.
        - Creamos una carpeta llamada "logs". Dentro de esa carpeta, crea un archivo llamado auth.log.
        - Y creamos registros que simulan ataques reales

    3. Crear el archivo "ayudante"
    Ahora toca programar la maquinaria inteligente que se va a encargar de devorar ese archivo de texto y extraer los datos valiosos.

    Para este módulo vamos a usar una herramienta súper potente en la informática llamada Expresiones Regulares (Regex, un patrón inteligente para cazar textos específicos dentro de un mar de letras).
        - Creamos un archivo nuevo llamado exactamente: log_utils.py, dentro de la carpeta src
        - Dentro tenemos que escribir codigo que lea un archivo auth.log y extrae los intentos fallidos de SSH.
            Y nos devuelva
            - Una lista de tuplas con (usuario, IP) de cada ataque.
            - Un diccionario con el conteo de ataques por IP: { "IP": cantidad_de_ataques }
            - - -

    4. Conectar el ayudante a tu menú principal de Python (src/sys_toolkit.py)
    Ahora tenemos que abrir el archivo del menú para decirle que cuando el usuario pulse el 3, use un nuevo código.
        - Primero abrimos src/sys_toolkit.py.
        - Añadimos código de import:
            from log_utils import parse_ssh_failures  # <-- Añadimos esta línea nueva
        - Y en la opcion "3" elif choice=="3":, hay que añadir un analizador  de intentos fallidos de SSH en logs/auth.log, con un "if not ataques" y un "else".
        - Probamos el sistema y la opción "3".
            Esperamos:      
            Resumen de peligrosidad (Ranking de IPs atacantes):
            📍 192.168.1.100   -> 1 intentos fallidos ⚠️
            📍 203.0.113.5     -> 3 intentos fallidos 🔥 (CRÍTICO - Sugerido bloquear en Firewall)
            📍 198.51.100.2    -> 1 intentos fallidos ⚠️
        - Chequeamos el examen del supervisor:z
            "mypy src/log_utils.py src/sys_toolkit.py"
        - - -

## Paso 4: El Módulo de Red con POO (Programación Orientada a Objetos)
Contexto:
    En el día a día de una empresa, un Sysadmin no gestiona "textos sueltos", gestiona equipos reales (servidores, routers, switches, ordenadores). En programación, para representar esos equipos de forma ordenada, usamos la "POO".

    Imagina que la POO es como un *plano de fábrica*. 
    
    Nuestro objetivo sera, crear los "moldes", llamados "Clases" para definir cómo es un objeto y qué sabe hacer.

    - Primero hay que pensar en una estructura de "Herencia":

        1. Una Clase Base (NetworkDevice): El molde genérico. Todos los aparatos de una red tienen un nombre, una dirección IP y un sistema operativo.

        2. Clase Hija (ServerDevice): Un molde especializado. Hereda todo lo del aparato genérico, pero además tiene cosas exclusivas de servidores, como el número de servicios activos (por ejemplo, si tiene una base de datos web encendida).

        3. Clase Hija (RouterDevice): Otro molde especializado. Hereda los datos básicos, pero tiene algo exclusivo de los routers: el número de puertos e interfaces de red que está gestionando.

### Paso 4.1: Crear el archivo ayudante "src/net_utils.py"
Vamos a construir el ecosistema de objetos.
    1. En la carpeta src/ en VS Code. Creamos un archivo nuevo llamado exactamente: net_utils.py
    2. Necesitaremos código sobre "class NetworkDevice, ServerDevice(NetworkDevice), RouterDevice(NetworkDevice), y un def get_mock_inventory() -> List[NetworkDevice]:"

### Paso 4.2: Conectar la POO a nuestro menú principal (src/sys_toolkit.py)
Ahora vamos a hacer que el menú sea capaz de leer esta lista de objetos y procesarlos uno a uno (lo que en programación llamamos Polimorfismo: el menú llamará a get_details() y cada objeto sabrá responder con sus datos exclusivos de forma inteligente).
    1. En nuestro archivo "menu" de python, src/sys_toolkit.py.
    2. Debemos incluir la nueva linea de código para la importación:
        Python
        from net_utils import get_mock_inventory  # <-- Añadimos esta línea nueva
    3. Y tendremos que editar la función de la opción "4" con un codigo para que inicie la "Iniciando Auditoría de Dispositivos de Red (POO)"
    4. Ahora hay que testear los objetos (la opcion "4"):

    **RECUERDA** para iniciar python primero encender sistema virtual (.venv) y luego escribiremos en la terminal: "python src/sys_toolkit.py"

    Esperamos: 
        [i] Iniciando Auditoría de Dispositivos de Red (POO)...
        📊 Se han cargado 4 dispositivos en la base de datos de auditoría.
        ============================================================
        🖥️  [srv-produccion-01] IP: 10.0.0.10 | SO: Ubuntu Server 22.04 | 💼 Servicios Activos: 5
        🖥️  [rtr-core-central] IP: 10.0.0.1 | SO: Cisco IOS | 🔌 Puertos Totales: 24
        🖥️  [srv-backup-datos] IP: 10.0.0.20 | SO: Debian 12 | 💼 Servicios Activos: 2
        🖥️  [rtr-oficina-b] IP: 192.168.1.1 | SO: MikroTik RouterOS | 🔌 Puertos Totales: 8
        ============================================================
        ✅ Auditoría completada con éxito. Estructura de clases validada.
        - - -
    5. Salimos del menu (pulsando "0") y vamos a comprobar que la estructura de clases, constructores (__init__) y el uso de super() sean perfectos para el tipado estricto.
        PowerShell
         "mypy src/net_utils.py src/sys_toolkit.py"
    - - -

## Paso 5: El Módulo API (Consultar Geolocalización de IP sospechosa)
En este paso vamos a programar para que deje de trabajar de forma "aislada" dentro del PC y lo conectaremos a internet en tiempo real para pedirle datos a un servidor externo.

El Contexto: 
    Una API (Application Programming Interface), es como una "ventanilla de información" que una web abre para que otros programas puedan hablar con ella de forma automática.

    En el "Paso 3" descubrimos que la IP 203.0.113.5 estaba intentando atacar nuestro sistema, pero nos falta información... ¿quién es esa IP? ¿Desde qué parte del mundo nos están atacando?

    En lugar de ir a Google a buscarlo a mano, vamos a hacer que tu script use la librería requests para conectarse a una API pública y gratuita de geolocalización (ip-api.com). Le enviaremos una IP y su servidor nos devolverá al instante un paquete de datos (en formato JSON) diciéndonos el país, la ciudad, la compañía de internet (ISP) y hasta las coordenadas geográficas del atacante.

### Paso 5.1: Instalar la librería externa requests
Para este paso necesitamos una herramienta para poder conectarnos a internet (ya que por defecto esta función no viene dentro de Python). 
    1. Necesitamos instalar la librería con el comando:
        PowerShell
        pip install requests

    2. Creamos el archivo ayudante src/"api_utils.py". En este programaremos mediante código la conexión a la API de ip-api.com para obtener la geolocalización de una IP. Y que nos devuelve:
        - Un booleano (True si la consulta fue exitosa).
        - Un diccionario con los datos de respuesta (país, ciudad, isp, etc.).

    3. Conectar la API al menú principal "sys_toolkit.py"
        1. En el archivo src/sys_toolkit.py
        2. Añadimos el import
        3. Editamos la función de la opción "5"  con un codigo para que "[Módulo API] Consultar Geolocalización de IP sospechosa"

    4. Ahora hay que testear la conexión externa (la opcion "5"):
        PowerShell
        python src/sys_toolkit.py

    Esperamos, al selecionar opción 5:
        🌐 [Módulo API] Consultar Geolocalización de IP sospechosa
        Introduce la IP que deseas investigar (ej: 8.8.8.8 o la del atacante): 203.0.113.5
        [i] Conectando con la API de geolocalización para investigar 203.0.113.5...
        ==================================================
        🌍 REPORTES DE UBICACIÓN PARA LA IP: 203.0.113.5
        --------------------------------------------------
        🏳️ País:     China
        🏙️ Ciudad:   Beijing
        🏢 Proveedor: China Telecom
        📍 Coordenadas: Latitud 39.9042 | Longitud 116.4074
        ==================================================

    Y al volver a seleccionar la "5" y introducir una ip como 8.8.8.8:
        🌐 [Módulo API] Consultar Geolocalización de IP sospechosa
        Introduce la IP que deseas investigar (ej: 8.8.8.8 o la del atacante): 8.8.8.8
        [i] Conectando con la API de geolocalización para investigar 8.8.8.8...
        ==================================================
        🌍 REPORTES DE UBICACIÓN PARA LA IP: 8.8.8.8
        --------------------------------------------------
        🏳️ País:     United States
        🏙️ Ciudad:   Ashburn
        🏢 Proveedor: Google LLC
        📍 Coordenadas: Latitud 39.03 | Longitud -77.5
        ==================================================

    5. Control de tipado de MyPy"
    Al introducir la librería externa requests, es vital comprobar que el supervisor de calidad siga estando contento con la lógica del código y los tipos de datos que maneja la API.
        PowerShell
        mypy src/api_utils.py src/sys_toolkit.py