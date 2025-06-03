#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: daniel
"""
import manageDB as man_DB

    
flag_exit = False
while (flag_exit == False):
    print('Opciones')
    print('-'*20)
    print('1. Agregar tarea')
    print('2. Ver tarea')
    print('3. Contar tareas pendientes')
    print('4. Salir')
    print('-'*20)
    
    option = input('Ingrese alguna de las opciones del menú: ')
    
    if option == '1':
        idTask = input('Ingrese el id de la nueva tarea: ')
        man_DB.add_task(idTask)
    elif option == '2':
        idTask = input('Ingrese el id de la tarea: ')
        man_DB.view_task(idTask)    
    elif option == '3':
        man_DB.count_task_pen()
    elif option == '4':
        flag_exit = True
    else:
        print('Opción invalida') 