from typing import List

class NetworkDevice:
    """Clase base que representa un dispositivo de red genérico."""
    def __init__(self, name: str, ip_address: str, os_type: str) -> None:
        self.name: str = name
        self.ip_address: str = ip_address
        self.os_type: str = os_type

    def get_details(self) -> str:
        """Devuelve una cadena de texto con la información básica del dispositivo."""
        return f"🖥️  [{self.name}] IP: {self.ip_address} | SO: {self.os_type}"


class ServerDevice(NetworkDevice):
    """Clase especializada para Servidores (Hereda de NetworkDevice)."""
    def __init__(self, name: str, ip_address: str, os_type: str, active_services: int) -> None:
        # Usamos 'super()' para rellenar los datos genéricos en la clase padre
        super().__init__(name, ip_address, os_type)
        # Añadimos la característica única del servidor
        self.active_services: int = active_services

    def get_details(self) -> str:
        """Sobrescribe el método original para añadir los servicios activos."""
        datos_base = super().get_details()
        return f"{datos_base} | 💼 Servicios Activos: {self.active_services}"


class RouterDevice(NetworkDevice):
    """Clase especializada para Routers (Hereda de NetworkDevice)."""
    def __init__(self, name: str, ip_address: str, os_type: str, total_ports: int) -> None:
        super().__init__(name, ip_address, os_type)
        # Añadimos la característica única del router
        self.total_ports: int = total_ports

    def get_details(self) -> str:
        """Sobrescribe el método original para añadir los puertos de red."""
        datos_base = super().get_details()
        return f"{datos_base} | 🔌 Puertos Totales: {self.total_ports}"


def get_mock_inventory() -> List[NetworkDevice]:
    """Fabricamos un inventario simulado con diferentes objetos para la auditoría."""
    return [
        ServerDevice("srv-produccion-01", "10.0.0.10", "Ubuntu Server 22.04", active_services=5),
        RouterDevice("rtr-core-central", "10.0.0.1", "Cisco IOS", total_ports=24),
        ServerDevice("srv-backup-datos", "10.0.0.20", "Debian 12", active_services=2),
        RouterDevice("rtr-oficina-b", "192.168.1.1", "MikroTik RouterOS", total_ports=8)
    ]