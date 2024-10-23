import requests

class GetRecord:
    def __init__(self, url):
        self.url = url

    def obtener_ultimo_registro(self):
        try:
            respuesta = requests.get(self.url)
            respuesta.raise_for_status()  # Verifica si hubo errores en la solicitud
            datos = respuesta.json()
            if datos:
                return datos[-1]  # Retorna el último registro
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener los datos: {e}")
            return None
