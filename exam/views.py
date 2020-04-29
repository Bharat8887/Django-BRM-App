from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
que=">Who developed C Language?"
a="Ken Thompson"
b="Dennis Ritchie"
c="Bjarne Stroustrup"
d="Saurabh Shukla"
data={"que":que,"a":a,"b":b,"c":c,"d":d}
def showtest(request):
    res=render(request,"exam/test.html",context=data)
    return res
def showResult(request):
    s="<h1>this is show Result page</h1>"
    return HttpResponse(s)
def showland(request):
    s="<h1>this is show Landing page</h1>"
    return HttpResponse(s)
