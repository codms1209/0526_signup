from django.shortcuts import render
from .models import Major
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    posts = Major.objects
    return render(request, 'blog/home.html',{'posts':posts})