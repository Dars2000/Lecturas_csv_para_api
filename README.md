<h1>Sistema de Detección en Tiempo Real</h1>
<p>Este repositorio contiene tres archivos principales relacionados con un sistema de detección y una API para gestionar los datos de detección en tiempo real. A continuación, se proporciona una descripción de cada archivo y su funcionalidad:</p>
<ul>
<li><code>API-Prueba.py</code>: Este archivo contiene el código para una API web que permite leer y escribir datos de detección en un sistema de detección en tiempo real. La API está construida con FastAPI y utiliza hilos para manejar la concurrencia.</li>
<li><code>datos.csv</code>: Este archivo CSV contiene datos de detección simulados que se utilizan para actualizar la API en tiempo real. Cada línea del archivo representa un conjunto de datos de detección.</li>
<li><code>prueba_csv.py</code>: Este archivo Python se encarga de leer los datos del archivo CSV y enviarlos a la API en tiempo real para su procesamiento. También incluye lógica para aplicar reglas específicas a los datos de detección antes de enviarlos a la API.</li>
</ul>
<h2>Instrucciones de Uso</h2>
<ol>
<li>Clonar el repositorio
<li>Ejecutar el archivo <code>API-Prueba.py</code> para iniciar la API: <code>python API-Prueba.py</code>.</li>
<li>Ejecutar el archivo <code>prueba_csv.py</code> para comenzar a enviar datos de detección a la API</li>
<li>Los datos de detección se enviarán a la API en tiempo real y se procesarán según las reglas definidas en <code>prueba_csv.py</code>.</li>
</ol>
<p>¡Eso es todo! Ahora puedes utilizar este sistema para gestionar datos de detección en tiempo real mediante una API web.</p>
</div>
