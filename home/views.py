#home/views.py
from django.shortcuts import render

# Create your views here.
def index(request):
    kdict = {
        'siteTitle':'Khmer Web',
        'pageTitle': 'Home',
        'message': 'ស្វាគមន៍​មក​កាន់​ទំព័រ​ដើម!'
    }
    
    return render(request,'base.html',context={'data':kdict})