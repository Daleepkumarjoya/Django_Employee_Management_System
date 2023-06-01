from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
# Create your views here.
from .models import Employee, aboutModel


def Home(request):
    EmpHome = Employee.objects.all()
    params = {'EmpHome': EmpHome}
    return render(request, 'home.html', params)


def about(request):
    AbaboutModel = aboutModel.objects.all()
    params = {'AbaboutModel': AbaboutModel}
    return render(request, 'about.html', params)


def AddEmp(request):
    if request.method == 'POST':
        name = request.POST.get('EmpName')
        email = request.POST.get('EmpEmail')
        EmployeeId = request.POST.get('EmpId')
        PhoneNumber = request.POST.get('EmpPhone')
        address = request.POST.get('EmpAddress')
        working = request.POST.get("EmpWorking")
        if working is None:
            working = False
        else:
            working = True
        department = request.POST.get('EmpDep')
        EmpObject = Employee(name=name, email=email, EmployeeId=EmployeeId, PhoneNumber=PhoneNumber, address=address,
                             working=working, department=department)
        EmpObject.save()
        messages.success(request, 'Employee has been Added Successfully Please See It On Home Page')
        return redirect('/AddEmp')
    return render(request, 'Add_Employee.html')


def Empdelete(request, Id):
    EmpId = Employee.objects.get(pk=Id)
    EmpId.delete()
    print(Id)
    return redirect('/')


def EmpUpdate(request, Id):
    EmpUpdated = Employee.objects.get(pk=Id)
    params = {'EmpUpdated': EmpUpdated}
    print(Id)
    return render(request, 'EmpUpdate.html', params)


def Do_update(request, Empid):
    if request.method == 'POST':
        Emp_Do_Update = Employee.objects.get(pk=Empid)
        name = request.POST.get('EmpName')
        email = request.POST.get('EmpEmail')
        EmployeeId = request.POST.get('EmpId')
        PhoneNumber = request.POST.get('EmpPhone')
        address = request.POST.get('EmpAddress')
        working = request.POST.get("EmpWorking")

        if working is None:
            working = False
        else:
            working = True
        department = request.POST.get('EmpDep')
        Emp_Do_Update.name = name
        Emp_Do_Update.email = email
        Emp_Do_Update.EmployeeId = EmployeeId
        Emp_Do_Update.PhoneNumber = PhoneNumber
        Emp_Do_Update.address = address
        Emp_Do_Update.working = working
        Emp_Do_Update.department = department
        Emp_Do_Update.save()
        messages.success(request, 'Employee has been Updated Successfully')
    return redirect('/')


def register(request):
    if request.method == 'POST':
        Username = request.POST['UName']
        firstname = request.POST['Fname']
        lastname = request.POST['Lname']
        Email = request.POST['Email']
        department = request.POST['department']
        Password = request.POST['Password']
        Cpassword = request.POST['CPassword']
        if len(Username) < 5:
            messages.error(request, 'Please Enter UserName More Than 5 Characters')
            return redirect('/register')
        if not Username.isalnum():
            messages.error(request, 'UserName Contains Only Letters And Numbers')
            return redirect('/register')
        if Password != Cpassword:
            messages.error(request, 'Please Enter Same Password Because This Password is not Matching')
            return redirect('/register')
        if User.objects.filter(username=Username).exists():
            messages.error(request, 'UserName has been Taken Enter Another')
        if User.objects.filter(email=Email).exists():
            messages.error(request, 'Email has been Taken Enter Another')

        user = User.objects.create_user(username=Username, email=Email, password=Password)
        user.first_name = firstname
        user.last_name = lastname
        user.department = department
        user.save()
        messages.success(request, 'you have Registered Successfully')
        return redirect('/EmpLogin')
    else:
        return render(request, 'Register.html')


def EmpLogin(request):
    if request.method == 'POST':
        UserName = request.POST['UName']
        Password = request.POST['Password']
        user = authenticate(username=UserName, password=Password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have Logged In Successfully')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/EmpLogin')
    return render(request, 'EmpLogin.html')


def Emplogout(request):
    auth.logout(request)
    return redirect('/')
