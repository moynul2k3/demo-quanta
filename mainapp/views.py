from django.shortcuts import render

#create your views here
def index(request):
    return render(request, 'mainapp/index.html')