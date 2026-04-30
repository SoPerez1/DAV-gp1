import threading
from typing import Optional


class Comando:
    """
    Clase base para el manejo de comandos de voz en DAVCore.
    Provee escucha exclusiva, relleno sistemático y print de testeo.
    """

    def EscuchaExclusiva(self, vector: list[str]) -> Optional[str]:
        """
        Escucha de voz restringida a los valores del vector dado.
        
        Palabras clave reservadas:
          - "Enter"    → concatena el siguiente valor dictado
          - "Cancelar" → aborta, devuelve None
          - "Enviar"   → finaliza, devuelve el string acumulado
        
        No se acumulan duplicados consecutivos.
        
        Args:
            vector: lista de strings aceptados como comandos válidos
        
        Returns:
            str con el contenido acumulado, o None si se canceló
        """
        pass  # TODO Grupo 1

    def RellenoSistematico(self):
        """
        Método virtual. No implementar en este sprint.
        """
        pass

    def PrintTesteo(self, indice_vector: int) -> None:
        """
        Llama a EscuchaExclusiva con el vector en posición indice_vector
        de la tupla global, convierte el resultado a string y lo imprime.

        Args:
            indice_vector: posición del vector dentro de la tupla de vectores
        """
        pass  # TODO Grupo 1
