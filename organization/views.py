from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'users/index.html')
    # return render(request, 'landing/index.html')