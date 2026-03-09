import psutil
import subprocess
import time

APP = "monitor_app_gui.py"

def app_activa():

    for proceso in psutil.process_iter(['cmdline']):
        try:
            if APP in str(proceso.info['cmdline']):
                return True
        except:
            pass

    return False


def iniciar_app():
    subprocess.Popen(["python", APP])


print("Demonio iniciado")

while True:

    if not app_activa():

        print("La aplicación no está activa. Reiniciando...")
        iniciar_app()

    else:
        print("La aplicación está funcionando")

    time.sleep(5)