from django.urls import path, include
from . import views
from .views import contactus, courses
urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('caresoul', views.caresoul, name='caresoul'),

    path('contactus', contactus.as_view(), name = 'contactus'),
    path('courses', views.courses, name = 'courses'),
    path('caresoul', views.courses, name = 'courses'),
    path('success/', views.success, name='success'),
    path('about', views.about, name='about'),
]

