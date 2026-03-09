# Monitor de CPU y RAM con Sistema Tolerante a Fallas

## Descripción del Proyecto

Este proyecto consiste en una aplicación desarrollada en Python que permite monitorear el uso de los recursos del sistema, específicamente el CPU y la memoria RAM, mediante una interfaz gráfica. 

Además, el sistema implementa un mecanismo de **tolerancia a fallas** mediante un **servicio de Windows que funciona en segundo plano**, el cual se encarga de verificar continuamente el estado de la aplicación principal y reiniciarla automáticamente en caso de que se detenga.

El objetivo principal del proyecto es demostrar la implementación de:

- Procesos en segundo plano
- Monitoreo continuo
- Manejo de fallas
- Servicios del sistema operativo

---

# Análisis del problema y diseño del sistema

## Problema que se desea resolver

El problema que se busca resolver es la necesidad de monitorear continuamente el uso de los recursos del sistema, particularmente el CPU y la memoria RAM. Estos recursos son fundamentales para el correcto funcionamiento de cualquier computadora, y su monitoreo permite detectar situaciones de sobrecarga, fallas o comportamientos anómalos que puedan afectar el rendimiento del sistema.

Para atender esta necesidad se desarrolló una aplicación que permite visualizar en tiempo real el consumo de CPU y memoria RAM mediante una interfaz gráfica.

---

## Por qué requiere ejecución en segundo plano

El monitoreo de recursos debe realizarse de manera constante para que la información sea útil y actualizada. Debido a esto, el sistema necesita ejecutarse en segundo plano sin depender de la interacción directa del usuario.

Para lograrlo se implementó un **servicio del sistema operativo Windows** que funciona como un demonio. Este servicio se ejecuta de forma continua y se encarga de supervisar el estado de la aplicación principal.

De esta forma el sistema puede seguir funcionando incluso si el usuario no está utilizando activamente la aplicación.

---

## Qué tipo de falla podría ocurrir

Durante la ejecución del sistema pueden ocurrir diferentes tipos de fallas que provoquen que la aplicación principal deje de funcionar. Algunas de estas fallas pueden ser:

- Cierre accidental de la aplicación por parte del usuario
- Errores inesperados dentro del programa
- Terminación del proceso por el sistema operativo
- Problemas relacionados con los recursos del sistema

Cuando ocurre alguna de estas situaciones, la aplicación deja de ejecutarse y el monitoreo del sistema se interrumpe.

---

## Estrategia de tolerancia a fallas

Para garantizar la continuidad del sistema se implementó una estrategia de tolerancia a fallas basada en **monitoreo continuo y reinicio automático del proceso**.

El servicio de Windows revisa periódicamente si la aplicación principal se encuentra en ejecución. En caso de detectar que el proceso ha finalizado o que no está activo, el servicio inicia nuevamente la aplicación.

Esta estrategia permite mantener el sistema funcionando incluso ante fallas inesperadas, asegurando que el monitoreo de los recursos del sistema continúe disponible.

---

# Características del sistema

- Monitoreo del uso de **CPU en tiempo real**
- Monitoreo del uso de **memoria RAM**
- **Interfaz gráfica** desarrollada con Tkinter
- **Servicio de Windows ejecutándose en segundo plano**
- Reinicio automático de la aplicación en caso de falla
- Supervisión continua del estado del sistema

---

# Tecnologías utilizadas

El proyecto fue desarrollado utilizando las siguientes tecnologías:

- **Python 3**
- **Tkinter** para la interfaz gráfica
- **psutil** para obtener información del sistema
- **pywin32** para la creación de servicios en Windows

---

