from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Data
0.# Create your views here.

def update_division(request):
    # Your logic here
    sample=list(Data.objects.all().values('id','Name'))
    data = {"message": sample}
    return JsonResponse(data)  # Return JSON data

def update_division_html(request):
    sample='data'
    return render(request, 'home.html', {'data': sample})



def home(request):
    data=Data.objects.all()
    return render(request, 'home.html',{'data':data})


def add(request):
    if request.method == 'POST':
        name=request.POST['name']
        data=Data.objects.create(Name=name)
        data.save()
        return redirect(add)
    return render(request, 'add.html')

def demo(req):
    return render(req,'demo.html')