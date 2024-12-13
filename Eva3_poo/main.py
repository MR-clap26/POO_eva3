from getpass import getpass
from servicios.uso_api import consultar_api
from negocio.encriptacion import encriptar_contrasena
from datos.consultas import insert_user
from modelos.usuarios import Usuario


def menuinicio():
    print("================================")
    print("       M E N Ú  I N I C I O     ")
    print("================================")
    print("       1.- INICIAR SESION       ")
    print("       2.- CREAR SESION         ")
    print("       3.- Salir                ")
    print("================================")




def inc_sesion():
    print("================================")
    print("           I N I C I A R        ")
    print("================================")

    print("                                ")
    print("================================")


def  crear_ses():
    print("================================")
    print("     C R E A R   S E S I O N    ")
    print("================================")
    nom_user=input('igrese su nombre de ususario: ')
    while not len(nom_user):
        print('campo nesesario')
        nom_user=input('igrese su nombre de ususario: ')

    print('''
        considere que su contraseña tiene que ser de 8 o mas 
        caracteres y almenos 1 simbolo (@&$#)''')
    password=getpass('contraseña: ') 
    simbolos=['&','@','#','$']
    cont=0
    for i in password:
        if i in simbolos:
            cont=+1
    while len(password)<8 or cont==0:
        print('tu contraseña no cumple con los parametros intenta de nuevo')
        password=getpass('contraseña: ')      
        for i in password:
            if i in simbolos:
                cont=+1

    encriptada=encriptar_contrasena(password)

    nuevo_usuario=Usuario()
    nuevo_usuario.id_user=
    nuevo_usuario.nombre=nom_user
    nuevo_usuario.contrseña=encriptada

    insert_user(nuevo_usuario)

    print('usuario creado')
    print("                                ")
    print("================================")



