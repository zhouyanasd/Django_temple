from django.conf.urls import  url
from fecodb.views import material_views

urlpatterns = [
        url(r'^list/$',material_views.NmrMaterialList.as_view(),name= 'nmrmaterial_list_all'),
        url(r'^detail/$',material_views.NmrMaterialDetail.as_view(),name= 'nmrmaterial_detail_all'),
        url(r'^add/$', material_views.NmrMaterialAdd.as_view(), name='nmrmaterial_add'),
        url(r'^update/$', material_views.NmrMaterialUpdate.as_view(), name='nmrmaterial_update'),
        url(r'^delete/$', material_views.NmrMaterialDelete.as_view(), name='nmrmaterial_delete'),
        ]