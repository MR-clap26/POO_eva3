from db import connector



def insert_user(usuario):
    
    values=(usuario.nombre,usuario.contraseña)

    cursor=connector().cursor()
    cursor.execute(f'insert into Usuarios (nombre,contraseña) values ({name},{password})')

