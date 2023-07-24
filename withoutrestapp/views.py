from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
import json
# Create your views here.
# function based views
def emp_dataview(request):
    emp_data={
        'eno': 1000,
        'ename' : 'Suresh',
        'esal' : 10000
    }
    return HttpResponse('employee info : eno {} ename {} esal {}'.
                        format(emp_data['eno'],emp_data['ename'],emp_data['esal']))

def emp_data_json_view(request):
    emp_data={
        'eno': 1000,
        'ename' : 'Suresh',
        'esal' : 10000
    }
    json_data=json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')

def emp_data_json_view2(request):
    emp_data={
        'eno': 1000,
        'ename' : 'Suresh',
        'esal' : 10000
    }
    return JsonResponse(emp_data)

# class based on views
# every class based view are chlid class of View class 
from django.views.generic import View
class JsonCBV(View):
    '''  using json response
        def get(self,request,*args,**kwargs):
            emp_data={
            'eno': 1000,
            'ename' : 'Suresh',
            'esal' : 10000
    }
        return JsonResponse(emp_data)
        '''
    # using http response
    def get(self,request,*args,**kwargs):
        data={'msg' : 'This is Get request class based view'    }
        return HttpResponse(json.dumps(data),content_type='application/json')

    def post(self,request,*args,**kwargs):
        data={'msg' : 'This is post request class based view'    }
        return HttpResponse(json.dumps(data),content_type='application/json')
    
    def put(self,request,*args,**kwargs):
        data={'msg' : 'This is Put request class based view'    }
        return HttpResponse(json.dumps(data),content_type='application/json')
    
    def delete(self,request,*args,**kwargs):
        data={'msg' : 'This is Delete request class based view'    }
        return HttpResponse(json.dumps(data),content_type='application/json')
# using mixin class
from withoutrestapp.mixin import HttpResponseMixin
class JsonCBVMixin(HttpResponseMixin,View):
    
    # using mixin class http response
    def get(self,request,*args,**kwargs):
        json_data={'msg' : 'This is Get request class based view'    }
        return self.render_http_resp(json_data)

    def post(self,request,*args,**kwargs):
        json_data={'msg' : 'This is post request class based view'    }
        return self.render_http_resp(json_data)
    
    def put(self,request,*args,**kwargs):
        json_data={'msg' : 'This is Put request class based view'    }
        return self.render_http_resp(json_data)
    
    def delete(self,request,*args,**kwargs):
        json_data={'msg' : 'This is Delete request class based view'    }
        return self.render_http_resp(json_data)