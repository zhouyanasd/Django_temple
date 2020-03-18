from django.conf.urls import  url
from fecodb.views.algorithm_views import pretreatment_views

urlpatterns = [
        url(r'^snv/$',pretreatment_views.PretreatmentSNV.as_view(),name= 'algorithm_pretreatment_SNV'),
        url(r'^diff1/$',pretreatment_views.PretreatmentDIFF1.as_view(),name= 'algorithm_pretreatment_DIFF1'),
        url(r'^diff2/$',pretreatment_views.PretreatmentDIFF2.as_view(),name= 'algorithm_pretreatment_DIFF2'),
        url(r'^fake/$',pretreatment_views.PretreatmentFAKE.as_view(),name= 'algorithm_pretreatment_FAKE'),
        ]