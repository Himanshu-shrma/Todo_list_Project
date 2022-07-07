from django.shortcuts import redirect, render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .forms import TaskForm
from django.contrib import messages
from .models import Task
# Create your views here.

def tasklist(request):
    if request.user.is_authenticated:
        tlist= Task.objects.filter(user=request.user.id)
        return render(request,'base/task_list.html',{'tlist':tlist})
    else:
        return redirect('login-user')

def show_task(request,task_id):
    tdetail=Task.objects.get(pk=task_id)
    return render(request,'base/show_task.html',{
        'tdetail':tdetail,
    })

def edit_task(request,task_id):
    task=Task.objects.get(pk=task_id)
    form=TaskForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,"base/edit_task.html",{
        'form':form,
        'task':task
    })



    
def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
            messages.success(request,("Event Added Successfully!! "))
            return redirect('home')  
    form=TaskForm
    return render(request,'base/add_task.html',{
        'form':form,
    })
    
def delete_task(request,task_id):
    task=Task.objects.get(pk=task_id)
    task.delete()
    messages.success(request,'Task Deleted!!')
    return redirect('home')

def update_task(request,task_id):
    task=Task.objects.get(pk=task_id)
    val=task.complete
    if val:
        task.complete=False
        task.save()
    else:
        task.complete=True
        task.save()
    return redirect('home')
    
