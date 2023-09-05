from django.contrib import admin
from .models import Project, Task

# Register your models here.
# Aggiungo varie interfaccie per creare nuovi compiti nella pagina del progetto
admin.site.register(Project)
admin.site.register(Task)