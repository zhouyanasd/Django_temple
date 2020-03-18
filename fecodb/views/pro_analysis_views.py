from django.http import Http404
from rest_framework.views import APIView

from fecodb import models
from fecodb.serilizers import pro_analysis_serializers
from fecodb.utils.json import JsonResponse


class PropAnalysisMethodList(APIView):
    def get_object(self, request):
        analysis_method_id = request.GET.get('analysis_method_id')
        property_id = request.GET.get('property_id')
        material_id = request.GET.get('material_id')
        status = request.GET.get('status')
        kwargs = {}
        if analysis_method_id != None:
            kwargs['ana_treat'] = analysis_method_id
        if property_id != None:
            kwargs['prop_material__property'] = property_id
        if material_id != None:
            kwargs['prop_material__material'] = material_id
        if status != None:
            kwargs['ana_process__state'] = status
        try:
            Queryset = models.PropAnalysisMethod.objects.filter(**kwargs)
            return Queryset
        except models.PropAnalysisMethod.DoesNotExist:
            raise Http404

    def get(self, request):
        PropAnalysisMethod = self.get_object(request)
        serializer = pro_analysis_serializers.PropAnalysisMethodSerializers(PropAnalysisMethod, many=True)
        return JsonResponse(data=serializer.data, code=0, msg='get PropPreMethodList success')


class PropAnalysisMethodDetail(APIView):
    def get_object(self, request):
        pro_analysis_id = request.GET.get('pro_analysis_id')
        kwargs = {}
        if pro_analysis_id != None:
            kwargs['id'] = pro_analysis_id
        try:
            Queryset = models.PropAnalysisMethod.objects.get(**kwargs)
            return Queryset
        except models.PropAnalysisMethod.DoesNotExist:
            raise Http404

    def get(self, request):
        PropAnalysisMethod = self.get_object(request)
        serializer = pro_analysis_serializers.PropAnalysisMethodSerializers(PropAnalysisMethod)
        return JsonResponse(data=serializer.data, code=0, msg='get PropPreMethodDetail success')


class PropAnalysisMethodAdd(APIView):
    def get_prop_material_id(self,request):
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        try:
            prop_material = models.NmrMaterialProp.objects.get(property=property_id, material= material_id)
            return prop_material.id
        except models.AnalysisProps.DoesNotExist:
             raise Http404

    def post(self,request):
        name = request.data.get('name')
        desc = request.data.get('desc')
        params = request.data.get('params')
        analysis_method_id = request.data.get('analysis_method_id')
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        priority = request.data.get('priority')
        analysis_process_id = request.data.get('analysis_process_id')
        if analysis_method_id !=None and property_id != None and material_id != None and priority != None:
            prop_material = self.get_prop_material_id(request)
            data = {
                'name': name,
                'desc': desc,
                'prop_material': prop_material,
                'params': params,
                'analysis_method_id': analysis_method_id,
                'priority': priority,
                'analysis_process_id': analysis_process_id
            }
            serializer = pro_analysis_serializers.PropAnalysisMethodSerializersAdd(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='add PropAnalysisMethodAdd success')
            return JsonResponse(data=[], code=1, msg='False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class PropAnalysisMethodUpdate(APIView):
    def get_prop_material_id(self,request):
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        try:
            prop_material = models.NmrMaterialProp.objects.get(property=property_id, material= material_id)
            return prop_material.id
        except models.AnalysisProps.DoesNotExist:
             raise Http404

    def get_object(self, request, prop_analysis_id):
        try:
            return models.PropAnalysisMethod.objects.get(id=prop_analysis_id)
        except models.PropAnalysisMethod.DoesNotExist:
            raise Http404

    def post(self, request):
        prop_analysis_id = request.data.get('prop_analysis_id')
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')

        if prop_analysis_id != None:
            PropAnalysisMethod = self.get_object(request, prop_analysis_id)
            if property_id !=None and material_id != None:
                prop_material = self.get_prop_material_id(request)
            else:
                prop_material = PropAnalysisMethod.prop_material.id
            data = request.data.copy()
            print(data)
            data.update({'prop_material':prop_material})
            serializer = pro_analysis_serializers.PropAnalysisMethodSerializersUpdate(PropAnalysisMethod, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='update PropAnalysisMethod success')
            return JsonResponse(data=[], code=1, msg='data valid False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class PropAnalysisMethodDelete(APIView):
    def get_object(self, request, prop_analysis_id):
        try:
            return models.PropAnalysisMethod.objects.get(id=prop_analysis_id)
        except models.PropAnalysisMethod.DoesNotExist:
            raise Http404

    def get(self, request):
        prop_analysis_id= request.GET.get('prop_analysis_id')
        if prop_analysis_id != None:
            PropAnalysisMethod = self.get_object(request, prop_analysis_id)
            PropAnalysisMethod.delete()
            return JsonResponse(data=[], code=0, msg='get PropAnalysisMethod success')
        else:
            return JsonResponse(data=[], code= 1, msg='False')