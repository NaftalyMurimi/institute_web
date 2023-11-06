from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    # return HttpResponse('We are building this')
    return render(request, 'homepage.html')