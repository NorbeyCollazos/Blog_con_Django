from django.shortcuts import render, redirect
from mainapp.models import Entrada
from django.core.paginator import Paginator
from mainapp.forms import RegisterForm
import sqlite3
from django.db.models import Q

#conexion a la base de datos sqlite
conexion = sqlite3.connect('db.sqlite3', check_same_thread=False)
#crear el cursor
cursor = conexion.cursor()

# Create your views here.
def index(request):

    queryset = request.GET.get("buscar")
    entradas = Entrada.objects.filter(public=True)

    if queryset:

        query = Q(title__icontains = queryset)
        query.add(Q(content__icontains = queryset), Q.OR)
        query.add(Q(public=True), Q.AND)

        entradas = Entrada.objects.filter(query)

    #paginar los articulos
    paginator = Paginator(entradas, 3)

    #obtener el numero de la pagina
    page = request.GET.get('page')
    page_entradas = paginator.get_page(page)

    return render(request, 'mainapp/index.html',{
        'title': 'Inicio',
        'entradas': page_entradas
    })

def detalle_entrada(request, entrada_id):

    entrada = Entrada.objects.get(id=entrada_id)

    return render(request,'mainapp/detalle_entrada.html',{
        'entrada': entrada
    })

def registro_usuario(request):

    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            objeto = register_form.save()
            
            idr = str(objeto.id)

            cursor.execute("UPDATE auth_user SET is_staff=1 WHERE id="+idr)
            conexion.commit()

            cursor.execute("INSERT INTO auth_user_groups (user_id, group_id)VALUES ("+idr+", 1);")
            conexion.commit()

            return redirect('/admin')

    return render(request, 'users/register.html',{
        'title': 'Registro de usuario',
        'register_form': register_form
    })
