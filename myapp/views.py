from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm


def todoapp(request):
    if request.method == "POST":
        b = CreateUserForm(request.POST)
        if b.is_valid():
            b.save()
    b = CreateUserForm()
    c = todo.objects.all()
    return render(request, "todo.html", {"form":b, "data":c})


def delete(request, id):
    d = todo.objects.get(id=id)
    d.delete()
    return redirect("todo")

# Create your views here.
def index(request):
    if request.method == 'POST':
        a = myform()
        a.name=request.POST['name']
        a.email=request.POST['email']
        a.subject=request.POST['subject']
        a.message=request.POST['message']
        a.save()    
    return render(request , "index.html")
