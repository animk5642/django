from django.http import HttpResponse

from django.shortcuts import render

from employ.models import Employee



def home(request):    
    emloyess=Employee.objects.all()
    emplo ={

       'employees':emloyess,


    }
    return render(request,'home.html',emplo)
   
     

def home2(request):
    return render(request,'home2.html')