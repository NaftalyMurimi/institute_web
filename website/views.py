from django.shortcuts import render
from django.http import HttpResponse
from .models import CoursesModel
from .models import ContactModel
from .forms import MyModelForm
from django.views.generic.edit import CreateView
# Create your views here.
# def homepage(request):
#     # return HttpResponse('We are building this')
#     return render(request, 'homepage.html')

def homepage(request):
    courses = CoursesModel.objects.all()
    return render (request=request,
                   template_name='homepage.html',
                   context= {"courses": courses})

def success(request):
    return render(request, 'success.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'includes/courses.html')


class contactus(CreateView):
    model = ContactModel
    form_class = MyModelForm
    template_name = 'contactus.html'
    
    success_url = '/success/'  # URL to redirect to after successful message submission
