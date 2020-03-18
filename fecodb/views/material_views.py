from django.http import Http404
from rest_framework.views import APIView

from fecodb import models
from fecodb.serilizers import material_serializers
from fecodb.utils.json import JsonResponse


class NmrMaterialList(APIView):
    def get_object(self, request):
        try:
            status = request.GET.get('status')
            location_id = request.GET.get('location_id')
            if status != None and location_id == None:
                NmrMaterial = models.NmrMaterial.objects.filter(state=status)
            elif status == None and location_id != None:
                NmrMaterial = models.NmrMaterial.objects.filter(location_id=location_id)
            elif status !=None and location_id != None:
                NmrMaterial = models.NmrMaterial.objects.filter(state=status,location_id=location_id)
            else:
                NmrMaterial = models.NmrMaterial.objects.all()
            return NmrMaterial
        except models.NmrMaterial.DoesNotExist:
            raise Http404

    def get(self, request):
        NmrMaterial = self.get_object(request)
        serializer = material_serializers.NmrMaterialSerializers(NmrMaterial, many= True)
        return JsonResponse(data=serializer.data, code= 0, msg='get NmrMaterialList success')


class NmrMaterialDetail(APIView):
    def get_object(self, request, material_id):
        try:
            return models.NmrMaterial.objects.get(id=material_id)
        except models.NmrMaterial.DoesNotExist:
            raise Http404

    def get(self, request):
        material_id = request.GET.get('material_id')
        if material_id != None:
            NmrMaterial = self.get_object(request, material_id)
            serializer = material_serializers.NmrMaterialSerializers(NmrMaterial)
            return JsonResponse(data=serializer.data, code= 0, msg='get NmrMaterialDetail success')
        else:
            return JsonResponse(data=[], code=1, msg='False')

class NmrMaterialAdd(APIView):
    def post(self, request):
        if request.data.get('name') !=None:
            data = {
                'name': request.data.get('name'),
                'desc': request.data.get('desc'),
                'status': int(request.data.get('status'))
            }
            serializer = material_serializers.NmrMaterialSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='add NmrMaterial success')
            return JsonResponse(data=[], code=1, msg='False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class NmrMaterialUpdate(APIView):
    def get_object(self, request, material_id):
        try:
            return models.NmrMaterial.objects.get(id=material_id)
        except models.NmrMaterial.DoesNotExist:
            raise Http404

    def post(self, request):
        material_id = request.data.get('material_id')
        if material_id != None:
            NmrLocation = self.get_object(request, material_id)
            data = {
                'name': request.data.get('name'),
                'desc': request.data.get('desc'),
                'status': int(request.data.get('status'))
            }
            serializer = material_serializers.NmrMaterialSerializers(NmrLocation, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='update NmrMaterial success')
            return JsonResponse(data=[], code=1, msg='False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class NmrMaterialDelete(APIView):
    def get_object(self, request, material_id):
        try:
            return models.NmrMaterial.objects.get(id=material_id)
        except models.NmrMaterial.DoesNotExist:
             raise Http404

    def post(self, request):
        material_id = request.data.get('material_id')
        if material_id!=None:
            NmrMaterial = self.get_object(request, material_id)
            NmrMaterial.delete()
            return JsonResponse(data=[], code=0, msg='Delete Success')
        else:
            return JsonResponse(data=[], code=1, msg='False')
