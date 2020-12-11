from django.shortcuts import render
from runTg import views as rviews

# Create your views here.
def index(request):
    # login first
    if 'id' not in request.session or request.session['id'] == '':
        return render(request, './login.html')
    return render(request, 'index.html')
    
def agency(request):
    return render(request, 'agency.html')

def deal(request):
    return render(request, 'deal.html')

def details(request):
    return render(request, 'details.html')