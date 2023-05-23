# Django Hello World

![Docker](https://img.shields.io/badge/Docker-2496ED?&style=flat&logo=docker&logoColor=ffffff)&nbsp;
![Python](https://img.shields.io/badge/Python-14354C?style=flat&logo=python&logoColor=white)&nbsp;
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)&nbsp;
![NGINX](https://img.shields.io/badge/Nginx-009639?style=flat&logo=nginx&logoColor=white)&nbsp;

## Introducción

Un Hello World en un proyecto minimalista en cualquier lenguaje de programación o scripting que pretende hacer una sencilla demo de ejecución satisfactoria del código que muestra en la pantalla el texto "Hello World".

En este caso el lenguaje es Python y utilizaremos el framework de Django y PyCharm como IDE.

## Objetivo

El objetivo de este proyecto es principalmente didáctico, un ejemplo básico de proyecto Python con el framework Django y el IDE de PyCharm, gestión de paquetes o librerías (Virtual Environments), ejecución y depuración de código, dockerización y ejecución en local con Docker y Docker Compose, utilización de Gunicorn como servidor Web y NGINX como Proxy Inverso, etc.

Este repo se ha creado para complementar el Post [Python – Hello World con Python, Django y PyCharm](https://elwillie.es/2023/05/22/hello-world-con-python-django-y-pycharm/) del Blog [El Willie - The Geeks invaders](https://elwillie.es)

**Puedes apoyar mi trabajo haciendo "☆ Star" en el repo o nominarme a "GitHub Star"**. Muchas gracias :-) 

[![GitHub Star](https://img.shields.io/badge/GitHub-Nominar_a_star-yellow?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://stars.github.com/nominate/)


## Arquitectura de la Solución

Se trata de un Proyecto Python que contiene:

* Un Proyecto Django, llamado hello_world.
 * Una Aplicación Django, llamada hello_world_page, que responde en http://localhost:8000/hello-world/.
* Se puede ejecutar dockerizado, para lo que incluye un fichero Dockerfile, y levanta un servidor Web Gunicorn.
* También se puede ejecutar con Docker Compose, levantando además del propio contenedor de la aplicación, otro con NGINX como Proxy Inverso que responde en http://localhost/hello-world/. 
 
Podemos ejecutarlo en local, arrancando el servidor Web de Django ejecutando un comando como el siguiente:

```
python manage.py runserver
```


## Otros detalles de interés

Si te interesa aprender Python, tienes disponibles los siguientes [cursos gratuitos de Python en Edube - OpenEDG](https://edube.org/):

* Python Essentials 1
* Python Essentials 2
* Python Advanced 1 – OOP
* Python Advanced 2 – Best Practices and Standardization
* Python Advanced 3 – GUI Programming
* Python Advanced 4 – RESTful APIs
* Python Advanced 5 – File Processing

Otro recurso muy interesante es [Real Python](https://realpython.com/), donde podrás encontrar tutoriales, baterías de preguntas para ponerte a prueba (quizzes), etc.

En mi Blog personal ([El Willie - The Geeks invaders](https://elwillie.es)) y en mi perfil de GitHub, encontrarás más información sobre mi, y sobre los contenidos de tecnología que comparto con la comunidad.

[![Web](https://img.shields.io/badge/GitHub-ElWillieES-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/ElWillieES)

# Git

## Repositorio

Este repo se puede clonar desde GitHub utilizando este [enlace HTTP](https://github.com/ElWillieES/django-hello-world.git). 

A continuación se muestra el comando git clone usando SSH en lugar de HTTP.

```sh
git clone git@github.com:ElWillieES/django-hello-world.git
```


# Docker - Ejecución en local

## Con Docker

Se puede ejecutar la aplicación en local con Docker. 

Los siguientes comandos ejecutados en la raíz del Proyecto, muestran:
* Cómo **crear una imagen** en local con docker build.
* Cómo listar las imágenes que tenemos disponibles en local. Deberá aparecer la que acabamos de crear.
* **Cómo ejecutar un contenedor con nuestra imagen**.
* Cómo parar el contenedor, cuando acabemos nuestras pruebas.

```shell
docker build -t django-hello-world .
docker images
docker run -it --rm -d -p 8000:8000 --name django-hello-world django-hello-world
docker stop django-hello-world
```

Podemos arrancar una sesión interativa de Bash sobre un Contendor con nuestra imagen Docker, para de este modo, analizar mejor incidencias y problemas que nos puedan surgir, depurar, etc. Suele ser bastante útil.

En el siguiente ejemplo, arrancamos una sesión bash sobre un contenedor con nuestra imagen, arrancamos manualmente la aplicación con gunicorn, y finalmente salimos.

```shell
docker run -it --rm -p 8000:8000 --name django-hello-world django-hello-world /bin/bash
gunicorn hello_world.wsgi:application --bind 0.0.0.0:8000
exit
```


## Con Docker Compose

El siguiente comando ejecutado en la raíz del Proyecto, muestra cómo compilar (es decir, construir la imagen Docker) y ejecutar django-hello-world con Docker Compose, así como la forma de poder comprobar los logs de su ejecución.

Si observamos el fichero **docker-compose.yml**, podemos ver que incluye un contenedor para la aplicación y otro para un NGINX que actúa como Proxy Inverso en el puerto tcp-80. 

```shell
docker-compose up --build -d
docker-compose logs
```

