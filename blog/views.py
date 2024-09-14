from django.shortcuts import render
from django.http import HttpResponse
from . import models



def hello_world_view(request):
    return HttpResponse("<h1>Hello world !!!</h1>")


# post_view


def post_view(request):
    post = models.Post_club.objects.all()
    return render(request, 'index.html', {'post': post})