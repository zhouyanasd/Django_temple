from django.conf.urls import  url
from fecodb.views import location_views

urlpatterns = [
    url(r'^list/$',location_views.NmrLocationList.as_view(),name= 'nmrlocation_list_all'),
    url(r'^detail/$',location_views.NmrLocationDetail.as_view(),name= 'nmrlocation_detail'),
    url(r'^add/$',location_views.NmrLocationAdd.as_view(),name= 'nmrlocation_add'),
    url(r'^update/$',location_views.NmrLocationUpdate.as_view(),name='nmrlocation_update' ),
    url(r'^delete/$',location_views.NmrLocationDelete.as_view(),name='nmrlocation_delete' ),
]