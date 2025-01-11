from datetime import datetime, timedelta

from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from collections import Counter

from .models import Pessoa, Diario





def home(request):
    return render(request, 'home.html')

def escrever(request):
    if request.method == "GET":
       return render(request, 'escrever.html')
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        tags = request.POST.getlist('tags')
        pessoas = request.POST.getlist('pessoas')
        texto = request.POST.get('texto')
        return HttpResponse (f' {titulo} - {tags} - {pessoas} - {texto}')
    
def cadastrar_pessoa(request):
    if request.method == 'GET':
        return render(request, 'pessoa.html')

    elif request.method == 'POST':

        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')

        pessoa = Pessoa(nome=nome, foto=foto)
        pessoa.save()

        return redirect('escrever')

def dia(request):
    data = request.GET.get('data')
    data_formatada = datetime.strptime(data, '%Y-%m-%d')

    diarios = (Diario.objects.filter(create_at__gte=data_formatada)
              .filter(create_at__lte=data_formatada + timedelta(days=1)))


    return render(request, 'dia.html', {'diarios':diarios, 'total':diarios.count(), 'data':data})

def excluir_dia(request):
    dia = datetime.strptime(request.GET.get('data'),'%Y-%m-%d')
    diarios = (Diario.objects.filter(create_at__gte=dia)
               .filter(create_at__lte=dia + timedelta(days=1)))

    diarios.delete()

    return HttpResponse('teste')
   
   
    
    
