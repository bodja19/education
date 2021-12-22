from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse
from django.contrib.auth.models import User

def index(request):
    user = User.objects.all()
    return render(request, 'finances/login.html', {'users': user})
