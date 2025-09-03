import customtkinter as ctk
# Configuración general
ctk.set_appearance_mode("dark") # Fondo negro
ctk.set_default_color_theme("dark-blue")
# -------- Ventana Principal --------
def v_principal():
 app = ctk.CTk()
 app.title("Juego Ahorcado")
 app.geometry("400x300")
 lbl = ctk.CTkLabel(app, text="BIENVENIDO", font=("Arial", 20))
 lbl.pack(pady=20)
 btn_jugar = ctk.CTkButton(app, text="JUGAR", command=lambda: [app.destroy(),
v_juego()])
 btn_jugar.pack(pady=10)
 btn_salir = ctk.CTkButton(app, text="SALIR", command=app.destroy)
 btn_salir.pack(pady=10)
 app.mainloop()
# -------- Ventana Juego --------
def v_juego():
 app = ctk.CTk()
 app.title("Juego")
 app.geometry("500x400")
 top = ctk.CTkFrame(app)
 top.pack(pady=10)
 btn_add = ctk.CTkButton(top, text="AGREGAR PALABRA", command=lambda:
[app.destroy(), v_nueva()])
 btn_add.grid(row=0, column=0, padx=5)
 btn_new = ctk.CTkButton(top, text="NUEVA PALABRA")
 btn_new.grid(row=0, column=1, padx=5)
 btn_del = ctk.CTkButton(top, text="ELIMINAR PALABRA", command=lambda:
[app.destroy(), v_eliminar()])
 btn_del.grid(row=0, column=2, padx=5)
 ctk.CTkLabel(app, text="DESCRIPCION:").pack(anchor="w", padx=20)
 ctk.CTkLabel(app, text="NUMERO DE LETRAS:").pack(anchor="w", padx=20)
 ctk.CTkLabel(app, text="INTENTOS RESTANTES:").pack(anchor="w", padx=20)
 ent = ctk.CTkEntry(app, width=300)
 ent.pack(pady=10)
 btn_play = ctk.CTkButton(app, text="JUGAR", command=lambda: [app.destroy(),
v_ganar()])
 btn_play.pack(pady=5)
 btn_exit = ctk.CTkButton(app, text="SALIR", command=lambda: [app.destroy(),
v_confirmar()])
 btn_exit.pack(pady=5)
 app.mainloop()
# -------- Ventana Nueva Palabra --------
def v_nueva():
 app = ctk.CTk()
 app.title("Nueva Palabra")
 app.geometry("300x200")
 ctk.CTkLabel(app, text="NUEVA PALABRA").pack(pady=5)
 ent_pal = ctk.CTkEntry(app)
 ent_pal.pack(pady=5)
 ctk.CTkLabel(app, text="DESCRIPCION").pack(pady=5)
 ent_desc = ctk.CTkEntry(app)
 ent_desc.pack(pady=5)
 frame = ctk.CTkFrame(app)
 frame.pack(pady=10)
 btn_can = ctk.CTkButton(frame, text="CANCELAR", command=lambda:
[app.destroy(), v_juego()])
 btn_can.grid(row=0, column=0, padx=5)
 btn_ok = ctk.CTkButton(frame, text="OK", command=lambda: [app.destroy(),
v_juego()])
 btn_ok.grid(row=0, column=1, padx=5)
 app.mainloop()
# -------- Ventana Eliminar --------
def v_eliminar():
 app = ctk.CTk()
 app.title("Eliminar Palabra")
 app.geometry("300x150")
 ctk.CTkLabel(app, text="INGRESA LA PALABRA A ELIMINAR").pack(pady=5)
 ent_del = ctk.CTkEntry(app)
 ent_del.pack(pady=5)
 frame = ctk.CTkFrame(app)
 frame.pack(pady=10)
 btn_can = ctk.CTkButton(frame, text="CANCELAR", command=lambda:
[app.destroy(), v_juego()])
 btn_can.grid(row=0, column=0, padx=5)
 btn_ok = ctk.CTkButton(frame, text="OK", command=lambda: [app.destroy(),
v_juego()])
 btn_ok.grid(row=0, column=1, padx=5)
 app.mainloop()
# -------- Ventana Confirmar Salida --------
def v_confirmar():
 app = ctk.CTk()
 app.title("Confirmar salida")
 app.geometry("300x150")
 ctk.CTkLabel(app, text="¿ESTÁS SEGURO DE SALIR?").pack(pady=10)
 frame = ctk.CTkFrame(app)
 frame.pack(pady=10)
 btn_can = ctk.CTkButton(frame, text="CANCELAR", command=lambda:
[app.destroy(), v_juego()])
 btn_can.grid(row=0, column=0, padx=5)
 btn_ok = ctk.CTkButton(frame, text="OK", command=app.destroy)
 btn_ok.grid(row=0, column=1, padx=5)
 app.mainloop()
# -------- Ventana Ganaste --------
def v_ganar():
 app = ctk.CTk()
 app.title("Ganaste")
 app.geometry("300x150")
 ctk.CTkLabel(app, text="¡GANASTE! ¿QUIERES JUGAR OTRA VEZ?").pack(pady=10)
 frame = ctk.CTkFrame(app)
 frame.pack(pady=10)
 btn_can = ctk.CTkButton(frame, text="CANCELAR", command=app.destroy)
 btn_can.grid(row=0, column=0, padx=5)
 btn_ok = ctk.CTkButton(frame, text="OK", command=lambda: [app.destroy(),
v_juego()])
 btn_ok.grid(row=0, column=1, padx=5)
 app.mainloop()
# -------- Venta------------na Perdiste --------
def v_perder():
 app = ctk.CTk()
 app.title("Perdiste")
 app.geometry("300x150")
 ctk.CTkLabel(app, text="PERDISTE, ¿QUIERES JUGAR DE NUEVO?").pack(pady=10)
 frame = ctk.CTkFrame(app)
 frame.pack(pady=10)
 btn_can = ctk.CTkButton(frame, text="CANCELAR", command=app.destroy)
 btn_can.grid(row=0, column=0, padx=5)
 btn_ok = ctk.CTkButton(frame, text="OK", command=lambda: [app.destroy(),
v_juego()])
 btn_ok.grid(row=0, column=1, padx=5)
 app.mainloop()
# -------- Iniciar Programa --------
v_principal()
