from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *
from django.db import IntegrityError


# Create your views here.
def studenthomepage(request):
    return render(request,'student_record/homepage.html')

def showstu(request):
    return render(request,'student_record/show.html',context={'stu':student.objects.all()})

def createstu(request):
    if (request.method=="POST"):
        form=Form(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('showstu')
        else:
            raise IntegrityError()
    
    return render(request,'student_record/create.html',context={'stu':Form()})

def editstu(request,rno):
    selected_stu= student.objects.get(roll_no=rno)
    form=Form(request.POST or None,instance=selected_stu,initial=selected_stu.__dict__)
    if(request.method=='POST'):
        if(form.is_valid()):
            form.save()
        return redirect('showstu')
    return render(request,'student_record/update.html',context={'stu':selected_stu,'form':form})

def deletestu(request,rno):
    selected_stu= student.objects.get(roll_no=rno)
    selected_stu.delete()
    return redirect('showstu')