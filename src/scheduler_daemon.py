import time
import schedule
from inventory_manager import run_inventory_analysis

def ejecutar_tarea_mantenimiento() -> None:
    print("\n⏰ [DEMONIO] Ejecutando análisis automático programado...")
    ruta_csv = "data/inventory.csv"
    ruta_excel = "data/informe_mensual_gerencia.xlsx"
    
    # Ejecuta el análisis del paso 7 de forma automatizada
    run_inventory_analysis(ruta_csv, ruta_excel)
    print("⏰ [DEMONIO] Tarea completada. Esperando a la siguiente hora...")

# Programamos el demonio para que se ejecute CADA HORA como pide la tarea
schedule.every(1).hours.do(ejecutar_tarea_mantenimiento)

# También programamos una versión de prueba cada 10 segundos para poder ver que funciona ahora mismo
schedule.every(10).seconds.do(ejecutar_tarea_mantenimiento)

if __name__ == "__main__":
    print("🤖 Demonio de automatización para Sysadmins iniciado.")
    print("⏳ Presiona Ctrl + C para detener el demonio en segundo plano.\n")
    
    # Bucle infinito para mantener el servicio corriendo (Demonio)
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Demonio detenido por el Administrador.")