from django.shortcuts import render
from .models import myform

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
