from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import os

def page1(request):
    x = 'testing.html'
    if request.method == 'GET':
        return render(request, x)

def reflejar_api(request):
    if request.method == 'GET':
        #Se abre el archivo .json ubicado enla raíz del proyecto
        with open('explorers.json') as file:
            #Se carga el json en la variable data
            data = json.load(file)

            #Se regresa el json como respuesta entrando en la URL definida para esta función
            return JsonResponse(data, safe=False)


def api(url, params={}):
    #Encabezados para la peticion
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.153'}
    #Se guarda la petición en la variable response
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()

def get_data(params={}):
    response = api('http://localhost:8000/apilocal', params)
    if response:
        return response
        # user = response.get('results')[0]
        # return user.get('name').get('first')

    return

def hello(request):
    if request.method == 'GET':
        data = get_data()
        context = {
            'name': data[0]['name']
        }
        return render(request, 'hello.html', context)
