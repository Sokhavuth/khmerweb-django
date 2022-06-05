from django.shortcuts import render

# Create your views here.
def index(request):
    kdict = {
        'siteTitle':'Khmer Web'
    }
    
    return render(request,'index.html',context={'data':kdict})