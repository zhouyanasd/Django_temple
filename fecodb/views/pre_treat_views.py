from django.http import Http404
from rest_framework.views import APIView

from fecodb import models
from fecodb.serilizers import pre_treat_serializers
from fecodb.utils.json import JsonResponse

class PreTreatmentMethodList(APIView):
    def get_object(self, request, status):
        status = request.GET.get('status')
        kwargs = {}
        if status != None:
            kwargs['state'] = status
        try:
            Queryset = models.PreTreatmentMethod.objects.filter(**kwargs)
            return Queryset
        except models.PreTreatmentMethod.DoesNotExist:
            raise Http404

    def get(self, request):
        status = request.GET.get('status')
        PreTreatmentMethod = self.get_object(request, status)
        serializer = pre_treat_serializers.PreTreatmentMethodSerializers(PreTreatmentMethod, many=True)
        return JsonResponse(data=serializer.data, code= 0, msg='get PreTreatmentMethodList success')


class PreTreatmentMethodDetail(APIView):
    def get_object(self, request, pre_treat_id):
        try:
            return models.PreTreatmentMethod.objects.filter(id=pre_treat_id)
        except models.PreTreatmentMethod.DoesNotExist:
            raise Http404

    def get(self, request,pre_treat_id=None):
        pre_treat_id= request.GET.get('pre_treat_id')
        if pre_treat_id != None:
            PreTreatmentMethod = self.get_object(request, pre_treat_id)
            serializer = pre_treat_serializers.PreTreatmentMethodSerializers(PreTreatmentMethod, many=True)
            return JsonResponse(data=serializer.data, code=0, msg='get PreTreatmentMethodDetail success')
        else:
            return JsonResponse(data=[], code= 1, msg='False')

class PreTreatmentMethodAdd(APIView):
    def post(self, request):
        if request.data.get('name') !=None:
            data = {
                'name': request.data.get('name'),
                'desc': request.data.get('desc'),
                'status': int(request.data.get('status')),
                'input': request.data.get('output'),
                'output': request.data.get('output'),
                'params': request.data.get('params'),
                'priority': request.data.get('priority'),
            }
            serializer = pre_treat_serializers.PreTreatmentMethodSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='add PreTreatmentMethod success')
        else:
            return JsonResponse(data=[], code=1, msg='False')

class PreTreatmentMethodUpdate(APIView):
    def get_object(self, request, pre_treat_id):
        try:
            return models.PreTreatmentMethod.objects.get(id=pre_treat_id)
        except models.PreTreatmentMethod.DoesNotExist:
            raise Http404

    def post(self, request):
        pre_treat_id = request.data.get('pre_treat_id')
        priority = request.data.get('priority')
        if pre_treat_id != None and priority != None:
            PreTreatmentMethod = self.get_object(request, pre_treat_id)
            data = {
                'name': request.data.get('name'),
                'desc': request.data.get('desc'),
                'status': int(request.data.get('status')),
                'input': request.data.get('output'),
                'output': request.data.get('output'),
                'params': request.data.get('params'),
                'priority': request.data.get('priority'),
            }
            serializer = pre_treat_serializers.PreTreatmentMethodSerializers(PreTreatmentMethod, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='update PreTreatmentMethod success')
        else:
            return JsonResponse(data=[], code=1, msg='False')
class PreTreatmentMethodDelete(APIView):
    def get_object(self, request, pre_treat_id):
        try:
            return models.PreTreatmentMethod.objects.get(id=pre_treat_id)
        except models.PreTreatmentMethod.DoesNotExist:
             raise Http404

    def post(self, request):
        pre_treat_id = request.data.get('pre_treat_id')
        if pre_treat_id!=None:
            PreTreatmentMethod = self.get_object(request, pre_treat_id)
            PreTreatmentMethod.delete()
            return JsonResponse(data=[], code=0, msg='Delete Success')
        else:
            return JsonResponse(data=[], code=1, msg='False')