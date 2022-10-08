from django.db import models

# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Person(models.Model):
    number_ci = models.CharField(max_length=100)
    names = models.CharField(max_length=100)
    firts_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    birthay_date = models.DateField()

class Unit(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Responsible(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)

class Authority(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)

class PartAssistance(models.Model):
    responsible = models.ForeignKey(Responsible, on_delete=models.CASCADE)
    authority = models.ForeignKey(Authority, on_delete=models.CASCADE)
    month = models.CharField(max_length=50)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

