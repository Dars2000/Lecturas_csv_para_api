import csv
import time
import threading

# Variables para almacenar los valores de los semáforos
semaforo1 = 0
semaforo2 = 0
semaforo3 = 0
semaforo4 = 0

# Función para enviar datos a la API
def enviar_a_api(datos):
    # Esta función debe enviar los datos a la API
    print("Datos enviados a la API:", datos)

# Función para actualizar los semáforos y enviar los datos a la API
def actualizar_sem_y_enviar(lineas):
    global semaforo1, semaforo2, semaforo3, semaforo4
    for linea in lineas:
        semaforo1, semaforo2, semaforo3, semaforo4 = map(int, linea[:4])
        print("semaforo1:", semaforo1)
        print("semaforo2:", semaforo2)
        print("semaforo3:", semaforo3)
        print("semaforo4:", semaforo4)
        for _ in range(15):  # Actualizar cada segundo durante 15 segundos
            datos_actuales = {'semaforo1': semaforo1, 'semaforo2': semaforo2, 'semaforo3': semaforo3, 'semaforo4': semaforo4}
            enviar_a_api(datos_actuales)
            time.sleep(1)
        time.sleep(1)  # Esperar 1 segundo antes de pasar a la siguiente línea

# Función para iniciar el hilo de actualización de semáforos
def iniciar_actualizacion():
    with open('datos.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Salta la primera línea que contiene encabezados
        lineas = list(reader)  # Convertir el lector CSV a una lista de líneas
        primera_linea = lineas[0]  # Obtener la primera línea
        lineas_restantes = lineas[1:]  # Obtener las líneas restantes
        hilo_primera_linea = threading.Thread(target=actualizar_sem_y_enviar, args=(primera_linea,))
        hilo_primera_linea.start()  # Iniciar hilo para actualizar la primera línea
        for linea in lineas_restantes:  # Actualizar el resto de las líneas
            semaforo1, semaforo2, semaforo3, semaforo4 = map(int, linea[:4])
            print("semaforo1:", semaforo1)
            print("semaforo2:", semaforo2)
            print("semaforo3:", semaforo3)
            print("semaforo4:", semaforo4)
            datos_actuales = {'semaforo1': semaforo1, 'semaforo2': semaforo2, 'semaforo3': semaforo3, 'semaforo4': semaforo4}
            enviar_a_api(datos_actuales)
            time.sleep(1)  # Esperar 1 segundo antes de leer la siguiente línea del archivo CSV

# Iniciar el proceso de actualización
iniciar_actualizacion()
