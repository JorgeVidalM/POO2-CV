from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import CV, Ciudad
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from .forms import CVForm
from django.shortcuts import get_object_or_404

def menu_principal(request):
    return render(request, "menu.html")

def ingresar_cv(request):
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_cvs')
    else:
        form = CVForm()
    return render(request, 'ingresar_cv.html', {'form': form})

def listar_cvs(request):
    cvs = CV.objects.all()
    ciudades = Ciudad.objects.all()

    edad = request.GET.get('edad')
    ciudad_id = request.GET.get('ciudad')
    keyword = request.GET.get('keyword')

    if edad:
        cvs = [cv for cv in cvs if str(cv.edad()) == edad]

    if ciudad_id and ciudad_id != "":
        cvs = cvs.filter(ciudad_id=ciudad_id)

    if keyword:
        cvs = cvs.filter(descripcion__icontains=keyword)

    return render(request, 'listar_cvs.html', {
        'cvs': cvs,
        'ciudades': ciudades,
        'edad_filtro': edad,
        'ciudad_filtro': ciudad_id,
        'keyword_filtro': keyword
    })


def detalle_cv(request, cv_id):
    cv = get_object_or_404(CV, id=cv_id)
    return render(request, 'detalle_cv.html', {'cv': cv})