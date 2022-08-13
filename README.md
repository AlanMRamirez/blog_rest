# AlanMRamirez

## Blog Rest
<h6>Este proyecto es una API REST  que puede ser consumida por diferentes front-end, y se encuentra desarrollada con django-rest framework</h6> 

![](https://www.astera.com/wp-content/uploads/2020/01/rest.png)

## Librerias necesarias se encuentran en el archivo requirements

<p>Se recomienda utilizar un entorno virtual</p>

`pip install -r requirements.txt`

<p>La libreria necesaria para poder conectar la api a postgreSQL ya se encuentra en el archivo requirements</p>

## Desarrollo

<p>Recordar que durante la fase de desarrollo se tiene colocar True en el DEBUG y si se requiere colocar localhost y 127.0.0.1 en ALLOWED_HOST</p>

    DEBUG = True
    
    ALLOWED_HOSTS = []

<h6>Para levantar el servidor local</h6>

`python manage.py runserver`

<h6>Si se quiere probar hacer peticiones lo puedes realizar desde programas como Postman e Insomnia</h6>

[Blog Rest](https://blog-rest-alanmr.herokuapp.com "Blog Rest")

![](https://dashboard.snapcraft.io/site_media/appmedia/2018/04/twitter-card-icon.png)

![](https://www.sngular.com/wp-content/uploads/2021/12/postman-logo-vert-2018.jpg)
