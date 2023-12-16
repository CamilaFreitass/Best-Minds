from django.shortcuts import render, redirect
from .models import Produto
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'home.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == "GET":
        return render(request, 'cadastrar_produto.html')
    elif request.method == "POST":
        nome_produto = request.POST.get('nome_produto')
        codigo_produto = request.POST.get('codigo_produto')
        descricao_produto = request.POST.get('descricao_produto')
        preco_produto = request.POST.get('preco_produto').replace(',', '.')

        produto = Produto(nome_produto=nome_produto,
                        codigo_produto=codigo_produto,
                        descricao_produto=descricao_produto,
                        preco_produto=preco_produto)
        
        produto.save()
        messages.add_message(request, constants.SUCCESS, 'Produto cadastrado com sucesso')
        return redirect(reverse('home'))
    
def editar_produto(request, id):
    produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome_produto')
        codigo= request.POST.get('codigo_produto')
        descricao = request.POST.get('descricao_produto')
        preco = request.POST.get('preco_produto').replace(',', '.')

        if nome and codigo and descricao and preco:
            produto.nome_produto = nome
            produto.codigo_produto = codigo
            produto.descricao_produto = descricao
            produto.preco_produto = preco
            produto.save()
            messages.add_message(request, constants.SUCCESS, 'Produto alterado com sucesso')
            return redirect(reverse('home'))
        else:
            return HttpResponse("Produto Inválido")
        
    return render(request, 'editar_produto.html', {'produto': produto})

def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    messages.add_message(request, constants.SUCCESS, 'Produto deletado com sucesso')
    return redirect(reverse('home'))

