from django.core.serializers import serialize
from django.http import HttpResponse
import json
class SerializeMixin(object):
    def serialize(self,qs):
        json_data=serialize('json',qs)
        p_list=json.loads(json_data)
        final_list=[]
        for emp in p_list:
            emp_data=emp['fields']
            final_list.append(emp_data)
        json_data=json.dumps(final_list)
        return json_data

class HttpResponseStausMixin(object):
    def httpresponse_withstatus(self,json_data,status=200):
        return HttpResponse(json_data,content_type='application/json',status=status)