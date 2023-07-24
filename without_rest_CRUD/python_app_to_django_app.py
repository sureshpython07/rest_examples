import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
end_point='apiwithout_rest_crud/emp/'

# retrieving resource from django application
# GET
def get_resource(id):
    resp=requests.get(BASE_URL+end_point+id)
    print('Employee Data from DJango Application')
    print('#'*40)
    print(resp.status_code)
    print(resp.json())
#id=input('Enter Some Emp Id')
#get_resource(id)  # calling above function

end_point='apiwithout_rest_crud/emp_serialize/'
def get_resp_serialize(id):
    resp=requests.get(BASE_URL+end_point+id)
    print(resp.status_code)
    #if resp.status_code in range(200,300):
    if resp.status_code == requests.codes.ok:
        print(resp.json()) 
    else:
        print('some thing goes worng')

#get_resp_serialize(id)  # calling above function


end_point='apiwithout_rest_crud/emp_list_serialize'
def get_emp_list():
    resp=requests.get(BASE_URL+end_point)
    print('Employee Data from DJango Application')
    print('#'*40)
    print(resp.status_code)
    print(resp.json()) 
#get_emp_list()  # calling above function


# Creating resources of Django application from here.
# POST
end_point1='apiwithout_rest_crud/emp_list_serialize'
def create_resource():
    emp = {
        'eno' : 1006,
        'ename' :'Kalli',
        'esal' : 30000.00,
        'eadd' : 'Hyderabad'
    }
    json_data = json.dumps(emp)
    resp=requests.post(BASE_URL+end_point1,data=json_data)
    print(resp.status_code)
    print(resp.json())
create_resource()

