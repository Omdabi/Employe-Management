from django.shortcuts import render,redirect,HttpResponse
from . forms import SignUpForm,d_form,r_form,e_form
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login as us_login,logout as us_logout , update_session_auth_hash
from .models import department,role,employe

# Create your views here.
def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')


def signup(request):
    if request.method =='POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'You Have Register Succesfully !!')
            return redirect('base')
    else:
        fm = SignUpForm()
        return render(request,'signup.html',{'fm':fm})



def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            my_user = authenticate(request ,username=username, password=password)
            if my_user is not None:
                us_login(request,my_user)
                messages.success(request, ('You Have Been Logged In!'))
                return redirect('home')
            else:
                messages.success(request, ('Error Logging In - Please Try Again...'))
                return redirect('login')
                
                
    else:
        fm = AuthenticationForm()
        return render(request, 'login.html', {'fm':fm})

def logout(request):
    us_logout(request)
    return redirect('base')


def adddepartment(request):
    if request.method == 'POST':
        fm = d_form(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            location = fm.cleaned_data['location']
            department(name=name,location=location).save()
            messages.success(request,'add succesfully')
            return redirect('adddepartment')  
    else:
        fm = d_form()
        return render(request,'adddepartment.html',{'fm':fm})


def addemploye(request):
    if request.method == 'POST':
        fm = e_form(request.POST)
        if fm.is_valid():
            fname = fm.cleaned_data['fname']
            lname = fm.cleaned_data['lname']
            salary = fm.cleaned_data['salary']
            bonus = fm.cleaned_data['bonus']
            dept = fm.cleaned_data['dept']
            phone = fm.cleaned_data['phone']
            role = fm.cleaned_data['role']
            hired_date = fm.cleaned_data['hired_date']
            employe(fname=fname,lname=lname,salary=salary,bonus=bonus,dept=dept,phone=phone,role=role,hired_date=hired_date).save()
            messages.success(request,'add succesfully')
            return redirect('addemploye')  
    else:
        fm = e_form()
        return render(request,'addemploye.html',{'fm':fm})


def addrole(request):
    if request.method == 'POST':
        fm = r_form(request.POST)
        print("khelo---------------------------------------------------")
        if fm.is_valid():
            nam =  fm.cleaned_data['r_name']
            role(r_name = nam).save()
            return redirect("addrole")
    else:
        fm = r_form()
        return render(request,'addrole.html',{'fm':fm})


def ddetails(request):
    d = department.objects.all()
    return render(request,'showdata.html',{'data':d})

def rdetails(request):
    d = role.objects.all()
    return render(request,'rdetails.html',{'data':d})

def edetails(request):
    d = employe.objects.all()
    return render(request,'edetails.html',{'data':d})

def ddelete(request,did):
    d = department.objects.filter(id =did)
    d.delete()
    return redirect('ddetails')

def dedit(request,did):
    pk = department.objects.get(id=did)
    if request.method == 'POST':
        fm = d_form(request.POST,instance=pk)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            location = fm.cleaned_data['location']
            department(id=did,name=name,location=location).save()
            messages.success(request,'add succesfully')
            return redirect('ddetails')  
    else:
        fm = d_form(instance=pk)
        return render(request,'adddepartment.html',{'fm':fm})
