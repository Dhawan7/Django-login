from django.shortcuts import render
from django.http import HttpResponse
from .forms import userForm
from django.contrib.auth import login,authenticate

def index(request):
    form = userForm()
    if request.method == 'POST':
        form = userForm(data=request.POST)
        if form.is_valid():
            print("Validation Successfully")
            form.save()
            return HttpResponse("<h1 style='color:green'>Thanks For Registeration</h1>")
    return render(request,'index.html',{'uform':form})

def uslogin(request):
    if request.method == "POST":
        name = request.POST['un']
        pswd = request.POST['pwd']
        print(name,pswd)
        authUser = authenticate(username=name, password=pswd)
        if authUser:
            if authUser.is_active:
                login(request,authUser)
                return HttpResponse("<h1 style='color:green'>Login Success!!!</h1>")
                # return HttpResponseRedirect('/dashboard')
            else:
                return HttpResponse("<h1>Sorry!!! You are Not Active user / So you can't Login</h1>")
        else:
            print("Sorry!! You are not authenticated")
    return render(request,'login.html')
