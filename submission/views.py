from django.shortcuts import render, redirect
from django.views.generic import ListView,View
from .models import Assignment, Submission
from .forms import SubmissionForm ,student_loginform,student_regform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator

class homeview(View):
    def get(self,request):
        return render(request,'submission/home.html')
#decorators
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("home")
        else:
            return fn(request,*args,**kwargs)
    return wrapper
#register
class student_regview(View):
    def get(self,request,*args,**kwargs):
        form=student_regform()
        return render(request,"submission/signup.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=student_regform(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"registerd succesfully")
        else:
            messages.error(request,"signup first..")
        form=student_regform()
        return redirect("s_login")
#login
class student_loginview(View):
    def get(self,request,*args,**kwargs):
        form=student_loginform()
        return render(request,"submission/login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=student_loginform(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                login(request,user_obj)
                return redirect('assignment_list')
            else:
                print("oopss")
        return redirect("home")
#logout
class logoutview(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("home")


class AssignmentListView(ListView):
    model = Assignment
    template_name = 'submission/assignment_list.html'
    context_object_name = 'assignments'

@method_decorator(signin_required,name="dispatch")
class SubmissionFormView(View):
    def get(self,request,*args,**kwargs):
        form=SubmissionForm()
        return render(request,"submission/submission_form.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=SubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"submitted succesfully")
        else:
            messages.error(request,"invalid cridential")
        form=SubmissionForm()
        return redirect("assignment_list")

@method_decorator(signin_required,name="dispatch")
class SubmissionListView(View):
    def get(self,request,*args,**kwargs):
        data=Submission.objects.all()
        id=kwargs.get("pk")
        assign=Assignment.objects.get(id=id)
        return render(request,"submission/submission_list.html",{"data":data,"assign":assign})

