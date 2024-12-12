from django.shortcuts import render
from .models import *
from datetime import datetime

def index(request):
    courses = Course.objects.all()
    students = Student.objects.all()

    context = {
        'courses': courses,
        'students': students,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    students = Student.objects.filter(course_id=course_id)

    context = {
        'courses': [course],
        'students': students,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)

    context = {
        'student': student,
        'current_year': datetime.now().year
    }

    return render(request, 'student.html', context)
