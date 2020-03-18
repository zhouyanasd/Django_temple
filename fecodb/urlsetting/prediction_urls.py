from django.conf.urls import  url,include
from fecodb.views import calculate_views

urlpatterns = [
        url(r'^calculate/$',calculate_views.Calculate.as_view(),name= 'property_result_calculate'),
        url(r'^algorithm_analysis/', include('fecodb.urlsetting.algorithm_urls.analysis_urls')),
        url(r'^algorithm_pretreatment/', include('fecodb.urlsetting.algorithm_urls.pretreatment_urls')),
        ]