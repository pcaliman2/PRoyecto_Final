# PROYECTO FINAL DEL BOOTCAMP: Predictor de Precio de Vehiculos de Segunda mano

El objetivo de este proyecto es la implementacion de un predictor de precio de Vehiculos de Segunda mano. Los datos para el predictor vienen de estadisticas suministrados por la plataforma Kaggle.

La versión implementada de este proyecto se encuentra en el siguiente url;

https://proyectofinal-production-8943.up.railway.app/

## Estructura

El proyecto esta organizado de la siguiente manera:

- **`src/app.py`** → Contiene la aplicación principal de Flask. Aquí se definen las rutas y funciones que gestionan la lógica del servidor y la comunicación con las plantillas HTML (por ejemplo, index.html).
- **`src/explore.ipynb`** → Notebook Jupyter donde se desarrolla el análisis exploratorio de datos (EDA) y se construyen/entrenan los modelos de Machine Learning utilizados por la aplicación.
- **`src/run_waitress.py`** → Script que ejecuta la aplicación Flask (app.py) usando el servidor Waitress, configurado para escuchar en el puerto 5000 (o el definido por la variable de entorno PORT en despliegues).


## Contributors

This template was built as part of the [Data Science and Machine Learning Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning) by 4Geeks Academy by [Alejandro Sanchez](https://twitter.com/alesanchezr) and many other contributors. Learn more about [4Geeks Academy BootCamp programs](https://4geeksacademy.com/us/programs) here.

Other templates and resources like this can be found on the school's GitHub page.
