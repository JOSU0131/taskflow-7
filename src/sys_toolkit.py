import sys
# Importamos las funciones del módulo "os_utils" que acabamos de crear
from os_utils import run_ping, check_disk_storage
from log_utils import parse_ssh_failures  # <-- Añadimos esta línea nueva
from net_utils import get_mock_inventory  # <-- Módulo POO

def show_menu() -> None:
    """Imprime el menú interactivo en la consola."""
    print("\n" + "="*45)
    print("🛠️  SYS_TOOLKIT v1.0 - KIT DE AUTOMATIZACIÓN")
    print("="*45)
    print("1. [OS] Ejecutar verificación de Ping")
    print("2. [OS] Comprobar espacio libre en disco")
    print("3. [LOG] Analizar intentos fallidos de SSH (auth.log)")
    print("4. [NET] Ejecutar auditoría de dispositivos (POO)")
    print("5. [API] Consultar Geolocalización de IP sospechosa")
    print("6. [DATA] Generar e importar inventario masivo (Pandas)")
    print("0. Salir")
    print("="*45)

def main() -> None:
    """Bucle principal de la interfaz de línea de comandos."""
    while True:
        show_menu()
        try:
            choice: str = input("Selecciona una opción: ").strip()
            
            if choice == "1":
                ip: str = input("\nIntroduce la IP o dominio a testear (ej: 8.8.8.8): ").strip()
                print(# Pasamos los bytes a Gigabytes (GB) de forma legible
f"[i] Lanzando ping a {ip}...")
                exito, resultado = run_ping(ip)
                if exito:
                    print(f"✅ ¡El host {ip} RESPONDE correctamente!")
                else:
                    print(f"❌ ¡El host {ip} NO responde o es inaccesible!")
                print("-" * 30 + "\n" + resultado)
                
            elif choice == "2":
                print("\n[i] Analizando almacenamiento del sistema...")
                total, usado, libre, alerta = check_disk_storage()
                print(f"📦 Disco Total: {total} GB")
                print(f"🛑 Espacio Usado: {usado} GB")
                print(f"🟢 Espacio Libre: {libre} GB")
                
                if alerta:
                    print("⚠️  ¡ALERTA CRÍTICA! El espacio libre en disco es menor al 20%.")
                else:
                    print("✅ Estado del disco: Óptimo (Suficiente espacio libre).")
                    
            elif choice == "3":
                print("\n[i] Analizando intentos fallidos de SSH en logs/auth.log...")
                ruta_log: str = "logs/auth.log"
                
                # Llamamos al ayudante para que procese el archivo
                ataques, mapa_ips = parse_ssh_failures(ruta_log)
                
                if not ataques:
                    print("✅ No se detectaron intentos fallidos de inicio de sesión o el archivo está vacío.")
                else:
                    print(f"\n🚨 ¡SE DETECTARON {len(ataques)} INTENTOS DE ATAQUE SSH! 🚨")
                    print("-" * 50)
                    print("Detalle de los últimos accesos bloqueados:")
                    for usuario, ip in ataques:
                        print(f" 💀 IP: {ip.ljust(15)} -> Intentó robar el usuario: [{usuario}]")
                    
                    print("-" * 50)
                    print("Resumen de peligrosidad (Ranking de IPs atacantes):")
                    for ip, total in mapa_ips.items():
                        # Si una IP ataca 3 o más veces, le ponemos una alerta roja extra
                        alerta_nivel = "🔥 (CRÍTICO - Sugerido bloquear en Firewall)" if total >= 3 else "⚠️"
                        print(f" 📍 {ip.ljust(15)} -> {total} intentos fallidos {alerta_nivel}")

            elif choice == "4":
                print("\n[i] Iniciando Auditoría de Dispositivos de Red (POO)...")
                
                # Solicitamos el inventario de objetos reales a nuestro ayudante
                inventario = get_mock_inventory()
                
                print(f"📊 Se han cargado {len(inventario)} dispositivos en la base de datos de auditoría.")
                print("=" * 60)
                
                # Recorremos la lista. Gracias al polimorfismo, cada objeto se dibuja a sí mismo correctamente
                for dispositivo in inventario:
                    print(dispositivo.get_details())
                    
                print("=" * 60)
                print("✅ Auditoría completada con éxito. Estructura de clases validada.")

            elif choice == "5":
                print("\n[!] Opción 5 seleccionada (Módulo API pendiente...)")
            elif choice == "6":
                print("\n[!] Opción 6 seleccionada (Módulo Pandas pendiente...)")
            elif choice == "0":
                print("\n👋 Saliendo del Toolkit. ¡Buen día, Sysadmin!")
                sys.exit(0)
            else:
                print("\n❌ Opción no válida. Inténtalo de nuevo.")
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Ejecución interrumpida por el usuario. Saliendo...")
            sys.exit(0)

if __name__ == "__main__":
    main()