from django.shortcuts import render

# Create your views here.
def calcolators(request):
    return render(request, 'index.html')

