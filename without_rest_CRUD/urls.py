from django.urls import path
from without_rest_CRUD import views 
urlpatterns = [
    path(r'emp/<int:id>',views.EmployeeDetailsCBV.as_view()),
    path(r'emp_serialize/<int:id>',views.EmployeeDetailsCBV_Serialize.as_view()),
    path(r'emp_list_serialize',views.Employee_ListCBV_Serialize.as_view()), 
    path(r'api_single_endpoint',views.EmployeeCBVSingleEndPoint.as_view()),    
]
