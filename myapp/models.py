from django.db import models

# Create your models here.
#1 creo classe
class Project(models.Model):
#2 creo attributi per specificare le colonne, dati che salvo in una tavola
    name = models.CharField(max_length=200)
#python manage.py runserver per aggiungere

    def __str__(self):
            return self.name
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    #1titolo
    #2descrizione
    #3 a quale progetto appartiene [in questo caso fo la FK e specifico la relazione]
    #a cascata verranno eliminate le tavole relazionate
    def __str__(self):
        return self.title + ' - ' + self.project.name #mostra titolo + appartenenza project
