from django.conf.urls import  url
from fecodb.views.algorithm_views import analysis_views

urlpatterns = [
        url(r'^rwnn/$',analysis_views.AnalysisRWNN.as_view(),name= 'algorithm_analysis_RWNN'),
        ]