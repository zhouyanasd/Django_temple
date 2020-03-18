from django.conf.urls import  url
from fecodb.views import location_material_views

urlpatterns = [
    url(r'^list/$',location_material_views.NmrLocationMaterialList.as_view(),name= 'location_material_list_all'),
    url(r'^detail/$',location_material_views.NmrLocationMaterialDetail.as_view(),name= 'location_material_detail_all'),
    url(r'^add/$',location_material_views.NmrLocationMaterialAdd.as_view(),name= 'location_material_add_all'),
    url(r'^update/$',location_material_views.NmrLocationMaterialUpdate.as_view(),name= 'location_material_update_all'),
    url(r'^delete/$',location_material_views.NmrLocationMaterialDelete.as_view(),name= 'location_material_delete_all'),
    ]