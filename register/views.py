from django.shortcuts import render
from .models import Titles
# Create your views here.
def register(request):
    news = Titles.objects.all
    return render(request, 'register/register.html', {'news': news})