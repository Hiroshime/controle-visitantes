from django.shortcuts import (render, redirect, get_object_or_404)
from visitantes.forms import VisitanteForm
from visitantes.models import Visitante
# Create your views here.

def registrar_visitante(request):

    form = VisitanteForm()

    if request.method == "POST":
        form = VisitanteForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.registrado_por = request.user.porteiro
            visitante.save()

            return redirect("index")

    context = {"nome_pagina": "Registrar Visitante",
    "form": form
    
    }

    return render(request,"registrar_visitante.html", context)

def informacoes_visitante(request, id):

    visitante = get_object_or_404(Visitante,id=id)

    context = {"nome_pagina":"Informacoes de visitante","visitante":visitante}
    return render(request, "informacoes_visitante.html", context)
