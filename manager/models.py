from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(default="Ma'lumot qo'shilmadi.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


