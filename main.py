import sys

# Agregá la ruta donde tenés la carpeta DAV-gp1 (descomentá y ajustá esta línea si hace falta)
# sys.path.append(r"C:\Users\benja\Proyectos\Documentos\Pet\DAVCore\DAV-gp1")

from src.modelo.VoskModel import VoskModel

if __name__ == "__main__":
    # Importante: poné la ruta de la carpeta que acabás de descomprimir
    ruta_modelo = r"MODELO\vosk-model-small-es-0.42" 
    
    try:
        modelo = VoskModel(ruta_modelo)
        modelo.escuchar_latente("cerrar")
    except KeyboardInterrupt:
        print("\nPrograma terminado a la fuerza.")
