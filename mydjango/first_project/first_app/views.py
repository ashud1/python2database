from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    my_dict={'insert_me':"now i am coming from first_app/index.html"}
    return render(request,'first_app/index.html',context=my_dict)
