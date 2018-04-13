from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'model.html',{})


def main(request):
    return render(request, 'home.html',{})