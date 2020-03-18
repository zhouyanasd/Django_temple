from django.http import Http404
from rest_framework.views import APIView

from fecodb import models
from fecodb.serilizers import pre_analysis_serializers
from fecodb.utils.json import JsonResponse


class PreAnalysisProcessList(APIView):
    def get_object(self, request):
        property_id = request.GET.get('property_id')
        material_id = request.GET.get('material_id')
        status = request.GET.get('status')
        id_list = request.GET.get('id_list')
        if id_list != None:
            id_list = [int(x) for x in id_list if x != ',' and x != '[' and x != ']']
        print(id_list)
        kwargs = {}
        if property_id != None:
            kwargs['p_pre_pro__property_material__prop_material__property'] = property_id
        if material_id != None:
            kwargs['p_pre_pro__property_material__prop_material__material'] = material_id
        if status != None:
            kwargs['state'] = status
        if id_list != None:
            kwargs['id__in'] = id_list
        try:
            Queryset = models.PreAnalysisProcess.objects.filter(**kwargs).distinct().values('id', 'name','owner_id',
                                                                                            'p_pre_pro__property_material__prop_material__material',
                                                                                            'description', 'state',
                                                                                            'edit_time', 'add_time',
                                                                                            'p_ana_pro', 'p_pre_pro',
                                                                                            'p_pre_pro__property_material__prop_material__property')
            print(Queryset)
            return Queryset
        except models.PreAnalysisProcess.DoesNotExist:
            raise Http404

    def get(self, request):
        PreAnalysisProcess = self.get_object(request)
        serializer = pre_analysis_serializers.PreAnalysisProcessHandSerializers(PreAnalysisProcess, many=True)
        return JsonResponse(data=serializer.data, code=0, msg='get PreAnalysisProcessList success')


class PreAnalysisProcessAdd(APIView):
    def get_prop_material_id(self,request):
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        try:
            prop_material= models.NmrMaterialProp.objects.get(property=property_id, material= material_id)
            return prop_material.id
        except models.NmrMaterialProp.DoesNotExist:
             raise Http404

    def post(self,request):
        if request.data.get('property_id') != None and request.data.get('material_id') != None:
            prop_material = self.get_prop_material_id(request)
            data = request.data.copy()
            data.update({'prop_material': prop_material})
            serializer = pre_analysis_serializers.PreAnalysisProcessHandSerializersAdd(data=data)
            if serializer.is_valid():
                serializer.save()
                data_s = dict(serializer.data)
                data_s['material_id'] = int(data['material_id'])
                data_s['property_id'] = int(data['property_id'])
                return JsonResponse(data=data_s, code=0, msg='add PreAnalysisProcess success')
            return JsonResponse(data=[], code=1, msg='data valid False')
        else:
            return JsonResponse(data=[], code=1, msg='False')

class PreAnalysisProcessUpdate(APIView):
    def get_prop_material_id(self,request):
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        try:
            prop_material= models.NmrMaterialProp.objects.get(property=property_id, material= material_id)
            return prop_material.id
        except models.NmrMaterialProp.DoesNotExist:
             raise Http404

    def get_object(self,pre_analysis_id):
        try:
            return models.PreAnalysisProcess.objects.get(id=pre_analysis_id)
        except models.PreAnalysisProcess.DoesNotExist:
            raise Http404

    def post(self,request):
        pre_analysis_id = request.data.get('pre_analysis_id')
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        if pre_analysis_id != None:
            PreAnalysisProcess = self.get_object(pre_analysis_id)
            if property_id !=None and material_id != None:
                prop_material = self.get_prop_material_id(request)
            else:
                prop_material = PreAnalysisProcess.prop_material.id
            data = request.data.copy()
            data.update({'prop_material':prop_material})
            serializer = pre_analysis_serializers.PreAnalysisProcessHandSerializersUpdate(PreAnalysisProcess, data=data)
            if serializer.is_valid():
                serializer.save()
                data_s = dict(serializer.data)
                data_s['material_id'] = int(material_id)
                data_s['property_id'] = int(property_id)
                return JsonResponse(data=data_s, code=0, msg='add PreAnalysisProcess success')
            return JsonResponse(data=[], code=1, msg='data valid False')
        else:
            return JsonResponse(data=[], code=1, msg='False')



class PreAnalysisProcessDelete(APIView):
    def get_object(self,request, pre_analysis_id):
        try:
            return models.PreAnalysisProcess.objects.get(id=pre_analysis_id)
        except models.PreAnalysisProcess.DoesNotExist:
            raise Http404

    def get(self, request):
        pre_analysis_id= request.GET.get('pre_analysis_id')
        if pre_analysis_id != None:
            PreAnalysisProcess = self.get_object(request, pre_analysis_id)
            PreAnalysisProcess.delete()
            return JsonResponse(data=[], code=0, msg='get PreAnalysisProcess success')
        else:
            return JsonResponse(data=[], code= 1, msg='False')
