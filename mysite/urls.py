"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin #attivo la FUN 'admin', crea un pannello di controllo nel navigatore
from django.urls import path, include
from myapp.views import hello
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')) #campo vuoto indica rotta da seguire(''se inserisco qualcosa creo nuovo urls, quindi per accdedere alla rotta dovrò prima inserire la nuova rotta creata poi quella che già ho)
    #path('', views.hello),
    #path('about/', views.about)
    #BD--python manage.py makemigrations/python manage.py migrate[per utilizzare db.sqlite3]

]
