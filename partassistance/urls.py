
from django.contrib import admin
from django.urls import path

from userapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("inicio/", views.index, name="index"),
    path("hello-world/", views.hello_world, name='helloWorld'),
    path("pagina-pruebas/", views.pagina, name='pruebas'),
    path("contacto/<str:name>", views.contacto, name='contacto'),

    path("faculty", views.faculty, name="view_faculty"),
    path("faculty/create", views.create_faculty, name="create_faculty"),
    path("faculty/create_full", views.create_full_faculty, name="create_full_faculty"),
    path("faculty/store", views.store_faculty, name="store_faculty"),
    path("faculty/edit/<int:id>", views.edit_faculty, name="edit_faculty"),
    path("faculty/delete/<int:id>", views.delete_faculty, name="delete_faculty"),
    path("faculties", views.faculties, name="faculties")
]
