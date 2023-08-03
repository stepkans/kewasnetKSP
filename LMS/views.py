from django.shortcuts import redirect, render
from app.models import Categories
from django.contrib.auth.decorators import login_required

def BASE(request):
    return render(request,'base.html')

def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]

    context = {
        'category': category,
    }
    return render(request, 'Main/home.html', context) 

def SINGLE_COURSE(request):
    return render(request,'Main/single_course.html')
def course(request):
    return render(request,'Main/course.html')

def CONTACT_US(request):
    return render(request,'Main/contact_us.html')

def ABOUT_US(request):
    return render(request,'Main/about_us.html')

def PILLARS(request):
    return render(request,'Main/pillars.html')

