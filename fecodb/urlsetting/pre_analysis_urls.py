from django.conf.urls import url
from fecodb.views import pre_analysis_views

urlpatterns = [
    url(r'^list/$',pre_analysis_views.PreAnalysisProcessList.as_view(), name='pre_analysis_list_all'),
    url(r'^add/$',pre_analysis_views.PreAnalysisProcessAdd.as_view(), name='pre_analysis_add'),
    url(r'^update/$',pre_analysis_views.PreAnalysisProcessUpdate.as_view(), name='pre_analysis_update'),
    url(r'^delete/$',pre_analysis_views.PreAnalysisProcessDelete.as_view(), name='pre_analysis_delete'),
]