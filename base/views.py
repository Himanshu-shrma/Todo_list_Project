from email import message
from django.shortcuts import redirect, render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .forms import TaskForm
from django.contrib import messages
from .models import Task
# Create your views here.


def add_task(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=TaskForm(request.POST)
            if form.is_valid():
                task=form.save(commit=False)
                task.user=request.user
                task.save()
                return redirect('home')  
        form=TaskForm
        return render(request,'base/add_task.html',{
            'form':form,
        })
    messages.success(request,"You Need to Log in First")
    return redirect('home')

def tasklist(request):
    if request.user.is_authenticated:
        tlist= Task.objects.filter(user=request.user.id)
        return render(request,'base/task_list.html',{'tlist':tlist})
    else:
        return redirect('login-user')

def show_task(request,task_id):
    if request.user.is_authenticated:
        
        if Task.objects.filter(pk=task_id):
            tdetail=Task.objects.get(pk=task_id)
            if request.user ==tdetail.user:
                return render(request,'base/show_task.html',{
                    'tdetail':tdetail,
                })
            else:
                messages.success(request,"You are Not Authorized to modify/check Other's Task")
                return redirect('home')
        else:
            messages.success(request,"No Such Task Exists !")
            return redirect('home')

    messages.success(request,"You need to log in first !")
    return redirect('home')

def edit_task(request,task_id):
    if request.user.is_authenticated:
        
        if Task.objects.filter(pk=task_id):
            task=Task.objects.get(pk=task_id)
            if request.user ==task.user:
                form=TaskForm(request.POST or None,instance=task)
                if form.is_valid():
                    form.save()
                    return redirect('home')
                return render(request,"base/edit_task.html",{
                    'form':form,
                    'task':task
                })
            else:
                messages.success(request,"You are Not Authorized to modify/check Other's Task")
                return redirect('home')
        else:
            messages.success(request,"No Such Task Exists")
            return redirect('home')
    messages.success(request,"You need to log in first !")
    return redirect('home')
   
    
def delete_task(request,task_id):
    if request.user.is_authenticated:
        
        if Task.objects.filter(pk=task_id):
            task=Task.objects.get(pk=task_id)
            if request.user ==task.user:
                task.delete()
                messages.success(request,'Task Deleted!!')
                return redirect('home')
            else:
                messages.success(request,"You are Not Authorized to modify/check other's Task")
                return redirect('home')
        else:
            messages.success(request,"No Such Task Exists")
            return redirect('home')
    messages.success(request,"You need to log in first !")
    return redirect('home')

def update_task(request,task_id):
    if request.user.is_authenticated:
       
        if Task.objects.filter(pk=task_id):
            task=Task.objects.get(pk=task_id)
            if request.user ==task.user:
                val=task.complete
                if val:
                    task.complete=False
                    task.save()
                else:
                    task.complete=True
                    task.save()
                return redirect('home')
            else:
                messages.success(request,"You are Not Authorized to do modify/check other's tasks ")
                return redirect('home')
        else:
            messages.success(request,"No Such Task Exists")
            return redirect('home')
    messages.success(request,"You need to log in first !")
    return redirect('home')
    
