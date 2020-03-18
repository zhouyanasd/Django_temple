from django.conf.urls import  url
from fecodb.views import analysis_method_views

urlpatterns = [
        url(r'^list/$',analysis_method_views.AnalysisMethodList.as_view(),name= 'analysis_method_list_all'),
        url(r'^detail/$',analysis_method_views.AnalysisMethodDetail.as_view(),name= 'analysis_method_detail_all'),
        url(r'^add/$',analysis_method_views.AnalysisMethodAdd.as_view(),name= 'analysis_method_add_all'),
        url(r'^update/$',analysis_method_views.AnalysisMethodUpdate.as_view(),name= 'analysis_method_update_all'),
        url(r'^delete/$',analysis_method_views.AnalysisMethodDelete.as_view(),name= 'analysis_method_delete_all'),
        ]