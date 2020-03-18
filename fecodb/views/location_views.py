from django.http import Http404
from rest_framework.views import APIView

from fecodb import models
from fecodb.serilizers import location_serializers
from fecodb.utils.json import JsonResponse


class NmrLocationList(APIView):
    def get_object(self, request, status):
        try:
            status = request.GET.get('status')
            material_id = request.GET.get('material_id')
            if status != None and material_id == None:
                NmrLocation = models.NmrLocation.objects.filter(state=status)
            elif status == None and material_id != None:
                NmrLocation = models.NmrLocation.objects.filter(material_id=material_id)
            elif status !=None and material_id != None:
                NmrLocation = models.NmrLocation.objects.filter(state=status, material_id=material_id)
            else:
                NmrLocation = models.NmrLocation.objects.all()
            return NmrLocation
        except models.NmrLocation.DoesNotExist:
            raise Http404

    def get(self, request, status=None):
        status = request.GET.get('status')
        NmrLocation = self.get_object(request, status)
        serializer = location_serializers.NmrLocationSerializers(NmrLocation, many= True)
        return JsonResponse(data=serializer.data, code= 0, msg='get NmrLocationList success')

class NmrLocationDetail(APIView):
    def get_object(self, request, location_id):
        try:
            return models.NmrLocation.objects.get(id=location_id)
        except models.NmrLocation.DoesNotExist:
             raise Http404

    def get(self, request):
        location_id = request.GET.get('location_id')
        if location_id != None:
            NmrLocation = self.get_object(request, location_id)
            serializer = location_serializers.NmrLocationSerializers(NmrLocation)
            return JsonResponse(data=serializer.data, code= 0, msg='get NmrLocationDetail success')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class NmrLocationAdd(APIView):
    def post(self, request):
        if request.data.get('name') !=None:
            data = {
                'name': request.data.get('name'),
                'desc': request.data.get('desc'),
                'status': int(request.data.get('status')),
            }
            serializer = location_serializers.NmrLocationSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='add NmrLocation success')
            return JsonResponse(data=[], code=1, msg='False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class NmrLocationUpdate(APIView):
    def get_object(self, request, location_id):
        try:
            return models.NmrLocation.objects.get(id=location_id)
        except models.NmrLocation.DoesNotExist:
            raise Http404

    def post(self, request):
        location_id = request.data.get('location_id')
        if location_id != None:
            NmrLocation = self.get_object(request, location_id)
            data = {
                'name': request.data.get('name'),
                'desc': request.data.get('desc'),
                'status': int(request.data.get('status')),
            }
            serializer = location_serializers.NmrLocationSerializers(NmrLocation, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='update NmrLocation success')
            return JsonResponse(data=[], code=1, msg='False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class NmrLocationDelete(APIView):
    def get_object(self, request, location_id):
        try:
            return models.NmrLocation.objects.get(id=location_id)
        except models.NmrLocation.DoesNotExist:
             raise Http404

    def post(self, request):
        location_id = request.data.get('location_id')
        if location_id!=None:
            NmrLocation = self.get_object(request, location_id)
            NmrLocation.delete()
            return JsonResponse(data=[], code=0, msg='Delete Success')
        else:
            return JsonResponse(data=[], code=1, msg='False')

