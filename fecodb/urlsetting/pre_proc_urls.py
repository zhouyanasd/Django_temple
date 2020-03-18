from django.conf.urls import  url
from fecodb.views import pre_proc_views

urlpatterns = [
    url(r'^list/$',pre_proc_views.PropPreProcessList.as_view(), name= 'pre_proc_list_all'),
    url(r'^detail/$',pre_proc_views.PropPreProcessDetail.as_view(),name= 'pre_proc_detail_all'),
    url(r'^add/$',pre_proc_views.PropPreProcessAdd.as_view(),name= 'pre_proc_add'),
    url(r'^addlist/$',pre_proc_views.PropPreProcessAddPreList.as_view(),name= 'pre_proc_addlist'),
    url(r'^update/$',pre_proc_views.PropPreProcessUpdate.as_view(),name= 'pre_proc_update'),
    url(r'^updatelist/$',pre_proc_views.PropPreProcessUpdatePreList.as_view(),name= 'pre_proc_update'),
    url(r'^delete/$',pre_proc_views.PropPreProcessDelete.as_view(),name= 'pre_proc_delete'),
    ]