from django.http import Http404
from rest_framework.views import APIView
from django.db.models import Q

from fecodb import models
from fecodb.serilizers import location_material_serializers
from fecodb.utils.json import JsonResponse


class  NmrLocationMaterialList(APIView):
    def get_object(self,request):
        di = {}
        if request.GET.get('status') != None:
            di['state']=request.GET.get('status')
        if request.GET.get('location_id') != None:
            di['location'] = request.GET.get('location_id')
        if request.GET.get('material_id') != None:
            di['material'] = request.GET.get('material_id')
        q=Q()
        for i in di:
            q.add(Q(**{i: di[i]}), Q.AND)
        try:
            NmrLocationMaterial = models.NmrLocationMaterial.objects.filter(q)
            return NmrLocationMaterial
        except models.NmrLocationMaterial.DoesNotExist:
            raise Http404

    def get(self, request):
        NmrLocation = self.get_object(request)
        serializer = location_material_serializers.NmrLocationMaterialSerializers(NmrLocation, many=True)
        return JsonResponse(data=serializer.data, code=0, msg='get Location_MaterialList success')


class NmrLocationMaterialDetail(APIView):
    def get_object(self, request, location_material_id):
        try:
            return models.NmrLocationMaterial.objects.get(id=location_material_id)
        except models.NmrLocationMaterial.DoesNotExist:
            raise Http404

    def get(self, request):
        location_material_id = request.GET.get('location_material_id')
        if location_material_id != None:
            NmrLocationMaterial = self.get_object(request, location_material_id)
            serializer = location_material_serializers.NmrLocationMaterialSerializers(NmrLocationMaterial)
            return JsonResponse(data=serializer.data, code=0, msg='get NmrLocationMaterialDetail success')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class NmrLocationMaterialAdd(APIView):
    def post(self, request):
        location_id = request.data.get('location_id')
        material_id = request.data.get('material_id')
        status = request.data.get('status')
        if location_id != None and material_id != None:
            try:
                NmrLocationMaterial = models.NmrLocationMaterial.objects.get(location=location_id, material=material_id)
                serializer = location_material_serializers.NmrLocationMaterialSerializersAdd(NmrLocationMaterial)
                return JsonResponse(data=serializer.data, code=0, msg='NmrLocationMaterial already exist')
            except models.NmrLocationMaterial.DoesNotExist:
                data = {
                    'location_id': location_id,
                    'material_id': material_id,
                    'status': status,
                }
                serializer = location_material_serializers.NmrLocationMaterialSerializersAdd(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(data=serializer.data, code=0, msg='Add NmrLocationMaterial success')
                return JsonResponse(data=[], code=1, msg='False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class NmrLocationMaterialUpdate(APIView):
    def get_object(self, request, location_material_id):
        try:
            return models.NmrLocationMaterial.objects.get(id=location_material_id)
        except models.NmrLocationMaterial.DoesNotExist:
            raise Http404

    def post(self, request):
        location_material_id = request.data.get('location_material_id')
        location_id = request.data.get('location_id')
        material_id = request.data.get('material_id')
        status = request.data.get('status')
        if location_material_id != None:
            NmrLocationMaterial = self.get_object(request, location_material_id)
            data = {
                'location_id': location_id,
                'material_id': material_id,
                'status': status,
            }
            print(data)
            serializer = location_material_serializers.NmrLocationMaterialSerializersUpdate(NmrLocationMaterial, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='update NmrLocation success')
            return JsonResponse(data=[], code=1, msg='False')
        else:
            return JsonResponse(data=[], code=1, msg='False')

class NmrLocationMaterialDelete(APIView):
    def get_object(self, request, location_material_id):
        try:
            return models.NmrLocation.objects.get(id=location_material_id)
        except models.NmrLocation.DoesNotExist:
            raise Http404

    def post(self, request):
        location_material_id = request.data.get('location_material_id')
        if location_material_id != None:
            NmrLocationMaterial = self.get_object(request, location_material_id)
            NmrLocationMaterial.delete()
            return JsonResponse(data=[], code=0, msg='Delete Success')
        else:
            return JsonResponse(data=[], code=1, msg='False')