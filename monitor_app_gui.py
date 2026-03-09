import tkinter as tk
import psutil

def actualizar():

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    etiqueta_cpu.config(text=f"CPU: {cpu}%")
    etiqueta_ram.config(text=f"RAM: {ram}%")

    barra_cpu["value"] = cpu
    barra_ram["value"] = ram

    ventana.after(1000, actualizar)


ventana = tk.Tk()
ventana.title("Monitor del Sistema")
ventana.geometry("300x200")

titulo = tk.Label(ventana, text="Monitor de CPU y RAM", font=("Arial",14))
titulo.pack(pady=10)

etiqueta_cpu = tk.Label(ventana, text="CPU: 0%")
etiqueta_cpu.pack()

from tkinter.ttk import Progressbar

barra_cpu = Progressbar(ventana,length=200,maximum=100)
barra_cpu.pack(pady=5)

etiqueta_ram = tk.Label(ventana, text="RAM: 0%")
etiqueta_ram.pack()

barra_ram = Progressbar(ventana,length=200,maximum=100)
barra_ram.pack(pady=5)

actualizar()

ventana.mainloop()