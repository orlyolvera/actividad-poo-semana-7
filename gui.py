import tkinter as tk
from tkinter import messagebox
from repository import ClienteRepository
from modelos import Cliente

repository = ClienteRepository("clientes.json")

def actualizar():
    lista.delete(0, tk.END)
    for cliente in repository.listar_clientes():
        lista.insert(tk.END, str(cliente))
    cantidad.set(f"Clientes en espera: {repository.cantidad_clientes()}")

def agregar():
    c, n, t = codigo.get().strip(), nombre.get().strip(), tramite.get().strip()
    if not c or not n or not t:
        messagebox.showwarning("Datos incompletos", "Complete todos los campos.")
        return
    repository.agregar_cliente(Cliente(c, n, t))
    codigo.delete(0, tk.END); nombre.delete(0, tk.END); tramite.delete(0, tk.END)
    actualizar()
    messagebox.showinfo("Sistema", "Cliente agregado correctamente.")

def consultar():
    cliente = repository.siguiente_cliente()
    messagebox.showinfo("Siguiente cliente", str(cliente) if cliente else "No hay clientes en espera.")

def atender():
    cliente = repository.atender_cliente()
    messagebox.showinfo("Atención", f"Cliente atendido:\n{cliente}" if cliente else "No hay clientes en espera.")
    actualizar()

ventana = tk.Tk()
ventana.title("Sistema de Atención de Clientes")
ventana.geometry("760x560")
tk.Label(ventana, text="SISTEMA DE ATENCIÓN DE CLIENTES", font=("Arial", 20, "bold")).pack(pady=18)

form = tk.Frame(ventana); form.pack()
for i, texto in enumerate(("Código:", "Nombre:", "Trámite:")):
    tk.Label(form, text=texto, width=12, anchor="e").grid(row=i, column=0, padx=5, pady=5)

codigo = tk.Entry(form, width=35); codigo.grid(row=0, column=1)
nombre = tk.Entry(form, width=35); nombre.grid(row=1, column=1)
tramite = tk.Entry(form, width=35); tramite.grid(row=2, column=1)

botones = tk.Frame(ventana); botones.pack(pady=15)
tk.Button(botones, text="Agregar cliente", width=20, command=agregar).grid(row=0,column=0,padx=5,pady=5)
tk.Button(botones, text="Consultar siguiente", width=20, command=consultar).grid(row=0,column=1,padx=5,pady=5)
tk.Button(botones, text="Atender siguiente", width=20, command=atender).grid(row=1,column=0,padx=5,pady=5)
tk.Button(botones, text="Actualizar lista", width=20, command=actualizar).grid(row=1,column=1,padx=5,pady=5)

cantidad = tk.StringVar()
tk.Label(ventana, textvariable=cantidad, font=("Arial", 13, "bold")).pack(pady=8)
lista = tk.Listbox(ventana, width=82, height=12, font=("Consolas", 11)); lista.pack(padx=20)
tk.Button(ventana, text="Salir", width=20, command=ventana.destroy).pack(pady=10)

actualizar()
codigo.focus()
ventana.mainloop()
