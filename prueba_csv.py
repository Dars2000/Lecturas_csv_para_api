import csv
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests

# Función para enviar datos a la API
def enviar_a_api(datos):
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

# Función para actualizar una línea específica en el archivo CSV
def actualizar_linea_csv(linea_index, datos):
    with open('resultados.csv', 'r', newline='') as csvfile:
        reader = list(csv.reader(csvfile))

    # Asegurar que la longitud de reader sea al menos linea_index + 1
    while len(reader) <= linea_index:
        reader.append([])

    # Actualizar la línea correspondiente
    reader[linea_index] = datos

    with open('resultados.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(reader)

# Función para actualizar las detecciones y enviar los datos a la API
def actualizar_detecciones(linea, linea_index):
    if len(linea) == 2:
        deteccion1, tiempo = map(int, linea)
        deteccion1 = aplicar_logica(deteccion1)
        print(f"deteccion1: {deteccion1}")
        print(f"tiempo asignado: {tiempo}")
        for _ in range(tiempo):
            datos_actuales = {'deteccion1': deteccion1}
            enviar_a_api(datos_actuales)
            requests.post(f"http://localhost:5030/escribir_deteccion1?s={deteccion1}")
            time.sleep(1)
        actualizar_linea_csv(linea_index, [deteccion1])
    elif len(linea) == 3:
        deteccion1, deteccion2, tiempo = map(int, linea)
        deteccion1 = aplicar_logica(deteccion1)
        deteccion2 = aplicar_logica(deteccion2)
        print(f"deteccion1: {deteccion1}")
        print(f"deteccion2: {deteccion2}")
        print(f"tiempo asignado: {tiempo}")
        for _ in range(tiempo):
            datos_actuales = {'deteccion1': deteccion1, 'deteccion2': deteccion2}
            enviar_a_api(datos_actuales)
            requests.post(f"http://localhost:5030/escribir_deteccion1?s={deteccion1}")
            requests.post(f"http://localhost:5030/escribir_deteccion2?s={deteccion2}")
            time.sleep(1)
        actualizar_linea_csv(linea_index, [deteccion1, deteccion2])
    elif len(linea) == 4:
        deteccion1, deteccion2, deteccion3, tiempo = map(int, linea)
        deteccion1 = aplicar_logica(deteccion1)
        deteccion2 = aplicar_logica(deteccion2)
        deteccion3 = aplicar_logica(deteccion3)
        print(f"deteccion1: {deteccion1}")
        print(f"deteccion2: {deteccion2}")
        print(f"deteccion3: {deteccion3}")
        print(f"tiempo asignado: {tiempo}")
        for _ in range(tiempo):
            datos_actuales = {'deteccion1': deteccion1, 'deteccion2': deteccion2, 'deteccion3': deteccion3}
            enviar_a_api(datos_actuales)
            requests.post(f"http://localhost:5030/escribir_deteccion1?s={deteccion1}")
            requests.post(f"http://localhost:5030/escribir_deteccion2?s={deteccion2}")
            requests.post(f"http://localhost:5030/escribir_deteccion3?s={deteccion3}")
            time.sleep(1)
        actualizar_linea_csv(linea_index, [deteccion1, deteccion2, deteccion3])
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
        print(f"tiempo asignado: {tiempo}")
        for _ in range(tiempo):
            datos_actuales = {'deteccion1': deteccion1, 'deteccion2': deteccion2, 'deteccion3': deteccion3, 'deteccion4': deteccion4}
            enviar_a_api(datos_actuales)
            requests.post(f"http://localhost:5030/escribir_deteccion1?s={deteccion1}")
            requests.post(f"http://localhost:5030/escribir_deteccion2?s={deteccion2}")
            requests.post(f"http://localhost:5030/escribir_deteccion3?s={deteccion3}")
            requests.post(f"http://localhost:5030/escribir_deteccion4?s={deteccion4}")
            time.sleep(1)
        actualizar_linea_csv(linea_index, [deteccion1, deteccion2, deteccion3, deteccion4])
    else:
        print("La línea no tiene un número válido de valores:", linea)

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with open('datos.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for index, linea in enumerate(reader):
                actualizar_detecciones(linea, index)

def iniciar_vigilancia():
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

def iniciar_actualizacion():
    while True:
        with open('datos.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for index, linea in enumerate(reader):
                actualizar_detecciones(linea, index)
        time.sleep(1)

# Iniciar el proceso de actualización
iniciar_actualizacion()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
