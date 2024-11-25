from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')