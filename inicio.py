import tkinter as tk
import requests

# Función para obtener el último registro desde la API
def obtener_ultimo_registro():
    url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verifica si hubo errores en la solicitud
        datos = respuesta.json()

        if datos:
            ultimo_registro = datos[-1]  # Obtener el último registro
            mostrar_datos(ultimo_registro)
        else:
            etiqueta_resultado.config(text="No hay datos disponibles.")
    except requests.exceptions.RequestException as e:
        etiqueta_resultado.config(text=f"Error: {e}")

# Función para mostrar los datos del último registro en la interfaz

def mostrar_datos(registro):
    texto = (
        f"ID: {registro['id']}\n"
        f"Nombre: {registro['nombre']}\n"
        f"Apellido: {registro['apellido']}\n"
        f"Ciudad: {registro['ciudad']}\n"
        f"Calle: {registro['calle']}"
    )
    etiqueta_resultado.config(text=texto)
# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Último Registro - Estudiante")
ventana.geometry("300x200")

# Botón para actualizar y mostrar el último registro
boton_actualizar = tk.Button(ventana, text="Obtener Último Registro", command=obtener_ultimo_registro)
boton_actualizar.pack(pady=10)

# Etiqueta para mostrar los resultados
etiqueta_resultado = tk.Label(ventana, text="", justify="left")
etiqueta_resultado.pack(padx=10, pady=10)

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
