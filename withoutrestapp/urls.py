from django.urls import path
from withoutrestapp import views

urlpatterns = [
    path('empstr',views.emp_dataview,name='emp_dataview'),
    path('empjson',views.emp_data_json_view,name='emp_data_json_view'),
    path('empjson2',views.emp_data_json_view2,name='emp_data_json_view2'),
    # class based view define
    path('apijsoncbv',views.JsonCBV.as_view()),
    path('apijsoncbvmixin',views.JsonCBVMixin.as_view())

]
