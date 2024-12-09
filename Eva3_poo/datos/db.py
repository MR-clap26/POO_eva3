import mysql.connector


def connector():
            
        connection = mysql.connector.connect(
            user='root',
            password='',
            host='127.0.0.1',
            database='eva3_poo'
        )
        if connection.is_connected():
                print("Conexión exitosa a la base de datos.")
                return connection