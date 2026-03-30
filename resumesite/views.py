from django.shortcuts import render
def home(request):
    return render(request, 'resumesite/home.html')

# Create your views here.
