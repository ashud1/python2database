from django.shortcuts import render

# Create your views here.
from . import forms


def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form=forms.MyForm()

    if request.method=="POST":
        form=forms.MyForm(request.POST)
        if form.is_valid():
            # do something 
            print("validation success")
            print("Name:"+form.cleaned_data["name"])
            print("email:"+form.cleaned_data["email"])
            print("text:"+form.cleaned_data["text"])
    return render(request,'basicapp/form_page.html',{'form':form})