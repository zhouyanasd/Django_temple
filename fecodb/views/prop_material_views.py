from django.http import Http404
from rest_framework.views import APIView
from django.db.models import Q

from fecodb import models
from fecodb.serilizers import prop_material_serializers
from fecodb.utils.json import JsonResponse


class  NmrMaterialPropList(APIView):
    def get_object(self,request):
        di = {}
        if request.GET.get('status') != None:
            di['state']=request.GET.get('status')
        if request.GET.get('material_id') != None:
            di['material'] = request.GET.get('material_id')
        if request.GET.get('property_id') != None:
            di['property'] = request.GET.get('property_id')
        q = Q()
        for i in di:
            q.add(Q(**{i: di[i]}), Q.AND)
        try:
            NmrMaterialProp = models.NmrMaterialProp.objects.filter(q)
            return NmrMaterialProp
        except models.NmrMaterialProp.DoesNotExist:
            raise Http404

    def get(self, request):
        PropName = self.get_object(request)
        serializer = prop_material_serializers.NmrMaterialPropSerializers(PropName, many=True)
        return JsonResponse(data=serializer.data, code=0, msg='get NmrMaterialPropList success')


class NmrMaterialPropDetail(APIView):
    def get_object(self, request, property_material_id):
        try:
            return models.NmrMaterialProp.objects.get(id=property_material_id)
        except models.NmrMaterialProp.DoesNotExist:
            raise Http404

    def get(self, request):
        property_id = request.GET.get('property_material_id')
        if property_id != None:
            NmrMaterialProp = self.get_object(request, property_id)
            serializer = prop_material_serializers.NmrMaterialPropSerializers(NmrMaterialProp)
            return JsonResponse(data=serializer.data, code=0, msg='get NmrMaterialPropDetail success')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class NmrMaterialPropAdd(APIView):
    def post(self, request):
        material_id = request.data.get('material_id')
        property_id = request.data.get('property_id')
        status = request.data.get('status')
        process_id = request.data.get('process_id')
        if material_id != None and property_id != None:
            try:
                NmrMaterialProp = models.NmrMaterialProp.objects.get(material=material_id, property= property_id)
                serializer = prop_material_serializers.NmrMaterialPropSerializersAdd(NmrMaterialProp)
                return JsonResponse(data=serializer.data, code=0, msg='NmrMaterialProp already exist')
            except models.NmrMaterialProp.DoesNotExist:
                data = {
                    'material_id': material_id,
                    'property_id': property_id,
                    'status' : status,
                    'process_id' : process_id,
                }
                serializer = prop_material_serializers.NmrMaterialPropSerializersAdd(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(data=serializer.data, code=0, msg='Add NmrMaterialProp success')
                return JsonResponse(data=[], code=1, msg='False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class NmrMaterialPropUpdate(APIView):
    def get_object(self, request, property_material_id):
        try:
            return models.NmrMaterialProp.objects.get(id=property_material_id)
        except models.NmrMaterialProp.DoesNotExist:
            raise Http404

    def post(self, request):
        property_material_id = request.data.get('property_material_id')
        material_id = request.data.get('material_id')
        property_id = request.data.get('property_id')
        status = request.data.get('status')
        process_id = request.data.get('process_id')
        if property_material_id != None:
            PropName = self.get_object(request, property_material_id)
            data = {
                'material_id': material_id,
                'property_id': property_id,
                'status': status,
                'process_id': process_id,
            }
            serializer = prop_material_serializers.NmrMaterialPropSerializersUpdate(PropName, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='update PropName success')
            return JsonResponse(data=[], code=1, msg='False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class NmrMaterialPropDelete(APIView):
    def get_object(self, request, property_material_id):
        try:
            return models.PropName.objects.get(id=property_material_id)
        except models.PropName.DoesNotExist:
            raise Http404

    def post(self, request):
        property_material_id = request.data.get('property_material_id')
        if property_material_id != None:
            NmrMaterialProp = self.get_object(request, property_material_id)
            NmrMaterialProp.delete()
            return JsonResponse(data=[], code=0, msg='Delete Success')
        else:
            return JsonResponse(data=[], code=1, msg='False')