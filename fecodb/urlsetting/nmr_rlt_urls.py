from django.conf.urls import  url
from fecodb.views import nmr_rlt_views

urlpatterns = [
    url(r'^list/$', nmr_rlt_views.AnalysisPropsList.as_view(), name='analysis_props_list_all'),
    url(r'^detail/$',nmr_rlt_views.AnalysisPropsDetail.as_view(),name= 'analysis_props_detail_all'),
    url(r'^add/$',nmr_rlt_views.AnalysisPropsAdd.as_view(),name= 'analysis_props_add'),
    url(r'^update/$',nmr_rlt_views.AnalysisPropsUpdate.as_view(),name= 'analysis_props_update'),
    url(r'^delete/$',nmr_rlt_views.AnalysisPropsDelete.as_view(),name= 'analysis_props_delete'),
]