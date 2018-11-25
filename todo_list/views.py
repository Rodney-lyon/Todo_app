from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def about(request):
    my_name = 'John Elder'
    return render(request, 'about.html', {'name': my_name})