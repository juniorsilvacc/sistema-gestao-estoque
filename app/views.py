from django.shortcuts import render

from django.http import HttpResponse

def force_500(request):
    1 / 0  # Isso vai gerar ZeroDivisionError e causar erro 500
    return HttpResponse("Isso nunca vai ser executado")

def home(request):
    context = {}
    return render(request, 'pages/home.html')

def custom_500(request, exception=None):
    return render(request, 'errors/_500.html', status=500)

def custom_404(request, exception=None):
    return render(request, 'errors/_404.html', status=404)