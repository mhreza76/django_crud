from django.shortcuts import render, redirect
from studentApp.forms import studentForm  
from studentApp.models import Student  

# Create your views here.  
def addnew(request):  
    if request.method == "POST":  
        form = studentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = studentForm()  
    return render(request,'studentApp/templates/index.html',  {'form':form})  
 
def index(request):  
    students = Student.objects.all()  
    return render(request,"show.html",{'students':students})  
 
def edit(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'edit.html', {'student':student})  
 
def update(request, id):  
    student = Student.objects.get(id=id) 
    form = studentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'student': student})  
     
def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/")