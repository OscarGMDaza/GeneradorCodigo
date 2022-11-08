# Generador de codigo para proyecto microservicios tiendita

## Autores
Oscar G. Mejia Daza - Código: 20221099009
Carlos Andres Penagos C. - Código: 20221099013

## USO
Para el generador de código se hacen uso de las herramientas de Jinja2 y TextX, las cuales permiten la creación de plantillas para generar el archivo con los parametros que se desen, para este caso se cuenta con la creación de los archivos para agregar un modulo al programa de microservicios de tiendita desarrollado en clase.

Para ello en el archivo modelo.ent se debe agregar la entidad, sus atributos y especificar el tipo de datos de estos atributos, luego de ello se debe ejecutar el archivo entity_codegen.py, donde en la carpeta srcgen se generaran los archivos app.py, config_app.py, Dockerfile, model.py y requerimientos.txt

Estos archivos generados se deben de mover al proyecto de microservicios de tiendita desarrollado en clase, en el archivo app.py se deben hacer unos ajustes los cuales son:
        1. En la funcion listar, eliminar la coma (,) del ultimo de los atributos
        2. En la función agregar, ajustar en la notación route los elementos que ingresaran y su variables para el mapeo
        3. En la función editar, ajustar en la notación route los elementos que ingresaran y su variables para el mapeo

En el proyecto microservicios de tiendita desarrollado en clase de manera manual se deben ajustar los archivos nginx.conf y docker-compose.yml agregando la nueva entrada al modulo para su despliegue en el microservicio.

Como archivo comprimido se agrega el proyecto de microservicios de tiendita donde se agrego el modulo de domicilio generado por medio de este proyecto
