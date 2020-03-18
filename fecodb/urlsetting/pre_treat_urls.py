from django.conf.urls import  url
from fecodb.views import pre_treat_views

urlpatterns = [
        url(r'^list/$',pre_treat_views.PreTreatmentMethodList.as_view(),name= 'pre_treat_list_all'),
        url(r'^detail/$',pre_treat_views.PreTreatmentMethodDetail.as_view(),name= 'pre_treat_detail_all'),
        url(r'^add/$',pre_treat_views.PreTreatmentMethodAdd.as_view(),name= 'pre_treat_add_all'),
        url(r'^update/$',pre_treat_views.PreTreatmentMethodUpdate.as_view(),name= 'pre_treat_update_all'),
        url(r'^delete/$',pre_treat_views.PreTreatmentMethodDelete.as_view(),name= 'pre_treat_delete_all')
        ]