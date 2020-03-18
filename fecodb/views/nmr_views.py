from django.http import Http404
from rest_framework.views import APIView
from django.db.models import Q
import json

from fecodb import models
from fecodb.serilizers import nmr_serializers
from fecodb.utils.json import JsonResponse
from fecodb.utils.json import JsonResponse_list


class NmrList(APIView):
    def get_object(self, request):
        start_time = request.GET.get('start_time')
        end_time = request.GET.get('end_time')
        location_id = request.GET.get('location_id')
        material_id = request.GET.get('material_id')
        status = request.GET.get('status')
        is_evaluate = request.GET.get('is_evaluate')
        page_index = 0
        page_size = 20
        if request.GET.get('page_index') != None:
            page_index = request.GET.get('page_index')
        if request.GET.get('page_size') != None:
            page_size = request.GET.get('page_size')
        start = page_index*page_size
        end = (page_index+1)*page_size
        di = {}
        if status != None:
            di['state'] = status
        if material_id != None:
            di['material'] = material_id
        if location_id != None:
            di['location'] = location_id
        if start_time != None:
            di['sample_time__gte'] = start_time
        if end_time != None:
            di['sample_time__lte'] = end_time
        if is_evaluate != None:
            di['is_evaluate'] = is_evaluate
        q = Q()
        for i in di:
            q.add(Q(**{i: di[i]}), Q.AND)
        try:
            return models.Nmr.objects.filter(q)[start:end],page_size
        except models.Nmr.DoesNotExist:
            raise Http404

    def get(self, request):
        PropName, page_size = self.get_object(request)
        serializer = nmr_serializers.NmrSerializers(PropName, many=True)
        return JsonResponse_list(data=serializer.data, code=0, msg='get NmrList success',
                                 page_size=page_size, total= PropName.count())


class NmrDetail(APIView):
    def get_object(self, request, nmr_id):
        try:
            return models.Nmr.objects.get(id=nmr_id)
        except models.Nmr.DoesNotExist:
            raise Http404

    def get(self, request):
        nmr_id = request.GET.get('nmr_id')
        if nmr_id != None:
            Nmr = self.get_object(request, nmr_id)
            serializer = nmr_serializers.NmrSerializers(Nmr)
            return JsonResponse(data=serializer.data, code= 0, msg='get NmrDetail success')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class NmrAdd(APIView):
    def post(self,request):
        data = request.data
        serializer = nmr_serializers.NmrSerializersAdd(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, code=0, msg='add Nmr success')
        return JsonResponse(data=[], code=1, msg='data valid False')


class NmrUpdate(APIView):
    def get_object(self, request, nmr_id):
        try:
            return models.Nmr.objects.get(id=nmr_id)
        except models.Nmr.DoesNotExist:
            raise Http404

    def post(self,request):
        nmr_id = request.data.get('nmr_id')
        if nmr_id != None:
            Nmr = self.get_object(request,nmr_id)
            data = request.data
            serializer = nmr_serializers.NmrSerializersAdd(Nmr, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='update Nmr success')
            return JsonResponse(data=[], code=1, msg='data valid False')
        else:
            return JsonResponse(data=[], code=1, msg='False')

class NmrDelete(APIView):
    def get_object(self, request, nmr_id):
        try:
            return models.Nmr.objects.get(id=nmr_id)
        except models.NmrLocation.DoesNotExist:
             raise Http404

    def post(self, request):
        nmr_id = request.data.get('nmr_id')
        if nmr_id!=None:
            NmrLocation = self.get_object(request, nmr_id)
            NmrLocation.delete()
            return JsonResponse(data=[], code=0, msg='Delete Success')
        else:
            return JsonResponse(data=[], code=1, msg='False')