import sender_stand_request
import data

# Función para recibir el authToken y agregarlo al encabezado para crear un kit
def get_new_user_token():
    # Guadar el resultado de crear un usuario en la variable "response"
    response = sender_stand_request.post_create_new_user()
    # Guardar el valor de "authToken" del usuario creado en la variable "auth_token"
    auth_token = response.json()["authToken"]
    #Copiar el diccionario de headers_kit y guardarlo en la variable "current_headers_kit"
    current_headers_kit = data.headers_kit.copy()
    # Agregar el string "Bearer" al diccionario de "current_headers_kit"
    current_headers_kit["Authorization"] = "Bearer "
    # Agregar el string "auth_token al diccionario de "current_headers_kit"
    current_headers_kit["Authorization"] += str(auth_token)
    # Retornar el diccionario actual del encabezado con el authToken del usuario creado
    return current_headers_kit

#Función para cambiar el valor del parámetro name en el cuerpo de la solicitud
def get_kit_body(name):
    # Copiar el diccionario kit_body con el cuerpo de la solicitud desde el archivo de datos
    current_kit_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_kit_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_kit_body

#Función de prueba positiva
def positive_assert_kit_body(name):
    # Obtener el authToken y el nuevo encabezado para crear un kit
    header_kit_new = get_new_user_token()
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(header_kit_new, kit_body)
    # Comprueba si el estado de código es 201 (se crea el kit)
    assert kit_response.status_code == 201

# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert_code_400(name):
    # Obtener el authToken y el nuevo encabezado para crear un kit
    header_kit_new = get_new_user_token()
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(header_kit_new, kit_body)
    # Comprueba si el estado de código es 201 (se crea el kit)
    assert kit_response.status_code == 400

# Prueba 1. El número permitido de caracteres (1), en el parámetro "name".
def test_create_kit_1_character_in_name_get_success_response():
    positive_assert_kit_body("A")

# Prueba 2. El número permitido de caracteres (511), en el parámetro "name".
def test_create_kit_516_character_in_name_get_success_response():
    positive_assert_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Prueba 3. El número de caracteres es menor que la cantidad permitida (0).
# El parámetro "name" contiene un string vacío
def test_create_kit_empty_name_get_error_response():
    negative_assert_code_400("")

# Prueba 4. El número de caracteres es mayor que la cantidad permitida (512).
def test_create_kit_512_letters_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Prueba 5. Se permiten caracteres especiales.
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert_kit_body("\"№%@\",")

# Prueba 6. Se permiten espacios en el parámetro "name".
def test_create_kit_with_spaces_in_name_get_success_response():
    positive_assert_kit_body(" A Aaa ")

# Prueba 7. Se permiten números en el parámetro "name".
def test_create_kit_with_numbers_in_name_get_success_response():
    positive_assert_kit_body("123")

# Prueba 8. El parámetro "name" no se pasa en la solicitud.
def test_create_kit_no_name_get_error_response():
    #El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "kit_body"
    kit_body = data.kit_body.copy()
    #El parámetro "name" se elimina de la solicitud
    kit_body.pop("name")
    #Comprueba la respuesta
    negative_assert_code_400(kit_body)

# Prueba 9. Se ha pasado un tipo de parámetro diferente (número).
def test_create_kit_number_type_name_get_error_response():
    negative_assert_code_400(123)



