import csv
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests

# Función para enviar datos a la API
def enviar_a_api(datos):
    # Esta función debe enviar los datos a la API
    print("Datos enviados a la API:", datos)

# Función para aplicar la lógica a cada valor de detección
def aplicar_logica(valor):
    if valor > 10:
        return 30
    elif valor > 5:
        return 20
    elif valor > 2:
        return 15
    elif valor > 0:
        return 10
    elif valor == 0:
        return 0

# Función para actualizar las detecciones y enviar los datos a la API
def actualizar_detecciones(linea):
    if len(linea) == 2:
        deteccion1, tiempo = map(int, linea)
        deteccion1 = aplicar_logica(deteccion1)
        print(f"deteccion1: {deteccion1}")
        for _ in range(tiempo):  # Actualizar cada segundo durante 15 segundos
            datos_actuales = {'deteccion1': deteccion1}
            enviar_a_api(datos_actuales)
            r = requests.post(f"http://localhost:5030/escribir_deteccion1?s={deteccion1}")
            time.sleep(1)
    elif len(linea) == 3:
        deteccion1, deteccion2, tiempo = map(int, linea)
        deteccion1 = aplicar_logica(deteccion1)
        deteccion2 = aplicar_logica(deteccion2)
        print(f"deteccion1: {deteccion1}")
        print(f"deteccion2: {deteccion2}")
        for _ in range(tiempo):  # Actualizar cada segundo durante 15 segundos
            datos_actuales = {'deteccion1': deteccion1, 'deteccion2': deteccion2}
            enviar_a_api(datos_actuales)
            r = requests.post(f"http://localhost:5030/escribir_deteccion1?s={deteccion1}")
            r = requests.post(f"http://localhost:5030/escribir_deteccion2?s={deteccion2}")
            time.sleep(1)
    elif len(linea) == 4:
        deteccion1, deteccion2, deteccion3, tiempo = map(int, linea)
        deteccion1 = aplicar_logica(deteccion1)
        deteccion2 = aplicar_logica(deteccion2)
        deteccion3 = aplicar_logica(deteccion3)
        print(f"deteccion1: {deteccion1}")
        print(f"deteccion2: {deteccion2}")
        print(f"deteccion3: {deteccion3}")
        for _ in range(tiempo):  # Actualizar cada segundo durante 15 segundos
            datos_actuales = {'deteccion1': deteccion1, 'deteccion2': deteccion2, 'deteccion3': deteccion3}
            enviar_a_api(datos_actuales)
            r = requests.post(f"http://localhost:5030/escribir_deteccion1?s={deteccion1}")
            r = requests.post(f"http://localhost:5030/escribir_deteccion2?s={deteccion2}")
            r = requests.post(f"http://localhost:5030/escribir_deteccion3?s={deteccion3}")
            time.sleep(1)
    elif len(linea) == 5:
        deteccion1, deteccion2, deteccion3, deteccion4, tiempo = map(int, linea)
        deteccion1 = aplicar_logica(deteccion1)
        deteccion2 = aplicar_logica(deteccion2)
        deteccion3 = aplicar_logica(deteccion3)
        deteccion4 = aplicar_logica(deteccion4)
        print(f"deteccion1: {deteccion1}")
        print(f"deteccion2: {deteccion2}")
        print(f"deteccion3: {deteccion3}")
        print(f"deteccion4: {deteccion4}")
        for _ in range(tiempo):  # Actualizar cada segundo durante 15 segundos
            datos_actuales = {'deteccion1': deteccion1, 'deteccion2': deteccion2, 'deteccion3': deteccion3, 'deteccion4': deteccion4}
            enviar_a_api(datos_actuales)
            r = requests.post(f"http://localhost:5030/escribir_deteccion1?s={deteccion1}")
            r = requests.post(f"http://localhost:5030/escribir_deteccion2?s={deteccion2}")
            r = requests.post(f"http://localhost:5030/escribir_deteccion3?s={deteccion3}")
            r = requests.post(f"http://localhost:5030/escribir_deteccion4?s={deteccion4}")
            time.sleep(1)
    else:
        print("La línea no tiene un número válido de valores:", linea)

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Cuando el archivo CSV se modifica, se ejecuta esta función
        with open('datos.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for linea in reader:
                actualizar_detecciones(linea)

# Función para iniciar la vigilancia del archivo CSV
def iniciar_vigilancia():
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

# Función para iniciar el hilo de actualización de detecciones
def iniciar_actualizacion():
    while True:  # Bucle infinito para mantener la lectura continua del archivo CSV
        with open('datos.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for linea in reader:
                actualizar_detecciones(linea)
        time.sleep(1)  # Espera un segundo antes de comenzar a leer el archivo nuevamente

# Iniciar el proceso de actualización
iniciar_actualizacion()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
