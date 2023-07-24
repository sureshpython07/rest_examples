from django.shortcuts import render
from django.views.generic import View
from without_rest_CRUD.models import Employee
from django.http import HttpResponse
import json
from django.core.serializers import serialize
from without_rest_CRUD.mixin import SerializeMixin,HttpResponseStausMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from without_rest_CRUD.util import is_json_valid
from without_rest_CRUD.forms import EmployeeForm

# Create your views here.
class EmployeeDetailsCBV(View):
    def get(self,request,id,*args,**kwargs):
        emp=Employee.objects.get(id=id)
        emp_data = {
            'eno' : emp.eno,
            'ename' : emp.ename,
            'esal' : emp.esal ,
            'eadd' :emp.eadd
        }
        json_data = json.dumps(emp_data)
        print('Data',json_data)
        return HttpResponse(json_data,content_type='application/json')

 #using mixin class   
class EmployeeDetailsCBV_Serialize(SerializeMixin,HttpResponseStausMixin,View):
    def get(self,request,id,*args,**kwargs):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data=json.dumps({'msg':'The requested records not available'})
            return self.httpresponse_withstatus(json_data,404)
        else:
            # json_data=serialize('json',[emp]) taking all fields 
            #json_data=serialize('json',[emp],fields=('eno','ename'))  taking only specific fields 
            json_data= self.serialize([emp])
            return self.httpresponse_withstatus(json_data,200)
#inheriting mixin class    
@method_decorator(csrf_exempt,name='dispatch')
class Employee_ListCBV_Serialize(SerializeMixin,HttpResponseStausMixin,View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        json_data=self.serialize(qs)
        return self.httpresponse_withstatus(json_data,200)

    def post(self,request,*args, **kwargs):
        data = request.body
        valid_data = is_json_valid(data)
        if not valid_data:
            json_data=json.dumps({'msg': 'Please Send valid data only'})
            return self.httpresponse_withstatus(json_data,400)
        #json_data=json.dumps({'msg': 'You provided valid json data only'})
        emp_data=json.loads(data)
        form=EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg': 'Resource Created successfully'})
            return self.httpresponse_withstatus(json_data,200)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.httpresponse_withstatus(json_data,400)
