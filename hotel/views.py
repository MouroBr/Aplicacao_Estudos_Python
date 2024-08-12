from django.shortcuts import render
from django.http import HttpResponse


# essa camada Faz a ligação entre os dados e o que será mostrado, criando a página que o usuário vê.
# Rotas
def home(request):
    return render(request, "hotel/home.html")
