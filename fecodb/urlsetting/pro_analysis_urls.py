from django.conf.urls import url
from fecodb.views import pro_analysis_views

urlpatterns = [
    url(r'^list/$',pro_analysis_views.PropAnalysisMethodList.as_view(), name= 'pro_analysis_list_all'),
    url(r'^detail/$',pro_analysis_views.PropAnalysisMethodDetail.as_view(), name= 'pro_analysis_detail_all'),
    url(r'^add/$',pro_analysis_views.PropAnalysisMethodAdd.as_view(), name= 'pro_analysis_add_all'),
    url(r'^update/$',pro_analysis_views.PropAnalysisMethodUpdate.as_view(), name= 'pro_analysis_update_all'),
    url(r'^delete/$',pro_analysis_views.PropAnalysisMethodDelete.as_view(), name= 'pro_analysis_delete_all')
]