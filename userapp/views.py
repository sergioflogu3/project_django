from django.shortcuts import render, HttpResponse, redirect
from userapp.models import Faculty
from userapp.forms import FormFaculty

layout = """
    
"""

# Create your views here.
def index(request):
    html = """
        <ul>
    """
    year = 2022
    while year <= 2050:
        html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"

    return render(request, 'index.html')


def hello_world(request):
    return render(request, 'hello-world.html')

def pagina(request):
    return render(request, 'pagina.html')

def contacto(request, name):
    return HttpResponse(layout + f"<h2>Contacto:  {name}</h2>")

def create_faculty(request):
    return render(request, 'create_faculty.html')

def create_full_faculty(request):
    if request.method == 'POST':
        form = FormFaculty(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            name = data_form.get('name')
            description = data_form.get('description')
            faculty = Faculty(
                name=name,
                description=description
            )
            faculty.save()
            return redirect('faculties')
    else:
        form = FormFaculty()
        return render(request, 'create_full_faculty.html', {
            'form': form
        })

def store_faculty(request):
    if request.method == 'POST':
        if len(request.POST['name']) <= 5:
            return HttpResponse('El nombre es muy pequeño')

        faculty = Faculty(
            name= request.POST['name'],
            description = request.POST['description']
        )
        faculty.save()
        return redirect('faculties')
    else:
        return HttpResponse('No se ha podido crear la Facultad')

def faculty(request):
    try:
        faculty = Faculty.objects.get(pk=5)
        response = f"Facultad: {faculty.name}"
    except:
        response = "<h1>Articulo no encontrado</h1>"
    return HttpResponse(response)

def edit_faculty(request, id):
    try:
        faculty = Faculty.objects.get(pk=id)
        faculty.name = "Facultad de Ciencias Puras"
        faculty.description = "Nueva descripcion"
        faculty.save()
        response = f"Articulo editado {faculty.name} - {faculty.description}"
    except:
        response = "<h1>Articulo no encontrado</h1>"
    return HttpResponse(response)

def faculties(request):
    faculties = Faculty.objects.order_by('id')
    return render(request, 'faculties.html', {
        'faculties': faculties
    })

def delete_faculty(request, id):
    faculty = Faculty.objects.get(pk=id)
    faculty.delete()
    return redirect('faculties')