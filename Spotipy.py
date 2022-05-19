# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 18:52:02 2021

@author: villajh
"""

import random
from urllib.parse import urlparse
import datetime as dt
import random as rd


def menu_validado_numerico(frase, campo, version):
    '''Utiliza la frase ingresada y el campo para crear una pregunta y navegar
    por los diccionarios, la version ('Key' o 'Field' indica si va a navegar
    por las Keys(para poder seleccionar informacion a editar por ejemplo) o si
    va a navegar por los Values(para seleccionar un artista basado en el campo
    nombre)'''
    if version == 'Key':
        while True:
            try:
                n = 0
                print(frase, '\n')
                for llave in lista[n].keys():
                    print(str(n+1)+'.', llave)
                    n += 1
                print('* Ingresa el numero correspondiente a tu eleccion')
                answer = list(lista[0].keys())[int(input())-1]
            except ValueError:
                print("Por favor, ingresa un valor numerico")
                continue
            return answer
    elif version == 'Field':
        while True:
            try:
                n = 0
                print(frase, '\n')
                for i in lista:
                    print(str(n+1)+'.', lista[n][campo])
                    n += 1
                print('* Ingresa el numero correspondiente a tu eleccion')
                answer = int(input())
            except ValueError:
                print("Por favor, ingresa un valor numerico")
                continue
            return answer


def input_validado(statement):
    while True:
        try:
            answer = input(statement)
            if answer == '':
                raise ValueError
        except ValueError:
            print('No se pueden ingresar campos vacios')
            continue
        return answer


def menu_principal():
    while True:
        try:
            opcion_menu = int(input('''Que deseas hacer?\n
1. Agregar una cancion a un artista
2. Agregar informacion de un artista
3. Consultar a un artista
4. Crear tu daily mix
5. Comprobar las URL's de un artista
*Ingresa el numero correspondiente a la opcion que quieres usar\n'''))
        except ValueError:
            print("Lo siento, ingresa un valor numerico")
            continue
        else:
            break
    return opcion_menu


def validacion_web(url, campo):
    if urlparse(url)[0] == '' and urlparse(url)[1] == '':
        print(f'La url para el campo "{campo}" no es valida.')
        url = input('Porfavor actualizala\n>')
    else:
        print(f'La url para el campo "{campo}" es valida.',
              'No son necesarias modificaciones')
    return url


nombres = ['Dua Lipa', 'Nicky Minaj', 'Justin Bieber', 'Ed Sheeran']

Diccionario = {
    'nombre': '',
    'oyentes': 0,
    'popular': [],
    'albums': [],
    'discografica': '',
    'web': '',
    'nacionalidad': '',
    'wiki': '',
}

lista = [
    {
        'nombre': 'Dua Lipa',
        'oyentes': 67221199,
        'popular': [
            'levitating',
            "we're good",
            'un dia',
            "don't start now",
            'one kiss',
        ],
        'albums': [
            'future nostalgia',
            'dua lipa deluxe'
        ],
        'discografica': 'warner - vertigo',
        'web': 'dualipa.com',
        'nacionalidad': 'britanica',
        'wiki': 'https://es.wikipedia.org/wiki/Dua_Lipa',
    },
    {
        'nombre': 'Nicky Minaj',
        'oyentes': 40033700,
        'popular': [
            'tusa',
            'super bass',
            'seeing green',
            'bang bang',
            'whole lotta money',
        ],
        'albums': [
            'beam me up scotty',
            'qeen',
            'the pinkprint',
            'pink friday'
        ],
        'discografica': 'Universal Motown -Young Money -Cash Money -Republic Records',
        'web': 'www.nickiminajofficial.com',
        'nacionalidad': 'trinitense',
        'wiki': 'https://es.wikipedia.org/wiki/Nicki_Minaj',
        'fecha_creacion': '2021-05-21 10:05-'
    },
    {
        'nombre': 'Justin Bieber',
        'oyentes': 71938798,
        'popular': [
            'peaches',
            'stay',
            'hold on',
            'stuck with U',
            '10,000 hours',
        ],
        'albums': [
            'Justice',
            'Changes',
            'Purpose',
            'Journals'
        ],
        'discografica': 'island records',
        'web': 'www.justinbiebermusic.com',
        'nacionalidad': 'inglés canadiense',
        'wiki': 'https://es.wikipedia.org/wiki/Justin_Bieber',
    }
]

print("Bienvenido/a a los perfiles de los artistas.\n Los artistas existentes son:")


for nombre in nombres:
    print('*', nombre)

input()

seleccion_menu_principal = menu_principal()

continuar = True

dt.datetime.now()

while continuar:

    if seleccion_menu_principal == 1:
        seleccion_artista = menu_validado_numerico(
            'Selecciona a un artista', 'nombre', 'Field')
        nombre_artista = lista[seleccion_artista-1]["nombre"]
        cancion = input_validado(
            f'Ingresa el nombre de la cancion para {nombre_artista}\n')
        lista[seleccion_artista-1]['popular'].append(cancion)
        print('La lista queda asi:\n')
        for i in lista[seleccion_artista-1]['popular']:
            print(i)
        print('\n', ('-'*20), '\nCancion agregada exitosamente')

    elif seleccion_menu_principal == 2:
        lista.append(Diccionario)
        continuar_edicion = 'Y'
        while continuar_edicion != 'N':
            seleccion = menu_validado_numerico(
                'Que campo deseas editar?', '', 'Key')
            edicion = input(
                f'Ingresa la informacion a agregar({seleccion})\n').title()
            if seleccion == 'popular' or seleccion == 'albums':
                lista[-1][seleccion].append(edicion)
            else:
                lista[-1][seleccion] = edicion
            continuar_edicion = input(
                'Deseas modificar otro campo?Y/N\n').upper()
        print('La informacion del artista queda asi:\n')
        for categoria, valor in lista[-1].items():
            print(categoria, ':', valor)

    elif seleccion_menu_principal == 3:
        seleccion_artista = menu_validado_numerico(
            'Selecciona a un artista', 'nombre', 'Field')
        nombre_artista = lista[seleccion_artista-1]["nombre"]
        print(f'La informacion de {nombre_artista} es:\n')
        for categoria, valor in lista[seleccion_artista-1].items():
            print(categoria, ':', valor)

    elif seleccion_menu_principal == 4:
        canciones = []
        daily_mix = []
        n = 0
        for listas in lista:
            for i in lista[n]['popular']:
                canciones.append(i)
            n += 1
        total_canciones = len(canciones)
        while len(daily_mix) < total_canciones//2:
            daily_mix = set(random.sample(canciones, total_canciones//2))
        print('Tu daily mix es el siguiente:\n')
        for cancion in daily_mix:
            print(cancion)

    elif seleccion_menu_principal == 5:
        seleccion_artista = menu_validado_numerico(
            'Selecciona a un artista', 'nombre', 'Field')
        nombre_artista = lista[seleccion_artista-1]["nombre"]
        web = lista[seleccion_artista-1]["web"]
        wiki = lista[seleccion_artista-1]["wiki"]
        lista[seleccion_artista-1]["web"] = validacion_web(web, 'web')
        lista[seleccion_artista-1]["wiki"] = validacion_web(wiki, 'wiki')

    if input_validado('Deseas continuar en la aplicacion? Y/N\n').title() == 'Y':
        continuar = True
        seleccion_menu_principal = menu_principal()
    else:
        continuar = False
