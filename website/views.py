from django.shortcuts import render
from django.http import HttpResponse
from .models import CoursesModel
# Create your views here.
# def homepage(request):
#     # return HttpResponse('We are building this')
#     return render(request, 'homepage.html')

def homepage(request):
    courses = CoursesModel.objects.all()
    return render (request=request,
                   template_name='homepage.html',
                   context= {"courses": courses})
