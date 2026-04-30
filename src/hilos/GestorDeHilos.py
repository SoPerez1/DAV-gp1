import threading


class GestorDeHilos:
    """
    Gestiona la creación y cierre ordenado de hilos para DAVCore.
    """

    def __init__(self):
        self._hilos: list[threading.Thread] = []

    def agregar_hilo(self, target, *args) -> threading.Thread:
        """Crea y registra un nuevo hilo."""
        pass  # TODO Grupo 4

    def cerrar_todos(self, intervalo_segundos: float = 1.0) -> None:
        """Cierra los hilos uno a uno con el intervalo dado."""
        pass  # TODO Grupo 4
