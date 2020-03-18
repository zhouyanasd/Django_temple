from django.conf.urls import url
from fecodb.views import prop_pre_views

urlpatterns = [
        url(r'^list/$',prop_pre_views.PropPreMethodList.as_view(), name= 'prop_pre_list_all'),
        url(r'^detail/$', prop_pre_views.PropPreMethodDetail.as_view(), name='prop_pre_detail_all'),
        url(r'^add/$',prop_pre_views.PropPreMethodAdd.as_view(), name='prop_pre_add'),
        url(r'^update/$', prop_pre_views.PropPreMethodUpdate.as_view(), name='prop_pre_update'),
        url(r'^delete/$', prop_pre_views.PropPreMethodDelete.as_view(), name='prop_pre_delete'),
        ]