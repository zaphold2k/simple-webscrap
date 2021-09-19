# Requisitos para ejecutar el proyecto
- python 3.6
- pip

# Virtual environment con python
Para no instalar librerías innecesarias en el sistema opeartivo, utilizaremos una herramienta de python llamada _Virtual Environments_ que nos permite crear ambientes aislados para proyectos de python. Esto significa que cada proyecto puede tener sus propias dependencias sin conflictuar con las del sistema operativo.

## Creación de un nuevo virtual environment
Estando sobre el directorio raíz del proyecto ejecutamos el siguiente comando para crear el virtual environment.
```shell
python3 -m venv ./venv
```

Al ejecutar el comando, python creará una estructura el directorio `venv`, donde se pueden encontrar todos los binarios y dependencias que utilizará el virtual env en cuestión.

##Activar venv
Una vez creado el virtual env, para que la terminal utilice el ambiente en vez del de el host, debemos activarlo con el siguiente comando:
```jshelllanguage
source venv/bin/activate
```

Para confirmar que el mismo se activó se verá antecedido al prompt el nombre del virtual env, en este caso `venv`
```jshelllanguage
(venv) [server]$
```

##Desactivar venv
Si queremos dejar de utilizar el virtual env y volver a utilizar los binarios de python del host, debemos desactivar el virtual env con el sigueinte comando:

```jshelllanguage
(venv) $ deactivate
```

# Instalación de dependencias de la aplicación
Una vez que tenemos creado y activado el virtual environment, debemos instalar los paquetes pip necesarios para que la aplicación pueda ejecutarse correctamente. Para ello corremos el sigueinte comando:
```jshelllanguage
pip install -r requeriments.txt
```

# Ejecutar aplicación flask
Para correr la aplicación flask se debe ejecutar el siguiente comando:
```jshelllanguage
flask run
```

Dicho comando devolverá un output similar al siguiente y la aplicación web se mantendrá operativa mientras no se cancele la terminal donde se ejecutó:
```jshelllanguage
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
    .../simple-webscrap/app.py:29: Warning: Silently ignoring app.run() because the application is run from the flask command line executable. Consider putting app.run() behind an if __name__ == "__main__" guard to silence this warning.
  app.run(host='localhost', port=5000)
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Tal como indica la terminal, la aplicación correrá en la URL [http://127.0.0.1:5000/](http://127.0.0.1:5000/)