# Python en la Administración de Sistemas Modernos (ASIR)

## Python vs Bash
Aunque **Bash** sigue siendo el rey indiscutible para automatizar tareas lineales del sistema operativo, tuberías (*pipelines*) rápidas y gestión de comandos nativos, carece de escalabilidad cuando la complejidad del problema aumenta. 

Un administrador de sistemas moderno recurre a **Python** por las siguientes razones:

* **Estructuras de Datos Avanzadas:** Manipular JSONs complejos de APIs de monitoreo, sets para deduplicación de IPs o diccionarios anidados es costoso y propenso a errores en Bash, mientras que en Python es nativo y eficiente.
* **Ecosistema de Librerías:** Python permite realizar análisis de datos masivos (Pandas), generar informes ejecutivos en hojas de cálculo reales (OpenPyXL) o interactuar de forma robusta con servicios web (Requests) sin depender de herramientas externas como `awk`, `sed` o `curl` encadenados.
* **Mantenibilidad y Robustez:** El uso de Programación Orientada a Objetos (POO), bloques de control de excepciones (`try/except`) y tipado estricto (*Type Hints*) garantiza que los scripts de infraestructura sean legibles, testeables mediante pruebas unitarias y fáciles de mantener por equipos de DevOps.