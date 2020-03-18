from django.http import Http404
from rest_framework.views import APIView
import json

from fecodb import models
from fecodb.serilizers import analysis_proc_serializers
from fecodb.serilizers import pro_analysis_serializers
from fecodb.utils.json import JsonResponse

class PropAnalysisProcessList(APIView):
    def get_object(self,request):
        property_id = request.GET.get('property_id')
        material_id = request.GET.get('material_id')
        status = request.GET.get('status')
        kwargs = {}
        if status != None:
            kwargs['state'] = status
        if property_id != None:
            kwargs['property_material__prop_material__property'] = property_id
        if material_id != None:
            kwargs['property_material__prop_material__material'] = material_id
        try:
            Queryset = models.PropAnalysisProcess.objects.filter(**kwargs)
            return Queryset
        except models.PropAnalysisProcess.DoesNotExist:
            raise Http404

    def get(self, request):
        PropAnalysisProcess = self.get_object(request)
        serializer = analysis_proc_serializers.PropAnalysisProcessSerializers(PropAnalysisProcess, many=True)
        return JsonResponse(data=serializer.data, code=0, msg='get PropAnalysisProcessList success')


class PropAnalysisProcessDetail(APIView):
    def get_object(self, request, analysis_proc_id):
        try:
            return models.PropAnalysisProcess.objects.get(id=analysis_proc_id)
        except models.PropAnalysisProcess.DoesNotExist:
             raise Http404

    def get(self, request):
        analysis_proc_id = request.GET.get('analysis_proc_id')
        if analysis_proc_id != None:
            PropAnalysisProcess = self.get_object(request, analysis_proc_id)
            serializer = analysis_proc_serializers.PropAnalysisProcessSerializers(PropAnalysisProcess)
            return JsonResponse(data=serializer.data, code= 0, msg='get PropAnalysisProcessDetail success')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class PropAnalysisProcessAdd(APIView):
    def post(self, request):
        data = request.data.copy()
        serializer = analysis_proc_serializers.PropAnalysisProcessSerializersAdd(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, code=0, msg='add PropAnalysisProcess success')
        return JsonResponse(data=[], code=1, msg='data valid False')


class PropAnalysisProcessAddAnalysisList(APIView):
    def get_object(self, request, analysis_proc_id):
        try:
            return models.PropAnalysisProcess.objects.get(id=analysis_proc_id)
        except models.PropPreProcess.DoesNotExist:
             raise Http404

    def get_prop_material_id(self,request):
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        try:
            prop_material = models.NmrMaterialProp.objects.get(property=property_id, material=material_id)
            return prop_material.id
        except models.NmrMaterialProp.DoesNotExist:
             raise Http404

    def post(self, request):
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        if property_id!=None and material_id!=None:
            prop_material = self.get_prop_material_id(request)
            data = request.data.copy()
            prop_analysis_list = json.loads(data.get('prop_analysis_list'))
            serializer = analysis_proc_serializers.PropAnalysisProcessSerializersAdd(data=data)
            if serializer.is_valid():
                serializer.save()
                #----save methods--------------
                for prop_analysis in prop_analysis_list:
                    prop_analysis['prop_material'] = prop_material
                    prop_analysis['analysis_process_id'] = serializer.data['id']
                    serializer_method=pro_analysis_serializers.PropAnalysisMethodSerializersAdd(data=prop_analysis)
                    if serializer_method.is_valid():
                        serializer_method.save()
                    else:
                        return JsonResponse(data=[], code=1, msg='prop_analysis_list valid False')
                #---------------------------------
                PropAnalysisProcess = self.get_object(request, serializer.data['id'])
                serializer = analysis_proc_serializers.PropAnalysisProcessSerializers(PropAnalysisProcess)
                return JsonResponse(data=serializer.data, code=0, msg='add PropAnalysisProcess success')
            else:
                return JsonResponse(data=[], code=1, msg='data valid False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class PropAnalysisProcessUpdate(APIView):
    def get_object(self, request, analysis_proc_id):
        try:
            return models.PropAnalysisProcess.objects.get(id=analysis_proc_id)
        except models.PropAnalysisProcess.DoesNotExist:
             raise Http404

    def post(self, request):
        analysis_proc_id = request.data.get('analysis_proc_id')
        if analysis_proc_id != None:
            PropAnalysisProcess = self.get_object(request, analysis_proc_id)
            data = request.data.copy()
            serializer = analysis_proc_serializers.PropAnalysisProcessSerializersUpdate(PropAnalysisProcess, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='update PropAnalysisProcess success')
            return JsonResponse(data=[], code=1, msg='data valid False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class PropAnalysisProcessUpdateAnalysisList(APIView):
    def get_object(self, request, analysis_proc_id):
        try:
            return models.PropAnalysisMethod.objects.get(id=analysis_proc_id)
        except models.PropAnalysisMethod.DoesNotExist:
             raise Http404

    def get_object_method(self, request, prop_analysis_id):
        try:
            return models.PropAnalysisMethod.objects.get(id=prop_analysis_id)
        except models.PropAnalysisMethod.DoesNotExist:
            raise Http404

    def get_prop_material_id(self,request):
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        try:
            prop_material = models.NmrMaterialProp.objects.get(property=property_id, material= material_id)
            return prop_material.id
        except models.NmrMaterialProp.DoesNotExist:
             raise Http404

    def post(self, request):
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        analysis_proc_id = request.data.get('analysis_proc_id')
        if analysis_proc_id != None:
            PropAnalysisProcess = self.get_object(request, analysis_proc_id)
            data = request.data.copy()
            prop_analysis_list = json.loads(data.get('prop_analysis_list'))
            serializer = analysis_proc_serializers.PropAnalysisProcessSerializersUpdate(PropAnalysisProcess, data=data)
            if serializer.is_valid():
                serializer.save()
                #----updata methods--------------
                for prop_analysis in prop_analysis_list:
                    prop_analysis_id = prop_analysis['prop_analysis_id']
                    if prop_analysis_id != None:
                        PropAnalysisMethod = self.get_object(request, prop_analysis_id)
                        if property_id != None and material_id != None:
                            prop_material = self.get_prop_material_id(request)
                        else:
                            prop_material = PropAnalysisMethod.prop_material.id
                        prop_analysis['prop_material'] = prop_material
                        serializer = pro_analysis_serializers.PropAnalysisMethodSerializersUpdate(PropAnalysisMethod,
                                                                                                  data=prop_analysis)
                        if serializer.is_valid():
                            serializer.save()
                        else:
                            return JsonResponse(data=[], code=1, msg='data valid False')
                #---------------------------------
                return JsonResponse(data=serializer.data, code=0, msg='update PropAnalysisProcess success')
            return JsonResponse(data=[], code=1, msg='data valid False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class PropAnalysisProcessDelete(APIView):
    def get_object(self, request, analysis_proc_id):
        try:
            return models.PropAnalysisProcess.objects.get(id=analysis_proc_id)
        except models.PropAnalysisProcess.DoesNotExist:
             raise Http404

    def post(self, request):
        analysis_proc_id = request.data.get('analysis_proc_id')
        if analysis_proc_id != None:
            PropAnalysisProcess = self.get_object(request, analysis_proc_id)
            PropAnalysisProcess.delete()
            return JsonResponse(data=[], code= 0, msg='delete PropAnalysisProcess success')
        else:
            return JsonResponse(data=[], code=1, msg='False')