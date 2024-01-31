import configuration
import requests
import data

#Función para crear un usuario
def post_create_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=data.user_body,
                         headers=data.headers)

#Función para crear un nuevo kit de producto
def post_new_client_kit(auth_token, kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, headers=auth_token, json=kit_body)