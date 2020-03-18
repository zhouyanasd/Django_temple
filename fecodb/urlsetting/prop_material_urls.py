from django.conf.urls import  url
from fecodb.views import prop_material_views

urlpatterns = [
    url(r'^list/$',prop_material_views.NmrMaterialPropList.as_view(),name= 'prop_material_list_all'),
    url(r'^detail/$',prop_material_views.NmrMaterialPropDetail.as_view(),name= 'prop_material_detail_all'),
    url(r'^add/$',prop_material_views.NmrMaterialPropAdd.as_view(),name= 'prop_material_add'),
    url(r'^update/$',prop_material_views.NmrMaterialPropUpdate.as_view(),name='prop_material_update' ),
    url(r'^delete/$',prop_material_views.NmrMaterialPropDelete.as_view(),name='prop_material_delete' ),
    ]