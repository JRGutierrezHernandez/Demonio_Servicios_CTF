import psutil
import time

print("Monitor de CPU y RAM iniciado")

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    print(f"Uso de CPU: {cpu}%")
    print(f"Uso de RAM: {ram}%")
    print("--------------------")

    time.sleep(2)