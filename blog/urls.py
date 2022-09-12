from django.urls import path
from blog.views import *

urlpatterns = [

    path('acerca-de/', nosotros, name="acerca-de"),
    path('iniciar-sesion/', login_request, name ='login'),
    path('register/', register,name="register"),
    #path('blog/padre', inicio,name="inicio"),
]