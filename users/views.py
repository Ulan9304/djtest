# from django.conf import settings
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

from django.shortcuts import render

from .forms import UserLoginForm, UserRegisterForm

# Create your views here.
def login_view(request):
    print(request.user.is_authenticated())
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())

    return render(request, "form.html", {"form":form, "title": title})

def register_view(request):
    title = "Register"
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            print ('true')
            user = form.save(commit=False)
            user.username = form.cleaned_data['username']
            user.password = form.cleaned_data['password']
            # user.email = form.cleaned_data['email']
            # user.email2 = form.cleaned_data['email2']
            user.set_password(user.password)
            user.save()
            new_user = authenticate(username=user.username,password=user.password)
            login(request, user)
            # login(request, user)
    #     return

    context = {
        "form": form,
        "title": title,
    }

    return render(request, "form.html",context)

def logout_view(request):
    logout(request)
    return render(request, "form.html",{})