from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .models import *
from django.contrib.auth import authenticate
import time
import datetime
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'Trainer':
            tr_id = request.user
            studs = Assignee.objects.filter(trainer=tr_id).order_by('-id')
            return render(request, 'home.html', {'studs': studs})

    students = Student.objects.all().order_by('-id')
    trainers = User.objects.filter(user_type='Trainer')

    return render(request, 'home.html', {"students": students,
                                         "trainers": trainers})


def login(request):
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pass')

        user_obj = User.objects.filter(username=u).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('login')

        user = authenticate(username=u, password=p)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('login')

        if user is not None:
            auth.login(request, user)
            return redirect('home')                                                                                                                                                                                                                                      

    return render(request, 'login.html')


def signup(request):                                                                                               
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user_type = request.POST['user_type']

        try:
            user_obj = User(first_name=firstname, last_name=lastname, username=username, email=email,
                            password=password, user_type=user_type)
            user_obj.set_password(password)
            user_obj.save()
            return redirect('login')
             
        except Exception as e:
            print(e)

    return render(request, "signup.html")


def add_student(request):
    return render(request, "student.html")


def saveStudent(request):
    std = Student()

    std.name = request.POST.get('name')
    std.email = request.POST.get('email')
    std.contact = request.POST.get('contact')
    std.college = request.POST.get('clg')
    std.degree = request.POST.get('degree')
    std.grad_year = request.POST.get('year')

    std.save()
    return redirect('home')


def save_followup(request, id):
    follow = Student.objects.get(id=id)
    follow.follow_up1 = request.POST.get('follow_up1')
    follow.follow_up2 = request.POST.get('follow_up2')
    follow.follow_up3 = request.POST.get('follow_up3')
    follow.comments = request.POST.get('comment')
    follow.save()
    return redirect('home')


def save_assignee(request, id):
    ass = Assignee()
    std = Student.objects.get(id=id)

    trainer = request.POST.get('trainer')
    trainer = User.objects.get(id=trainer)

    ass.trainer = trainer
    ass.stud_id = std

    ass.save()
    return redirect('home')


def savefollowup(request, id):
    follow = Student.objects.get(id=id)
    follow.follow_up1 = request.POST.get('follow_up1')
    follow.follow_up2 = request.POST.get('follow_up2')
    follow.follow_up3 = request.POST.get('follow_up3')
    follow.comments = request.POST.get('comment')

    follow.save()
    return redirect('home')


def editStudent(request, id):
    std = Student.objects.get(id=id)

    return render(request, 'editstudent.html', {'std': std})


def updateStudent(request, id):
    std = Student.objects.get(id=id)
    std.name = request.POST.get('name')
    std.email = request.POST.get('email')
    std.contact = request.POST.get('contact')
    std.college = request.POST.get('clg')
    std.degree = request.POST.get('degree')
    std.grad_year = request.POST.get('year')

    std.save()
    return redirect('home')


def edit_student(request, id):
    std = Student.objects.get(id=id)
    return render(request, 'editstudent.html', {'std': std})

