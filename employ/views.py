from django.shortcuts import render
from employ.models import Employee
from django.http import Http404,HttpResponse
# Create your views here.
def employ_details(request,id):
       try:
           employee = Employee.objects.get(id =id)
           return HttpResponse(employee)
       except:
             raise Http404
             