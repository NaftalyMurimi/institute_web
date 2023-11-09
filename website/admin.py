from django.contrib import admin
from .models import CoursesModel, AdvertModel, ContactModel
# Register your models here.

admin.site.register(CoursesModel)
admin.site.register(AdvertModel)

admin.site.register(ContactModel)

