from django.conf.urls import  url
from fecodb.views import analysis_proc_views

urlpatterns = [
    url(r'^list/$',analysis_proc_views.PropAnalysisProcessList.as_view(),name= 'analysis_proc_list_all'),
    url(r'^detail/$',analysis_proc_views.PropAnalysisProcessDetail.as_view(),name= 'analysis_proc_detail_all'),
    url(r'^add/$',analysis_proc_views.PropAnalysisProcessAdd.as_view(),name= 'analysis_proc_add'),
    url(r'^addlist/$',analysis_proc_views.PropAnalysisProcessAddAnalysisList.as_view(),name= 'analysis_proc_addlist'),
    url(r'^update/$',analysis_proc_views.PropAnalysisProcessUpdate.as_view(),name= 'analysis_proc_update'),
    url(r'^updatelist/$',analysis_proc_views.PropAnalysisProcessUpdateAnalysisList.as_view(),name= 'analysis_proc_updatelist'),
    url(r'^delete/$',analysis_proc_views.PropAnalysisProcessDelete.as_view(),name= 'analysis_proc_delete_all'),
    ]