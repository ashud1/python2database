import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

# FAKE pop script

import random
from first_app.models import AccessRecord, Topic , Webpage,User
from faker import Faker

fakegen=Faker()
# topic=['Search','Social','Marketplace','News','Games']

# def add_user():
#     t=Topic.objects.get_or_create(top_name=random.choice())[0]
#     t.save()
#     return t

def populate(N=5):

    for entry in range(N):

        # get the topic for the entry 

        # top=add_user()

        # create the fake data for that entry 

        fake_name=fakegen.name().split()
        fake_firstname=fake_name[0]
        fake_lastname=fake_name[1]
        fake_email=fakegen.email()

        # create a new web page entry 
        user=User.objects.get_or_create(first_name=fake_firstname,last_name=fake_lastname,email=fake_email)[0]

        # create a fake access record eot that webpage



if __name__=='__main__':
    print("populating script!")
    populate(20)
    print("populate completed!")