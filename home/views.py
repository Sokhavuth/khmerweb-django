#home/views.py
from django.shortcuts import render

# Create your views here.
def index(request):
    kdict = {
        'siteTitle':'Khmer Web'
    }
    
    return render(request,'base.html',context={'data':kdict})