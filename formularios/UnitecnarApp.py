import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

class UnitecnarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unitecnar - Panel de Administración")
        self.root.geometry("1000x600")
        self.root.config(bg="#F0F8FF")  
        
        self.centrar_ventana(self.root, 1000, 600)
        
        self.crear_menu_lateral()
        self.crear_contenido_principal()
        self.mostrar_correo()

    def centrar_ventana(self, ventana, ancho, alto):
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()
        posicion_x = (screen_width - ancho) // 2
        posicion_y = (screen_height - alto) // 2
        ventana.geometry(f'{ancho}x{alto}+{posicion_x}+{posicion_y}')

    def leer_imagen(self, ruta, tamano):
        imagen = Image.open(ruta)
        imagen = imagen.resize(tamano, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(imagen)

    def crear_menu_lateral(self):
        self.menu_lateral = tk.Frame(self.root, bg="#32CD32", width=200, height=600) 
        self.menu_lateral.pack(side="left", fill="y")
        self.cargar_foto_perfil()
        
        opciones = [("Inicio", self.mostrar_inicio), 
                    ("Perfil", self.mostrar_perfil), 
                    ("Información", self.mostrar_informacion), 
                    ("Configuración", self.mostrar_configuracion),
                    ("Imágenes", self.mostrar_imagen)]  
        
        for texto, comando in opciones:
            boton = tk.Button(
                self.menu_lateral, text=texto, bg="#228B22", fg="white", font=("Arial", 12),
                relief="flat", command=comando
            )
            boton.pack(fill="x", pady=5)

        boton_salir = tk.Button(
            self.menu_lateral, text="Salir", bg="#B22222", fg="white", font=("Arial", 12),
            relief="flat", command=self.salir_aplicacion
        )
        boton_salir.pack(fill="x", pady=5, side="bottom")

    def cargar_foto_perfil(self):
        ruta_imagen_perfil = "IMG/USER.png"
        try:
            imagen_perfil = Image.open(ruta_imagen_perfil)
            imagen_perfil = imagen_perfil.resize((80, 80), Image.Resampling.LANCZOS)
            self.foto_perfil_img = ImageTk.PhotoImage(imagen_perfil)
            foto_perfil_label = tk.Label(self.menu_lateral, image=self.foto_perfil_img, bg="#32CD32")
            foto_perfil_label.pack(pady=20)
        except Exception as e:
            foto_perfil_label = tk.Label(self.menu_lateral, text="👦", bg="#32CD32", fg="white", font=("Arial", 30))
            foto_perfil_label.pack(pady=20)

        
        nombre_usuario_label = tk.Label(self.menu_lateral, text="LD_KL", bg="#32CD32", fg="white", font=("Arial", 12, "bold"))
        nombre_usuario_label.pack(pady=5)

        universidad_label = tk.Label(self.menu_lateral, text="UNITECNAR", bg="#32CD32", fg="white", font=("Arial", 12, "italic"))
        universidad_label.pack(pady=5)

    def crear_contenido_principal(self):
        self.frame_contenido = tk.Frame(self.root, bg="#F0F8FF")  
        self.frame_contenido.pack(side="right", expand=True, fill="both")
        self.cargar_imagen_en_frame()

    def cargar_imagen_en_frame(self):
        ruta_imagen = "IMG/LOGO.png"
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((300, 200), Image.Resampling.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(imagen)
        logo_label = tk.Label(self.frame_contenido, image=self.logo_img, bg="#F0F8FF")
        logo_label.pack(pady=50)

    def mostrar_correo(self):
        
        correo_label = tk.Label(self.root, text="LDKL2022@ejemplo.com", bg="#F0F8FF", fg="#228B22", font=("Arial", 12))
        correo_label.place(relx=1.0, rely=1.0, anchor="se", padx=20, pady=20)

    def limpiar_contenido(self):
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        self.limpiar_contenido()
        self.cargar_imagen_en_frame()
        inicio_label = tk.Label(self.frame_contenido, text="Bienvenido a la Aplicación Unitecnar", font=("Arial", 20, "bold"), bg="#F0F8FF", fg="#228B22")
        inicio_label.pack(pady=50)

    def mostrar_perfil(self):
        self.limpiar_contenido()
        perfil_label = tk.Label(self.frame_contenido, text="Perfil de Usuario", font=("Arial", 20, "bold"), bg="#F0F8FF", fg="#228B22")
        perfil_label.pack(pady=50)

    def mostrar_imagen(self):
        self.limpiar_contenido()
        imagen_label = tk.Label(self.frame_contenido, text="Sección de Imágenes", font=("Arial", 20, "bold"), bg="#EAF6F6", fg="#34495E")
        imagen_label.pack(pady=50)

    def mostrar_informacion(self):
        self.limpiar_contenido()
        info_label = tk.Label(self.frame_contenido, text="Información General", font=("Arial", 20, "bold"), bg="#F0F8FF", fg="#228B22")
        info_label.pack(pady=50)

    def mostrar_configuracion(self):
        self.limpiar_contenido()
        config_label = tk.Label(self.frame_contenido, text="Configuración de la Aplicación", font=("Arial", 20, "bold"), bg="#F0F8FF", fg="#228B22")
        config_label.pack(pady=50)

    def salir_aplicacion(self):
        self.root.quit()
