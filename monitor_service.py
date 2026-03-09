import win32serviceutil
import win32service
import win32event
import subprocess
import psutil
import time

APP = "monitor_app_gui.py"

class MonitorService(win32serviceutil.ServiceFramework):

    _svc_name_ = "MonitorCPUService"
    _svc_display_name_ = "Servicio Monitor CPU y RAM"

    def __init__(self,args):

        win32serviceutil.ServiceFramework.__init__(self,args)
        self.stop_event = win32event.CreateEvent(None,0,0,None)

    def SvcStop(self):

        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):

        while True:

            activo = False

            for p in psutil.process_iter(['cmdline']):
                try:
                    if APP in str(p.info['cmdline']):
                        activo = True
                except:
                    pass

            if not activo:
                subprocess.Popen(["python", APP])

            time.sleep(5)


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(MonitorService)