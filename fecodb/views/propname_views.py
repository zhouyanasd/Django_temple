#-----------------------------------
#这里的property_id对应关联表中的主键id
#-----------------------------------
from django.http import Http404
from rest_framework.views import APIView

from fecodb import models
from fecodb.serilizers import propname_serializers
from fecodb.utils.json import JsonResponse

class PropNameList(APIView):
    def get_object(self, request):
        try:
            status = request.GET.get('status')
            material_id = request.GET.get('material_id')
            if status != None and material_id == None :
                PropName = models.PropName.objects.filter(state = status)
            elif status == None and material_id != None:
                PropName = models.PropName.objects.filter(material_id = material_id)
            elif status != None and material_id != None:
                PropName = models.PropName.objects.filter(state = status, material_id = material_id)
            else:
                PropName = models.PropName.objects.all()
            return PropName
        except models.PropName.DoesNotExist:
            raise Http404

    def get(self, request):
        PropName = self.get_object(request)
        serializer = propname_serializers.PropNameSerializers(PropName, many= True)
        return JsonResponse(data = serializer.data, code = 0, msg = 'get PropNameList success')


class PropNameDetail(APIView):
    def get_object(self, request, property_id):
        try:
            return models.PropName.objects.get(id=property_id)
        except models.PropName.DoesNotExist:
            raise Http404

    def get(self, request):
        property_id = request.GET.get('property_id')
        if property_id != None:
            PropName = self.get_object(request, property_id)
            serializer = propname_serializers.PropNameSerializers(PropName)
            return JsonResponse(data=serializer.data, code= 0, msg='get PropNameDetail success')
        else:
            return JsonResponse(data=[], code=1, msg='False')
        
        
class PropNameAdd(APIView):
    def post(self, request):
        if request.data.get('name') !=None:
            data = {
                'name': request.data.get('name'),
                'desc': request.data.get('desc'),
                'status': int(request.data.get('status')),
                'range': request.data.get('range'),
                'error': request.data.get('error'),
            }
            serializer = propname_serializers.PropNameSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='add PropName success')
            return JsonResponse(data=[], code=1, msg='False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class PropNameUpdate(APIView):
    def get_object(self, request, property_id):
        try:
            return models.PropName.objects.get(id=property_id)
        except models.PropName.DoesNotExist:
            raise Http404

    def post(self, request):
        property_id = request.data.get('property_id')
        if property_id != None :
            PropName = self.get_object(request, property_id)
            data = {
                'name': request.data.get('name'),
                'desc': request.data.get('desc'),
                'status': int(request.data.get('status')),
                'range': request.data.get('range'),
                'error': request.data.get('error')
            }
            serializer = propname_serializers.PropNameSerializers(PropName, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='update PropName success')
            return JsonResponse(data=[], code=1, msg='False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class PropNameDelete(APIView):
    def get_object(self, request, property_id):
        try:
            return models.PropName.objects.get(id=property_id)
        except models.PropName.DoesNotExist:
             raise Http404

    def post(self, request):
        property_id = request.data.get('property_id')
        if property_id!=None:
            PropName = self.get_object(request, property_id)
            PropName.delete()
            return JsonResponse(data=[], code=0, msg='Delete Success')
        else:
            return JsonResponse(data=[], code=1, msg='False')