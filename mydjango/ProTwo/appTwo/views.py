from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(requet):
    return HttpResponse("<em> My Second Project </em>")

def home(request):
    return HttpResponse("<p>This is the home page</p>")

def help(request):
    my_dict={"template_var":"This is added from tempalte"}
    return render(request,"app_Two/help.html",context=my_dict)