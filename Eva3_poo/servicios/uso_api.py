
import requests
from modelos.todo import Todo as tarea

def consultar_api():
    linck='http://jsonplaceholder.pycode.com'
    
    try:
        response=requests.get(linck)

        if response.status_code==200:
            #print('solicitud exitosa')
            print('Data:',response.json())
            tareas=[tarea()]
            for todo in response.json():
                print(f'{type(todo)}')
                print(f'Id Usuario:{todo['userId']},Id:{todo['id']},título:{todo['title']},estado:{todo['completed']}')

                nueva_tarea=tarea()
                nueva_tarea.userId=todo['userId']
                nueva_tarea.id=todo['id']
                nueva_tarea.title=todo['title']
                nueva_tarea.completed=todo['completed']

                tareas.append(nueva_tarea)
            #print(tareas)
            return (tareas)
            

    except requests.exceptions.Timeout:
        print('')
    except requests.exceptions.ConnectionError:
        print('')
        
    except requests.exceptions.InvalidHeader:
        print("")


print(consultar_api)