

from cryptography.fernet import Fernet
from auxiliares.clave import clave_guardada

def encriptar_contrasena(contrasena):
    clave = Fernet(clave_guardada)
    token = clave.encrypt(contrasena.encode('utf-8'))
    print(token)
    return token

def desencriptar_contrasena(token):
    clave = Fernet(clave_guardada)
    contrasena_guardada = clave.decrypt(token)
    return contrasena_guardada

    
