# Blog de Mezano

[![Python](https://img.shields.io/badge/python-black?style=for-the-badge&logo=python)](https://github.com/mezano85/blog)

Los blogs se escriben en Markdown y se utiliza Pelican para crear el contenido web estatico
para su publicación. Dentro de la carpeta content se localizan los artículos escritos.
## Levantar los cuentos de forma local

Para levantar un entorno local basta con instalar los **requirements.txt** y ejecutar el siguiente
comando en el directorio raiz del proyecto:

```python
make local
```

Al ejecutarse se limpia el contenido de la carpeta **docs** que es donde se almancenan los
archivos generados por Pelican y se vuelven a crear utilizando como configuración los datos
dentro de **pelicanconf.py**, una vez generado se levanta un micro servicio local que estará
buscando cambios y haciendolos visibles mediante el puerto 8000, http://localhost:8000 .

Para detener el entorno local desde la terminal precionar CTRL + C.

## Guardar los datos para publicarse

Una vez terminados los cambios a implementar, ejecutaremos el siguiente comando:

```python
make publish
```

Este proceso limpiará la carpeta **docs** y generará nuevamente los archivos, pero ahora
utilizando como archivo de configuracion **publishconf.py**.