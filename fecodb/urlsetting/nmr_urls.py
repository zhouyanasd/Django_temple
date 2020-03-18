from django.conf.urls import url
from fecodb.views import nmr_views

urlpatterns = [
        url(r'^list/$',nmr_views.NmrList.as_view(), name= 'nmr_list_all'),
        url(r'^detail/$', nmr_views.NmrDetail.as_view(), name='nmr_detail_all'),
        url(r'^add/$',nmr_views.NmrAdd.as_view(), name='nmr_add'),
        url(r'^update/$', nmr_views.NmrUpdate.as_view(), name='nmr_update'),
        url(r'^delete/$', nmr_views.NmrDelete.as_view(), name='nmr_delete'),
        ]