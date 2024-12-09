from getpass import getpass





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

    password=getpass('contraseña: ')    

    print("                                ")
    print("================================")
