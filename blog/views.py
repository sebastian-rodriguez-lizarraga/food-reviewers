from django.http import HttpResponse
from django.shortcuts import render
from blog.forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate


def inicio(request):
    return render(request,"blog/inicio.html")

def nosotros(request):
    return render(request, "blog/acerca-de.html")


####### LOGIN #######
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = request.POST["username"]
            clave = request.POST["password"]

            user = authenticate(username=usuario,password=clave)
            if user is not None:
                login(request, user)
                return render(request, "blog/inicio.html", {'mensaje':f'Bienvenido { user } a FoodReviewers'})
            else:
                return render(request, "blog/login.html", {'form':form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "blog/login.html", {'form':form, "mensaje":"FORMULARIO INVALIDO"})
    else:
        form=AuthenticationForm()
        return render(request, "blog/login.html", {'form':form})

####### REGISTRAR #######

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]

            form.save()
            return render(request, 'blog/inicio.html', {'mensaje':f"Usuario { username } creado"})
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form':form})