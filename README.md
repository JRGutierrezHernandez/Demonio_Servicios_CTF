## Análisis del problema y diseño del sistema

### Problema que se desea resolver

El problema que se busca resolver es la necesidad de monitorear continuamente el uso de los recursos del sistema, específicamente el CPU y la memoria RAM. En muchos sistemas es importante supervisar estos recursos para detectar posibles problemas de rendimiento, sobrecarga del sistema o comportamientos anómalos que puedan afectar el funcionamiento de otras aplicaciones.

Para solucionar este problema se desarrolló una aplicación que permite visualizar en tiempo real el consumo de CPU y memoria RAM mediante una interfaz gráfica.

---

### Por qué requiere ejecución en segundo plano

El sistema requiere ejecutarse en segundo plano porque el monitoreo debe realizarse de forma continua, incluso si el usuario no está interactuando directamente con la aplicación. 

Para lograr esto se implementó un servicio del sistema operativo que funciona como un demonio de monitoreo. Este servicio se ejecuta en segundo plano y se encarga de verificar periódicamente si la aplicación principal sigue en ejecución.

De esta manera se garantiza que el sistema de monitoreo permanezca activo y disponible en todo momento.

---

### Qué tipo de falla podría ocurrir

Una posible falla que podría ocurrir es que la aplicación principal deje de ejecutarse debido a diferentes factores, como:

- Cierre accidental por parte del usuario
- Error inesperado del programa
- Fallos del sistema operativo
- Terminación del proceso por falta de recursos

Cuando esto sucede, el sistema de monitoreo deja de funcionar y se pierde la supervisión de los recursos del sistema.

---

### Estrategia de tolerancia a fallas

Para resolver este problema se implementó una estrategia de tolerancia a fallas basada en monitoreo continuo y reinicio automático del proceso.

Un servicio de Windows se encarga de revisar periódicamente si la aplicación principal está activa. Si el servicio detecta que la aplicación no se encuentra en ejecución, automáticamente inicia nuevamente el proceso.

Esta estrategia permite garantizar la disponibilidad del sistema de monitoreo y reducir el impacto de fallas inesperadas.
