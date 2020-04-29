from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
# Create your views here.
def greeting(request):
    s="<h1>Hello and Welcome to first view of Testapp</h1><p>This is Landing page</p1>"
    return HttpResponse(s)
def showContact(request):
    s="<h1>Contact Page</h1>"
    s+="<p>Website: mysirg.com<p1>"
    s+="<p>Mobile: 90542000087<p1>"
    s+="<p>Email: abc@gmail.com<p1>"
    return HttpResponse(s)
def about(request):
    msg="this is an about page"
    return render(request,"testapp/about.html",{"msg":msg})
def customtemplate(request):
    text="this is an about page"
    return render(request,"testapp/customtags.html",{"text":text})
def employee_info_view(request):
    employee=Employee.objects.all()
    data={'employee':employee}
    res=render(request,"testapp/employee.html",data)
    return res
