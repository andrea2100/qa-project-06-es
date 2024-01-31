# Proyecto: Pruebas de la API "/api/v1/kits" especificamente en el parámetro "name" al crear un kit de un usuario.


## Descripción del proyecto:
- Este proyecto consiste en automatizar las pruebas de la API "/api/v1/kits" (crear un kit) de una aplicación denominada Urban.Grocers donde los usuarios pueden crear su propio kit de productos, en este vamos a validar los diferentes tipos de datos que se aceptan en el parámetro "name" de un kit de un usuario en especifico (se toma el authToken de autorización de cada usuario creado anteriormente).

## Fuente de documentación utilizada:

- En este proyecto se utilizó como fuente de documentación APIDOC.

## Descripción de las tecnologías y técnicas utilizadas.

- Entorno de desarrollo integrado (IDE): Pycharm, versión 2023.3.2 (Community Edition).
- Lenguaje de programación Python, versión 3.12.1.
- Paquete pytest, versión 8.0.0.
- Librería request, versión 2.31.0.
- Se utilizó como técnica para ejecutar las pruebas el comando pytest.


## Contenido de los archivos del proyecto:
- Archivo configuration.py. Este contiene la URL principal con sus respectivos endpoint de la API para crear un usuario y para crear un kit.
- Archivo data.py. Este contiene todos los encabezados y cuerpos de las solicitudes necesarias para crear un usuario y un kit. 
- Archivo sender_stand_request.py. Este contiene las funciones con las solicitudes para crear un usuario y para crear un kit.
- Archivo create_kit_name_kit_test.py. Este contiene las funciones para validar las pruebas positivas y negativas desarrolladas de acuerdo a lista de comprobación enviada en este proyecto. Son 5 pruebas con resultado esperado positivo y 4 pruebas con resultado esperado negativo. 


## Conclusiones:
**Luego de realizar las 9 pruebas se tiene como resultado:**

- Pasaron 5 pruebas: En este caso corresponden a las pruebas positivas, donde el resultado esperado coincide con el resultado actual. Este código de estado es 201, lo que quiere decir que se crearon los kit con el parámetro "name" de la lista de comprobación.
- Fallaron 4 pruebas: En este caso corresponde a las pruebas negativas donde el resultado esperado no coincide con el resultado actual. Se esperaba un código de estado 400 y se obtuvo un código de estado 201. Esto quiere decir que se esperaba que no se crearan los kit debido al tipo de dato enviado en cada una de estas pruebas.



