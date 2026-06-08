Documento de Pruebas inciales en menu Python

Terminal:
python src/sys_toolkit.py

# Prueba 1
    🛠️  SYS_TOOLKIT v1.0 - KIT DE AUTOMATIZACIÓN
    =============================================
    1. [OS] Ejecutar verificación de Ping
    2. [OS] Comprobar espacio libre en disco
    3. [LOG] Analizar intentos fallidos de SSH (auth.log)
    4. [NET] Ejecutar auditoría de dispositivos (POO)
    5. [API] Consultar Geolocalización de IP sospechosa
    6. [DATA] Generar e importar inventario masivo (Pandas)
    0. Salir
    =============================================
    Selecciona una opción: 1

    Introduce la IP o dominio a testear (ej: 8.8.8.8): 8.8.8.8
    [i] Lanzando ping a 8.8.8.8...
    ✅ ¡El host 8.8.8.8 RESPONDE correctamente!
    ------------------------------
    Haciendo ping a 8.8.8.8 con 32 bytes de datos:
    Respuesta desde 8.8.8.8: bytes=32 tiempo=21ms TTL=115

    Estad¡sticas de ping para 8.8.8.8:
        Paquetes: enviados = 1, recibidos = 1, perdidos = 0
        (0% perdidos),
    Tiempos aproximados de ida y vuelta en milisegundos:
        M¡nimo = 21ms, M ximo = 21ms, Media = 21ms

# Prueba 2
    =============================================
    Selecciona una opción: 2

    [i] Analizando almacenamiento del sistema...
    📦 Disco Total: 933.46 GB
    🛑 Espacio Usado: 464.26 GB
    🟢 Espacio Libre: 469.2 GB
    ✅ Estado del disco: Óptimo (Suficiente espacio libre).

## Prueba 3
    (.venv) PS C:\Users\danie\OneDrive\Desktop\docs-josu-PC3-dani\JOSU0131\taskflow-7> mypy src/os_utils.py src/sys_toolkit.py

    Success: no issues found in 2 source files

- ¿Por qué es tan importante el mensaje de "Success"?
    Cuando ejecutaste el comando mypy src/os_utils.py src/sys_toolkit.py y la pantalla te devolvió:

    Success: no issues found in 2 source files

    Significa que el supervisor ha revisado toda la estructura interna de tus dos archivos y ha comprobado que no hay ni una sola incoherencia.

    Ha verificado que cuando el menú llama a la función de hacer ping, le pasa un texto.

    Ha verificado que las variables reciben el tipo de dato correcto.

    Te garantiza que el código está "blindado" contra este tipo de errores humanos comunes.

## Últimas pruebas paso 8 con demonio automatico

### 1. Control de Calidad con PyTest (Pruebas Unitarias)
Se ha verificado la función de extracción y conteo de IPs atacantes (`parse_ssh_failures`) mediante datos simulados controlados, aislando la lógica de producción.
        Resultado: exitoso, rutas validadas en entorno Windows.
        ```powershell
        $env:PYTHONPATH="." ; pytest
        ============================ test session starts ============================
        platform win32 -- Python 3.10.0, pytest-9.0.3, pluggy-1.6.0
        rootdir: C:\Users\danie\OneDrive\Desktop\docs-josu-PC3-dani\JOSU0131\taskflow-7
        plugins: Faker-40.21.0
        collected 1 item                                                             

        tests\test_toolkit.py .                                                [100%]
        - - -

### 2. Prueba de Automatización en Segundo Plano (Demonio con Schedule)
Se ha creado y ejecutado con éxito el script scheduler_daemon.py, simulando un servicio del sistema que se ejecuta de forma autónoma. El demonio lee el inventario masivo en CSV, aplica los filtros analíticos de Pandas y regenera de forma limpia y automática el informe Excel para gerencia.
        🤖 Demonio de automatización para Sysadmins iniciado.
        ⏳ Presiona Ctrl + C para detener el demonio en segundo plano.

        ⏰ [DEMONIO] Ejecutando análisis automático programado...
        [i] Cargando inventario masivo desde data/inventory.csv con Pandas...

        🔍 --- APLICANDO FILTROS DE SEGURIDAD (Paso 6) ---
        ⚠️ Se han detectado 484 servidores que requieren atención (Windows o <4GB RAM).

        📊 --- AGRUPACIÓN POR DEPARTAMENTO (Paso 6) ---
        Departamento  Total_Servidores
        Desarrollo               158
            Finanzas               170
                IT               175
        Operaciones               150
                RRHH               187
        Seguridad               160

        📊 --- GENERACIÓN DE INFORME EJECUTIVO EN EXCEL (Paso 7) ---
        ✅ Informe mensual para gerencia generado en: data/informe_mensual_gerencia.xlsx
        ⏰ [DEMONIO] Tarea completada. Esperando a la siguiente hora...

        🛑 Demonio detenido por el Administrador.
        - - -

