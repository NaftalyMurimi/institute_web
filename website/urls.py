from django.urls import path, include
from . import views
from .views import contactus
urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('success/', views.success, name='success')

    path('contactus', contactus.as_view(), name = 'contactus'),
    path('success/', views.success, name='success'),
    path('about', views.about, name='about'),
]

