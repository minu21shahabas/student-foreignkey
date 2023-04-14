from django.shortcuts import render,redirect
from forapp.models import addcourse
from forapp.models import addstudent

# Create your views here.
def index(request):
    return render(request,'home.html')
def add(request):
    return render(request,'addcourse.html')
def add_course(request):
     if request.method=='POST':
        coursename=request.POST['cname']
        fees=request.POST['amount']
        stud=addcourse(course_name=coursename,fees=fees)
        stud.save()
        return redirect('/')
def stud(request):
    courses=addcourse.objects.all()
    return render(request,'addstud.html',{'course':courses})
def addstud(request):
    if request.method=='POST':
        sname=request.POST['name']
        age=request.POST['age']
        ad=request.POST['adrs']
        joind=request.POST['date']
        mobilenum=request.POST['num']
        sel=request.POST['subject']
        course1=addcourse.objects.get(id=sel)
        stud=addstudent(name=sname,age=age,address=ad,joining_date=joind,phone_no=mobilenum,course=course1)
        stud.save()
        return redirect('/')
def show(request):
    stud=addstudent.objects.all()
    return render(request,'showdetails.html',{'student':stud})
def editpage(request,id):
    edits=addstudent.objects.get(id=id)
    editc=addcourse.objects.all()
    return render(request,'edit.html',{'studen':edits,'course':editc})
def editstudent(request,id):
    if request.method=='POST':
        stud=addstudent.objects.get(id=id)

        stud.name=request.POST['name']
        stud.address=request.POST['adrs']
        stud.age=request.POST['age']
        stud.joining_date=request.POST['date']
        stud.phone_no=request.POST['num']

        stud.save()
        return redirect('show')
    return render(request,'editstud.html')
def delete(request,id):
    stud=addstudent.objects.get(id=id)
    stud.delete()
    return redirect('show')