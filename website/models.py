from django.db import models

# Create your model for posts here.
class CoursesModel(models.Model):
    course_title = models.CharField(max_length=100)
    course_description = models.CharField(max_length=1000)
    course_img = models.ImageField(upload_to=  'static/course_images/')
    course_requirements = models.CharField(max_length=200)
    course_duration = models.CharField(max_length= 10)

    def __str__(self):
        return self.course_title


