#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: daniel
"""

def checkTask(idTask):
    fileDB = open('database_task.txt')
    taskExist = False
    for line in fileDB:
        if idTask in line:
            taskExist = True
            break
    return taskExist

def add_task(idTask):
    taskExist = checkTask(idTask)
    if taskExist == False:
        descripcion = input('Descripcion: ')
        responsable = input ('Responsable: ')
        estado = input('Estado (PEN/Listo): ')
        
        file = open(idTask + '.txt', 'w')
        file.write('Descripcion: ' + descripcion + '\n')
        file.write('Responsable: ' + responsable + '\n')
        file.write('Estado: ' + estado + '\n')
        
        file.close()
        
        file_DB = open('database_task.txt', 'a')
        file_DB.write(idTask +'\n')
        file_DB.close()
    else:
        print('Esta tarea ya existe')

def view_task(idTask):
    taskExist = checkTask(idTask)
    if taskExist:
        print('-'*10)
        print(idTask)
        print('-'*10)
        file = open(idTask + '.txt', 'r')
        for line in file:
            print(line)
    else:
        print('No existe una tarea con este identificador')

def count_task_pen():
    fileDB = open('database_task.txt')
    contador_PEN = 0
    for idTask in fileDB:
        if 'Task' in idTask:
            file = open(idTask[:-1] + '.txt', 'r')
            for line in file:
                if 'PEN' in line:
                    contador_PEN +=1
                    break
    print('El número de tareas pendientes es: ', contador_PEN)
                
    
    



if __name__ == '__main__':
    taskExist = checkTask('Task_1')
    add_task('Task_4')
    view_task('Task_1')
    count_task_pen()