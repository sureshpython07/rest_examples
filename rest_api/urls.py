from django.urls import path,include
from rest_api.views import student_list_fbv,student_detail_fbv,stud_list_fbv_api_view,stud_detail_fbv_api_view,Std__List_CBV,Std_detail_CBV,Std_mixin_gen_CBV_list,Std_mixin_gen_CBV_detail,Std_gen_list,Std_gen_detail
from rest_api.views import StudentViewSet_list,StudentViewSet_detail,Std_Generic_ViewSet
from rest_framework import routers

#viewset and routers
router=routers.SimpleRouter()
router.register('api_viewset_list',StudentViewSet_list,basename='studentlist')
router.register('api_viewset_detail/{pk}',StudentViewSet_detail,basename='studentdetail')
#generic viewsets urls
router.register('api_generic_viewset',Std_Generic_ViewSet)

urlpatterns = [
    path("api",student_list_fbv,name='student_list_fbv'),
    path("api_detail/<id>",student_detail_fbv,name='student_detail_fbv'),
    # api_view related urls
    path("api_view_list",stud_list_fbv_api_view,name='post_list_fbv_api_view'),
    path("api_view_detail/<int:pk>",stud_detail_fbv_api_view,name='stud_detail_fbv_api_view'),
    # class based view urls
    path("api_view_list_cbv",Std__List_CBV.as_view()),
    path("api_view_detail_cbv/<int:id>",Std_detail_CBV.as_view()),
    # mixin and generic and authenticated api views urls
    path("api_view_list_mix_gen_cbv",Std_mixin_gen_CBV_list.as_view()),
    path("api_view_detail_mix_gen_cbv/<int:pk>",Std_mixin_gen_CBV_detail.as_view()),
    #only generics urls
    path('api_gen_list',Std_gen_list.as_view()),
    path('api_gen_detail/<int:pk>',Std_gen_detail.as_view()),
    #viewset urls
    path('',include(router.urls))
]
#urlpatterns +=router.urls
