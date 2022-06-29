import os
from urllib import request
from django.shortcuts import render,redirect
from adminapp.models import  course,student,usermember,User
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def homepage(request):
    return render(request,'home.html')


def loginpage(request):
    return render(request,'login.html')

@login_required(login_url='loginpage')
def admin_welcome(request):
    return render(request,'admin/welcome.html')


@login_required(login_url='load_signup')
def tutor_welcome(request):
    return render(request,'tutor/tutor_welcome.html')

   
def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('admin_welcome')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'welcome {username}')
                return redirect('tutor_welcome')
        else:
            messages.info(request,"invalid username or password")
            return redirect('loginpage')
    return render(request,'home.html')

@login_required(login_url='loginpage')            
def load_addcourse(request):
    return render(request,'admin/add_course.html')

@login_required(login_url='loginpage')
def add_course(request):
    if request.method=='POST':
        crs_name=request.POST['cname']
        crs_fees=request.POST['cfees']
        crs=course(course_name=crs_name,course_fee=crs_fees)
        crs.save()
        print('hi')
        return redirect('load_addcourse')
    return render(request,'admin/add_course.html')
    
@login_required(login_url='loginpage')
def load_addstudent(request):
    courses=course.objects.all()
    return render(request,'admin/add_student.html',{'courses':courses})

@login_required(login_url='loginpage')
def add_student(request):
    if request.method=='POST':
        s_name=request.POST['sname']
        s_address=request.POST['aname']
        s_age=request.POST['age']
        s_jdate=request.POST['dname']
        sel1=request.POST['sel']
        course1=course.objects.get(id=sel1)
        std=student(student_name=s_name,student_address=s_address,student_age=s_age,join_date=s_jdate,course=course1)
        std.save()
        print('hi')
        return redirect('load_addstudent')
    return render(request,'admin/add_student.html')

@login_required(login_url='loginpage')
def show_student(request):
    context=student.objects.all()
    return render(request,'admin/show_student.html',{'dataread':context})



def load_signup(request):
    courses=course.objects.all()
    return render(request,'signup.html',{'courses':courses})


def tutor_signup(request):
    if request.method=='POST':
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        address=request.POST.get('adname')
        email=request.POST.get('email')
        uname=request.POST.get('username')
        pname=request.POST.get('password')
        cname=request.POST.get('cpassword')
        gender=request.POST.get('gender')
        mobilee=request.POST.get('mname')
        cel1=request.POST['cel']
        course1=course.objects.get(id=cel1)
        if request.FILES.get('photo') is not None:
            photo=request.FILES['photo']
        else:
            photo="static/images/default.png"
        if cname==pname:
            if User.objects.filter(username=uname).exists():
               messages.info(request,'username not available')
               return redirect('load_signup')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'email not available')
                 return redirect('load_signup')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,password=pname,username=uname,email=email)
                user.save()
                u=User.objects.get(id=user.id)
                member=usermember(user_address=address,user_gender=gender,user_mobile=mobilee,user_photo=photo,course=course1,user=u)
                member.save()
                return redirect('loginpage')
    return render(request,'signup.html')

def profile(request):
    user=usermember.objects.filter(user=request.user)
    return render(request,'tutor/show_profile.html',{'u':user})

@login_required(login_url='loginpage')
def edit_page(request,pk):
    students=student.objects.get(id=pk)
    courses=course.objects.all()
    return render(request,'admin/edit.html',{'students':students,'courses':courses})

@login_required(login_url='loginpage')
def edit_details(request,pk):
    if request.method=='POST':
        Student=student.objects.get(id=pk)
        sel1=request.POST.get('sel')
        Course=course.objects.get(id=sel1)
        Student.student_name=request.POST.get('sname')
    
        Student.student_address=request.POST.get('aname')
        Student.student_age=request.POST.get('age')
        
        Student.joining_date=request.POST.get('dname')
        Course.id=request.POST.get('sel')
       
        Student.save()
        Course.save()
        return redirect('show_student')
    return render(request,'admin/edit.html')

@login_required(login_url='loginpage')
def delete(request,pk):
    st=student.objects.get(id=pk)
    st.delete()
    return redirect('show_student')

@login_required(login_url='loginpage')
def show_tutor(request):
    c=usermember.objects.all()
    return render(request,'admin/show_tuters.html',{'c':c})


@login_required(login_url='loginpage')
def delete_tutor(request,pk):
    u=usermember.objects.get(id=pk)
    if u.user_photo is not None:
        if not u.user_photo=="/static/images/default.png":
            os.remove(u.user_photo.path)
        else:
            pass
    u.delete()
    return redirect('show_tutor')

@login_required(login_url='loginpage')
def admin_logout(request):
    auth.logout(request)
    return render(request,'home.html')

@login_required(login_url='load_signup')
def tutor_logout(request):
    auth.logout(request)
    return render(request,'home.html')


@login_required(login_url='load_signup')
def load_edit_profile(request):
    return render(request,'tutor/edit_profile.html')




def edit(request):
    if request.user.is_authenticated:
        current_user = request.user
        print (current_user.id)
        user1=usermember.objects.get(user_id=current_user)
        if request.method=="POST":
            if len(request.FILES)!=0:
                if len(user1.user_photo)>0:
                    os.remove(user1.user_photo.path)
                user1.user_photo=request.FILES.get('photo')
            user1.user.first_name=request.POST.get('first_name')
            user1.user.last_name=request.POST.get('last_name')
            user1.user.username=request.POST.get('username')
            user1.user.password=request.POST.get('password')
            user1.user.email=request.POST.get('email')
            
            user1.user_address=request.POST.get('adname')
            user1.user_mobile=request.POST.get('mname')
            user1.save()
            return redirect('profile')
        
        return render(request,'tutor/edit_profile.html',{'users':user1})
    return redirect('/')   



def profile(request):
    if request.user.is_authenticated:
        current_user = request.user
        print (current_user.id)
        user1=usermember.objects.get(user_id=current_user)
        return render(request,'tutor/show_profile.html',{'users':user1})
