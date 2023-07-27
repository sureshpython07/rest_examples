import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
end_point='apiwithout_rest_crud/api_single_endpoint'

# retrieving resource from django application
# GET
# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#             }
#     resp=requests.get(BASE_URL+end_point,data=json.dumps(data))
#     print('Employee Data from DJango Application')
#     print('#'*40)
#     print(resp.status_code)
#     print(resp.json())
# get_resource(2)

# def create_resource():
#     data={
#         'eno': 1010,
#         'ename' : 'ABC',
#         'esal' : 40000,
#         'eadd' : 'Delhi'
#         }
#     resp=requests.post(BASE_URL+end_point,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()

# def update_resource(id):
#     data={
#         'id' : id,
#         'esal' : 40000,
#         'eadd' : 'Delhi'
#         }
#     resp=requests.put(BASE_URL+end_point,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(20)

def resource_delete(id):
    data={
        'id':id
    }
    resp=requests.delete(BASE_URL+end_point,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
resource_delete(15)