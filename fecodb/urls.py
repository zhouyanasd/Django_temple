from django.conf.urls import  url, include

urlpatterns = [
    url(r'^prop_material/',include('fecodb.urlsetting.prop_material_urls')),
    url(r'^location/', include('fecodb.urlsetting.location_urls')),
    url(r'^material/', include('fecodb.urlsetting.material_urls')),
    url(r'^property/', include('fecodb.urlsetting.propname_urls')),
    url(r'^pre_treat/', include('fecodb.urlsetting.pre_treat_urls')),
    url(r'^analysis_method/', include('fecodb.urlsetting.analysis_method_urls')),
    url(r'^nmr/', include('fecodb.urlsetting.nmr_urls')),
    url(r'^location_material/', include('fecodb.urlsetting.location_material_urls')),
    url(r'^prop_pre/',include('fecodb.urlsetting.prop_pre_urls')),
    url(r'^pre_proc/', include('fecodb.urlsetting.pre_proc_urls')),
    url(r'^analysis_proc/', include('fecodb.urlsetting.analysis_proc_urls')),
    url(r'^nmr_rlt/', include('fecodb.urlsetting.nmr_rlt_urls')),
    url(r'^pro_analysis/', include('fecodb.urlsetting.pro_analysis_urls')),
    url(r'^pre_analysis/', include('fecodb.urlsetting.pre_analysis_urls')),
    url(r'^prediction/', include('fecodb.urlsetting.prediction_urls'))
]