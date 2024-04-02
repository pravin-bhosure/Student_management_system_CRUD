from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Student, subject
# from .forms import Register
# from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'home.html')


def loginin(request):
    return render(request, 'loginin.html')


@login_required(login_url='/')
def stu_list(request):
    stud = Student.objects.all()
    sub = subject.objects.all()

    mylist = zip(stud, sub)
    return render(request, 'list.html', {"mylist": mylist})
    # return HttpResponseRedirect(reversed('loginin.html'))


@login_required(login_url='/')
def stu_add(request):

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        Address = request.POST['Address']
        Contact = request.POST['Contact']
        Class = int(request.POST['Class'])
        subject_name = int(request.POST['subject_name'])

        user = Student(fname=fname, lname=lname, Address=Address,Contact=Contact, Class=Class, subject_name_id=subject_name)
        user.save()
        stud = Student.objects.all()
        sub = subject.objects.all()
        
        return render(request,'list.html',{'mylist':zip(stud,sub)})

    elif request.method == "GET":

        sub = subject.objects.all()
        return render(request, 'add.html', {"sub": sub})


@login_required(login_url='/')
def stu_filter(request):
    
    if request.method == 'POST':
        fname = request.POST['fname']
        stud = Student.objects.all()
        sub = subject.objects.all()
        

        if fname:
            stud = stud.filter(fname__icontains=fname)
            return render(request, 'list.html', {'mylist': zip(stud,sub)})

    elif request.method == 'GET':
        return render(request, 'filter.html')
    return render(request, 'filter.html')


@login_required(login_url='/')
def stu_delete(request, stu_id=0):
    stud = Student.objects.all()

    if stu_id:
        try:
            stu_to_be_removed = Student.objects.get(id=stu_id)
            stu_to_be_removed.delete()
            return redirect('loginin')
        except:
            return HttpResponse('An error occured!!')
    print(stu_id)
    return render(request, 'delete.html', {'stud': stud})


@login_required(login_url='/')
def update(request, stu_id=0):

    if request.method == 'GET':
        data = Student.objects.get(id=stu_id)
        return render(request, 'update.html', {'data': data})


@login_required(login_url='/')
def do_update(request, stu_id=0):

    if request.method == 'POST':
        stu_id = request.POST['ID']
        fname = request.POST['fname']
        lname = request.POST['lname']
        Address = request.POST['Address']
        Contact = request.POST['Contact']
        Class = int(request.POST['Class'])
        subject_name = request.POST['subject_name']

        Student.objects.filter(id=stu_id).update(id=stu_id, fname=fname, lname=lname,
                                                 Address=Address, Contact=Contact, Class=Class, subject_name_id=subject_name)

        return redirect('loginin')
    return render(request, 'list.html')


def stu_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)

        print(user)
        if user is not None:
            login(request, user)
            print('login')
            fname = user.username
            messages.success(request, "Welcome",)
            return render(request, 'loginin.html', {'fname': fname})

        else:
            print('ji')
            messages.error(request, "Invalid credentials")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def stu_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist')
                return render(request, 'register.html')

            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exist')
                return redirect('register')

            else:
                if len(username) == 0 or len(email) == 0 or len(password1) == 0 or len(password2) == 0:
                    messages.error(request, 'Enter every data!')
                    return render(request, 'register.html')

                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=password1)
                    user.save()
                    messages.success(request, 'User created successfully')
                    print("User cretated succesully")
                    return render(request, 'login.html')

    else:
        print('hiiiiii')
        return render(request, 'register.html')
    return render(request, 'login.html')


def stu_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return render(request, 'login.html')
