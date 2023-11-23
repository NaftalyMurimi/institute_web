from django.db import models

# Create your model for posts here.
# this is the courses model
class CoursesModel(models.Model):
    course_title = models.CharField(max_length=100)
    course_description = models.TextField(max_length=1000)
    course_img = models.ImageField(upload_to=  'static/images/')
    course_requirements = models.CharField(max_length=200)
    course_duration = models.CharField(max_length= 100)
    course_cost = models.CharField(max_length= 100, default='')

    def __str__(self):
        return self.course_title

# this model holds contacts 
class ContactModel(models.Model):
    username =  models.CharField(max_length=100)
    user_email = models.EmailField(unique=True, blank=True)
    Phone_no =  models.CharField(max_length=100)
    email_subject =  models.CharField(max_length=100)
    email_message =  models.TextField(max_length=1000)

    def __str__(self):
        return self.email_subject
        
# This model holds the advert
class AdvertModel(models.Model):
    advert_title = models.CharField(max_length=1000)
    advert_img = models.ImageField(upload_to=  'static/adverts/')
    def __str__(self):
        return self.advert_title
        


