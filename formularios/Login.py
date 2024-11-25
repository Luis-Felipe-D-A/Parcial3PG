import tkinter as tk
from tkinter import messagebox
from formularios.UnitecnarApp import *

class Login(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("INGRESO AL SISTEMA")
        self.resizable(False, False)
        self.geometry("800x500")  
        self.centrar_ventana(self, 800, 500)
        
        
        self.logo = self.leer_imagen("IMG/LOGO.png", (300, 100))
        self.user = self.leer_imagen("IMG/login.png", (64, 64))
        
        
        self.frame_logo = tk.Frame(self, bd=0, width=300, relief=tk.SOLID)
        self.frame_logo.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
        self.llogo = tk.Label(self.frame_logo, image=self.logo)
        self.llogo.pack(padx=5, pady=150)

        
        self.frame_form = tk.Frame(self, bd=0, relief=tk.SOLID)
        self.frame_form.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)
        
        self.texto = tk.Label(self.frame_form, text="INGRESO AL SISTEMA", font=('Times', 20))
        self.texto.pack(padx=10, pady=10)
        
        self.imglogin = tk.Label(self.frame_form, image=self.user)
        self.imglogin.pack(padx=10, pady=10)
        
        self.lusuario = tk.Label(self.frame_form, text="Usuario:", font=('Times', 14))
        self.lusuario.pack(padx=10, pady=5)
        
        self.cusuario = tk.Entry(self.frame_form, width=30, font=('Times', 12))
        self.cusuario.pack(fill=tk.X, padx=10, pady=10)
        self.cusuario.focus()

        self.lclave = tk.Label(self.frame_form, text="Clave:", font=('Times', 14))
        self.lclave.pack(fill=tk.X, padx=10, pady=5)

        self.cclave = tk.Entry(self.frame_form, width=30, font=('Times', 12), show="*")
        self.cclave.pack(fill=tk.X, padx=10, pady=10)

        self.bregistrar = tk.Button(self.frame_form, text="\uf082 Iniciar sesión", font=('Times', 16), command=self.validar)
        self.bregistrar.pack(fill=tk.X, padx=10, pady=10)

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

    def validar(self):
        usuario = self.cusuario.get()
        clave = self.cclave.get()

        if usuario == "admin" and clave == "admin123":
            messagebox.showinfo("Éxito", "Bienvenido!")
            self.mostrar_unitecnar_app()
        else:
            messagebox.showerror("Error", "Usuario o clave incorrectos")

    def mostrar_unitecnar_app(self):
        self.destroy()  
        unitecnar_app = UnitecnarApp(tk.Tk())  
        unitecnar_app.mainloop()  
