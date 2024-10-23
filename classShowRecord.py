import tkinter as tk
from classGetRecord import GetRecord

class ShowRecordApp:
    def __init__(self):
        self.url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"
        self.api = GetRecord(self.url)  # Instancia de la clase GetRecord

        # Configuración de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Último Registro - Estudiante")
        self.ventana.geometry("300x200")

        # Botón para obtener el último registro
        self.boton_actualizar = tk.Button(
            self.ventana, text="Obtener Último Registro", command=self.mostrar_registro
        )
        self.boton_actualizar.pack(pady=10)

        # Etiqueta para mostrar los resultados
        self.etiqueta_resultado = tk.Label(self.ventana, text="", justify="left")
        self.etiqueta_resultado.pack(padx=10, pady=10)

    def mostrar_registro(self):
        registro = self.api.obtener_ultimo_registro()
        if registro:
            texto = (
                f"ID: {registro['id']}\n"
                f"Nombre: {registro['nombre']}\n"
                f"Apellido: {registro['apellido']}\n"
                f"Ciudad: {registro['ciudad']}\n"
                f"Calle: {registro['calle']}"
            )
        else:
            texto = "No hay datos disponibles o ocurrió un error."
        self.etiqueta_resultado.config(text=texto)

    def iniciar(self):
        self.ventana.mainloop()
