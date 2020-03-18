from django.http import Http404
from rest_framework.views import APIView

from fecodb import models
from fecodb.serilizers import analysis_method_serializers
from fecodb.utils.json import JsonResponse

class AnalysisMethodList(APIView):
    def get_object(self, request):
        status = request.GET.get('status')
        kwargs = {}
        if status != None:
            kwargs['state'] = status
        try:
            Queryset = models.AnalysisMethod.objects.filter(**kwargs)
            return Queryset
        except models.AnalysisMethod.DoesNotExist:
            raise Http404

    def get(self, request):
        AnalysisMethod = self.get_object(request)
        serializer = analysis_method_serializers.AnalysisMethodSerializers(AnalysisMethod, many=True)
        return JsonResponse(data=serializer.data, code= 0, msg='get AnalysisMethodList success')

class AnalysisMethodDetail(APIView):
    def get_object(self, request, analysis_method_id):
        try:
            return models.AnalysisMethod.objects.filter(id=analysis_method_id)
        except models.AnalysisMethod.DoesNotExist:
            raise Http404

    def get(self, request,analysis_method_id=None):
        analysis_method_id= request.GET.get('analysis_method_id')
        if analysis_method_id != None:
            AnalysisMethod = self.get_object(request, analysis_method_id)
            serializer = analysis_method_serializers.AnalysisMethodSerializers(AnalysisMethod, many=True)
            return JsonResponse(data=serializer.data, code=0, msg='get AnalysisMethodDetail success')
        else:
            return JsonResponse(data=[], code= 0, msg='False')

class AnalysisMethodAdd(APIView):
    def post(self, request):
        if request.data.get('name') !=None:
            data = {
                'name': request.data.get('name'),
                'desc': request.data.get('desc'),
                'status': int(request.data.get('status')),
                'input': request.data.get('output'),
                'output': request.data.get('output'),
                'params': request.data.get('params'),
            }
            serializer = analysis_method_serializers.AnalysisMethodSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='add AnalysisMethod success')
        else:
            return JsonResponse(data=[], code=1, msg='False')

class AnalysisMethodUpdate(APIView):
    def get_object(self, request, analysis_method_id):
        try:
            return models.AnalysisMethod.objects.get(id=analysis_method_id)
        except models.AnalysisMethod.DoesNotExist:
            raise Http404

    def post(self, request):
        analysis_method_id = request.data.get('analysis_method_id')
        if analysis_method_id != None:
            AnalysisMethod = self.get_object(request, analysis_method_id)
            data = {
                'name': request.data.get('name'),
                'desc': request.data.get('desc'),
                'status': int(request.data.get('status')),
                'input': request.data.get('output'),
                'output': request.data.get('output'),
                'params': request.data.get('params'),
            }
            serializer = analysis_method_serializers.AnalysisMethodSerializers(AnalysisMethod, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='update AnalysisMethod success')
        else:
            return JsonResponse(data=[], code=1, msg='False')

class AnalysisMethodDelete(APIView):
    def get_object(self, request, analysis_method_id):
        try:
            return models.AnalysisMethod.objects.get(id=analysis_method_id)
        except models.AnalysisMethod.DoesNotExist:
             raise Http404

    def post(self, request):
        analysis_method_id = request.data.get('analysis_method_id')
        if analysis_method_id!=None:
            AnalysisMethod = self.get_object(request, analysis_method_id)
            AnalysisMethod.delete()
            return JsonResponse(data=[], code=0, msg='Delete Success')
        else:
            return JsonResponse(data=[], code=1, msg='False')