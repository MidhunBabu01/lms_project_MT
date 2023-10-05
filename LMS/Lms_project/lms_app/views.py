from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import * 
# Create your views here.
def index(request):
    return render(request,'index.html')


def instructors_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect("lms_app:instructors_register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email  already registered")
                return redirect("lms_app:instructors_register")
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name = first_name,
                    last_name = last_name,
                    password=password2,
                    is_superuser=True,
                    is_staff=True,
                    is_active=True
                )
                user.save();
                print("user created")
                if 'username' in request.session:
                    request.session.flush();
                return redirect('lms_app:login')
        else:
            messages.info(request,"Invalid Password")
            return redirect('lms_app:instructors_register')
    return render(request,'register.html')


def login(request):
     if 'username' in request.session:
        return redirect('lms_app:index')
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            request.session['username'] = username
            auth.login(request,user)
            return redirect('lms_app:index')
        else:
            auth.login
            messages.error(request,'invalid Credentials')
            return redirect('lms_app:login')
     else:
        return render(request,'login.html')
     



def dashbaord(request):
    
    return render(request,'dashboard.html')



def instructor_course(request):
    courses = Coursess.objects.filter(added_by__username = request.user.username)
    context = {
        'courses':courses
    }
    return render(request,'instructor-course.html',context)



def create_course(request):
    form = AddCourse()
    if request.method == 'POST':
        form = AddCourse(request.POST,request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            added_by = User.objects.get(username=request.user.username)
            data.added_by = added_by
            data.save()
            messages.success(request,'Added..')
            return redirect('lms_app:instructor_course')
    else:
        form = AddCourse()
    context ={
        'form':form
    }  
    return render(request,'create-course.html',context)


def edit_course(request,update_id):
    update = Coursess.objects.filter(id=update_id).first()
    if request.method == 'POST':
        form = AddCourse(request.POST,request.FILES,instance=update)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated..')
            return redirect('lms_app:instructor_course')
    else:
        form = AddCourse(instance=update)
    return render(request,'edit-course.html',{'form':form})



def delete_course(request,delete_id):
    dlt = Coursess.objects.get(id=delete_id)
    dlt.delete()
    messages.success(request,'Deleted...')
    return redirect('lms_app:instructor_course')