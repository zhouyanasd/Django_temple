from django.http import Http404
from rest_framework.views import APIView
from fecodb import models
from django.http import JsonResponse as JsonResponses
from fecodb.utils.json import JsonResponse
from fecodb.utils.request import APIRequest
import json


class Calculate(APIView):
    def __init__(self):
        super(Calculate, self).__init__()
        self.path_list = [
            {
                "prop_id" : 1,
                "path" : "/data/car.csv"
            },
            {
                "prop_id": 7,
                "path":"/data/carr.csv"
            },
            {
                "prop_id": 3,
                "path": "/data/api.csv"
            },
            {
                "prop_id": 5,
                "path": "/data/gry500_540.csv"
            },
            {
                "prop_id": 4,
                "path": "/data/hyd.csv"
            },
            {
                "prop_id": 14,
                "path": "/data/diesel.csv"
            },
        ]

    def get_object_prop_pre(self,  pre_proc_id):
        try:
            return models.PropPreMethod.objects.filter(pre_process__id=pre_proc_id)
        except models.PropPreMethod.DoesNotExist:
             raise Http404

    def get_object_prop_ana(self,  analysis_proc_id):
        try:
            return models.PropAnalysisMethod.objects.filter(ana_process__id=analysis_proc_id)
        except models.PropAnalysisMethod.DoesNotExist:
             raise Http404

    def get_object_nmr(self,  nmr_id):
        try:
            return models.Nmr.objects.get(id=nmr_id)
        except models.Nmr.DoesNotExist:
            raise Http404

    def post(self, request):
        material_id = request.data.get('material_id')
        property_id = request.data.get('property_id')
        nmr_id = request.data.get('nmr_id')
        pre_proc_id = request.data.get('pre_proc_id')
        analysis_proc_id = request.data.get('analysis_proc_id')
        Nmr = self.get_object_nmr(nmr_id)
        PropAnalysisProcess = self.get_object_prop_ana(analysis_proc_id)
        PropPreProcess = self.get_object_prop_pre(pre_proc_id)

        property_train_data_path = None
        for path in self.path_list:
            if path['prop_id'] == int(property_id):
                property_train_data_path = path['path']
        data = Nmr.value

        response={}
        for PropPreMethod in PropPreProcess:
            pre_url = PropPreMethod.pre_treat.url
            conf = PropPreMethod.pre_treat.def_conf_para
            prams={
                'data':data,
                'conf':conf,
                'property_train_data_path' : property_train_data_path
            }
            response = APIRequest(url= pre_url,parms=prams,type='POST').request()


        PropAnalysisMethod = models.PropAnalysisMethod.objects.get(id=1)
        ana_url = PropAnalysisMethod.ana_treat.url
        conf_p = PropAnalysisMethod.ana_treat.def_conf_para
        conf_s = PropAnalysisMethod.ana_treat.def_conf_stru
        prams = {
            'data': json.dumps(response),
            'conf_p': conf_p,
            'conf_s': conf_s
        }
        result = APIRequest(url=ana_url, parms=prams, type='POST').request()

        response = {
            'result': result,
            'material_id': material_id,
            'property_id': property_id
        }

        return JsonResponse(data=response, code=0, msg='Success')


