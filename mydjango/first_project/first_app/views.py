from django.shortcuts import render

from first_app.models import Topic,Webpage,AccessRecord,User

# Create your views here.

from django.http import HttpResponse

def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list}
    my_dict={'insert_me':"now i am coming from first_app/index.html"}
    # return render(request,'first_app/index.html',context=my_dict)
    return render(request,'first_app/index.html',context=date_dict)


def users(request):
    userinfo=User.objects.order_by('first_name')
    user_dict={'user_info':userinfo}
    return render(request,'first_app/users.html',context=user_dict)