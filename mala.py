import customtkinter as ctk
import sqlite3

# ------------------- BASE DE DATOS -------------------

def crear_base_datos():
    conn = sqlite3.connect("ahorcado.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS palabras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        palabra TEXT NOT NULL,
        descripcion TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

crear_base_datos()

# Conexión global
conn = sqlite3.connect("ahorcado.db")
cursor = conn.cursor()

# ------------------- CONFIGURACIÓN -------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# ------------------- VENTANA PRINCIPAL -------------------

def v_principal():
    app = ctk.CTk()
    app.title("Juego Ahorcado")
    app.geometry("400x300")

    lbl = ctk.CTkLabel(app, text="BIENVENIDO", font=("Arial", 20))
    lbl.pack(pady=20)

    btn_jugar = ctk.CTkButton(app, text="JUGAR", command=lambda: [app.destroy(), v_juego()])
    btn_jugar.pack(pady=10)

    btn_salir = ctk.CTkButton(app, text="SALIR", command=app.destroy)
    btn_salir.pack(pady=10)

    app.mainloop()

# ------------------- VENTANA JUEGO -------------------

def v_juego(intentos=5):
    app = ctk.CTk()
    app.title("Juego")
    app.geometry("500x400")

    # Obtener palabra aleatoria
    cursor.execute("SELECT palabra, descripcion FROM palabras ORDER BY RANDOM() LIMIT 1")
    resultado = cursor.fetchone()
    palabra = resultado[0] if resultado else "------"
    descripcion = resultado[1] if resultado else "No hay palabras aún."

    top = ctk.CTkFrame(app)
    top.pack(pady=10)

    btn_add = ctk.CTkButton(top, text="AGREGAR PALABRA", command=lambda: [app.destroy(), v_nueva()])
    btn_add.grid(row=0, column=0, padx=5)

    btn_new = ctk.CTkButton(top, text="NUEVA PALABRA", command=lambda: [app.destroy(), v_juego()])
    btn_new.grid(row=0, column=1, padx=5)

    btn_del = ctk.CTkButton(top, text="ELIMINAR PALABRA", command=lambda: [app.destroy(), v_eliminar()])
    btn_del.grid(row=0, column=2, padx=5)

    lbl_desc = ctk.CTkLabel(app, text=f"DESCRIPCIÓN: {descripcion}")
    lbl_desc.pack(anchor="w", padx=20)
    lbl_num_letras = ctk.CTkLabel(app, text=f"NÚMERO DE LETRAS: {len(palabra)}")
    lbl_num_letras.pack(anchor="w", padx=20)
    lbl_intentos = ctk.CTkLabel(app, text=f"INTENTOS RESTANTES: {intentos}")
    lbl_intentos.pack(anchor="w", padx=20)

    ent = ctk.CTkEntry(app, width=300)
    ent.pack(pady=10)

    mensaje_error = ctk.CTkLabel(app, text="", text_color="red")
    mensaje_error.pack()

    def verificar_palabra():
        nonlocal intentos  # para modificar variable externa

        intento = ent.get().strip().lower()
        if intento == palabra.lower():
            app.destroy()
            v_ganar()
        else:
            intentos -= 1
            if intentos <= 0:
                app.destroy()
                v_perder()
            else:
                lbl_intentos.configure(text=f"INTENTOS RESTANTES: {intentos}")
                ent.delete(0, ctk.END)
                mensaje_error.configure(text="¡Palabra incorrecta! Intenta de nuevo.")

    btn_play = ctk.CTkButton(app, text="JUGAR", command=verificar_palabra)
    btn_play.pack(pady=5)

    btn_exit = ctk.CTkButton(app, text="SALIR", command=lambda: [app.destroy(), v_confirmar()])
    btn_exit.pack(pady=5)

    app.mainloop()

# ------------------- VENTANA NUEVA PALABRA -------------------

def v_nueva():
    app = ctk.CTk()
    app.title("Nueva Palabra")
    app.geometry("300x200")

    ctk.CTkLabel(app, text="NUEVA PALABRA").pack(pady=5)
    ent_pal = ctk.CTkEntry(app)
    ent_pal.pack(pady=5)

    ctk.CTkLabel(app, text="DESCRIPCIÓN").pack(pady=5)
    ent_desc = ctk.CTkEntry(app)
    ent_desc.pack(pady=5)

    def guardar_palabra():
        palabra = ent_pal.get().strip()
        descripcion = ent_desc.get().strip()
        if palabra and descripcion:
            cursor.execute("INSERT INTO palabras (palabra, descripcion) VALUES (?, ?)", (palabra, descripcion))
            conn.commit()
        app.destroy()
        v_juego()

    frame = ctk.CTkFrame(app)
    frame.pack(pady=10)

    btn_can = ctk.CTkButton(frame, text="CANCELAR", command=lambda: [app.destroy(), v_juego()])
    btn_can.grid(row=0, column=0, padx=5)

    btn_ok = ctk.CTkButton(frame, text="OK", command=guardar_palabra)
    btn_ok.grid(row=0, column=1, padx=5)

    app.mainloop()

# ------------------- VENTANA ELIMINAR PALABRA -------------------

def v_eliminar():
    app = ctk.CTk()
    app.title("Eliminar Palabra")
    app.geometry("300x150")

    ctk.CTkLabel(app, text="INGRESA LA PALABRA A ELIMINAR").pack(pady=5)
    ent_del = ctk.CTkEntry(app)
    ent_del.pack(pady=5)

    def eliminar_palabra():
        palabra = ent_del.get().strip()
        if palabra:
            cursor.execute("DELETE FROM palabras WHERE palabra = ?", (palabra,))
            conn.commit()
        app.destroy()
        v_juego()

    frame = ctk.CTkFrame(app)
    frame.pack(pady=10)

    btn_can = ctk.CTkButton(frame, text="CANCELAR", command=lambda: [app.destroy(), v_juego()])
    btn_can.grid(row=0, column=0, padx=5)

    btn_ok = ctk.CTkButton(frame, text="OK", command=eliminar_palabra)
    btn_ok.grid(row=0, column=1, padx=5)

    app.mainloop()

# ------------------- VENTANA CONFIRMAR SALIDA -------------------

def v_confirmar():
    app = ctk.CTk()
    app.title("Confirmar salida")
    app.geometry("300x150")

    ctk.CTkLabel(app, text="¿ESTÁS SEGURO DE SALIR?").pack(pady=10)

    frame = ctk.CTkFrame(app)
    frame.pack(pady=10)

    def salir():
        conn.close()
        app.destroy()

    btn_can = ctk.CTkButton(frame, text="CANCELAR", command=lambda: [app.destroy(), v_juego()])
    btn_can.grid(row=0, column=0, padx=5)

    btn_ok = ctk.CTkButton(frame, text="OK", command=salir)
    btn_ok.grid(row=0, column=1, padx=5)

    app.mainloop()

# ------------------- VENTANA GANASTE -------------------

def v_ganar():
    app = ctk.CTk()
    app.title("Ganaste")
    app.geometry("300x150")

    ctk.CTkLabel(app, text="¡GANASTE! ¿QUIERES JUGAR OTRA VEZ?").pack(pady=10)

    frame = ctk.CTkFrame(app)
    frame.pack(pady=10)

    btn_can = ctk.CTkButton(frame, text="CANCELAR", command=app.destroy)
    btn_can.grid(row=0, column=0, padx=5)

    btn_ok = ctk.CTkButton(frame, text="OK", command=lambda: [app.destroy(), v_juego()])
    btn_ok.grid(row=0, column=1, padx=5)

    app.mainloop()

# ------------------- VENTANA PERDISTE -------------------

def v_perder():
    app = ctk.CTk()
    app.title("Perdiste")
    app.geometry("300x150")

    ctk.CTkLabel(app, text="PERDISTE, ¿QUIERES JUGAR DE NUEVO?").pack(pady=10)

    frame = ctk.CTkFrame(app)
    frame.pack(pady=10)

    btn_can = ctk.CTkButton(frame, text="CANCELAR", command=app.destroy)
    btn_can.grid(row=0, column=0, padx=5)

    btn_ok = ctk.CTkButton(frame, text="OK", command=lambda: [app.destroy(), v_juego()])
    btn_ok.grid(row=0, column=1, padx=5)

    app.mainloop()

# ------------------- INICIAR PROGRAMA -------------------

v_principal()
