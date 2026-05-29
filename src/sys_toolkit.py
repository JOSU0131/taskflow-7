import sys

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
                print("\n[!] Opción 1 seleccionada (Módulo OS pendiente...)")
            elif choice == "2":
                print("\n[!] Opción 2 seleccionada (Módulo OS pendiente...)")
            elif choice == "3":
                print("\n[!] Opción 3 seleccionada (Módulo Log pendiente...)")
            elif choice == "4":
                print("\n[!] Opción 4 seleccionada (Módulo POO pendiente...)")
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