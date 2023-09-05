from django.urls import path
from . import views

urlpatterns = [
    #path('admin/',admin.site.urls)
    #path('', views.hello),
    path('', views.index),
    path('about/', views.about),
    #con il simbolo / aggiungo vari parametri in base a che URL necesito
    path('hello/<str:username>', views.hello),
    #creo una <variabile> che posso estrarre
    #possono essere anche numeri <INT:>
    path('projects/', views.projects),
    path('task/<int:id>', views.task), #posso anche inserire <int/str:name>,<title> etc dipende da come si chiama la colonna
]
