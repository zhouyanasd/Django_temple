from django.conf.urls import  url
from fecodb.views import propname_views

urlpatterns = [
    url(r'^list/$',propname_views.PropNameList.as_view(),name= 'PropName_list_all'),
    url(r'^detail/$',propname_views.PropNameDetail.as_view(),name= 'PropName_detail_all'),
    url(r'^add/$',propname_views.PropNameAdd.as_view(),name= 'PropName_add'),
    url(r'^update/$',propname_views.PropNameUpdate.as_view(),name='PropName_update' ),
    url(r'^delete/$',propname_views.PropNameDelete.as_view(),name='PropName_delete' ),
    ]