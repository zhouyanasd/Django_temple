from django.http import Http404
from rest_framework.views import APIView

from fecodb import models
from fecodb.serilizers import nmr_rlt_serializers
from fecodb.utils.json import JsonResponse
from fecodb.utils.json import JsonResponse_list


class AnalysisPropsList(APIView):
    def get_object(self,request):
        start_time = request.GET.get('start_time')
        end_time = request.GET.get('end_time')
        location_id = request.GET.get('location_id')
        property_id = request.GET.get('property_id')
        material_id = request.GET.get('material_id')
        nmr_id = request.GET.get('nmr_id')
        process_id = request.GET.get('process_id')
        status = request.GET.get('status')
        page_index = 0
        page_size = 20
        if request.GET.get('page_index') != None:
            page_index = request.GET.get('page_index')
        if request.GET.get('page_size') != None:
            page_size = request.GET.get('page_size')
        start = page_index*page_size
        end = (page_index+1)*page_size
        kwargs = {}
        if status != None:
            kwargs['state'] = status
        if property_id != None:
            kwargs['prop_material__property'] = property_id
        if material_id != None:
            kwargs['nmr_id__material'] = material_id
        if location_id != None:
            kwargs['nmr_id__location'] = location_id
        if nmr_id != None:
            kwargs['nmr_id'] = nmr_id
        if process_id != None:
            kwargs['pre_ana'] = process_id
        if start_time != None:
            kwargs['add_time__gte'] = start_time
        if end_time != None:
            kwargs['add_time__lte'] = end_time
        try:
            Queryset = models.AnalysisProps.objects.filter(**kwargs)[start:end],page_size
            return Queryset
        except models.AnalysisProps.DoesNotExist:
            raise Http404

    def get(self, request):
        AnalysisProps, page_size = self.get_object(request)
        serializer = nmr_rlt_serializers.AnalysisPropsSerializers( AnalysisProps, many=True)
        return JsonResponse_list(data=serializer.data, code=0, msg='get AnalysisPropsList success',
                                 page_size=page_size, total= AnalysisProps.count())

class AnalysisPropsDetail(APIView):
    def get_object(self, request, nmr_rlt_id):
        try:
            return models.AnalysisProps.objects.get(id=nmr_rlt_id)
        except models.AnalysisProps.DoesNotExist:
             raise Http404

    def get(self, request):
        nmr_rlt_id = request.GET.get('nmr_rlt_id')
        if nmr_rlt_id != None:
            AnalysisProps = self.get_object(request, nmr_rlt_id)
            serializer = nmr_rlt_serializers.AnalysisPropsSerializers(AnalysisProps)
            return JsonResponse(data=serializer.data, code= 0, msg='get AssayPropsDetail success')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class AnalysisPropsAdd(APIView):
    def get_prop_material_id(self,request):
        property_id = request.data.get('property_id')
        nmr_id = request.data.get('nmr_id')
        try:
            prop_material= models.NmrMaterialProp.objects.get(property=property_id, material__nmr__id= nmr_id)
            return prop_material.id
        except models.AnalysisProps.DoesNotExist:
             raise Http404

    def post(self,request):
        sample_time = request.data.get('sample_time')
        property_id = request.data.get('property_id')
        process_id = request.data.get('process_id')
        nmr_id = request.data.get('nmr_id')
        value = request.data.get('value')
        status = request.data.get('status')
        if status ==None:
            status = 1
        if value != None and sample_time != None and property_id != None and process_id != None and nmr_id != None:
            data = {
                'value':value,
                'sample_time': sample_time,
                'prop_material': self.get_prop_material_id(request),
                'process_id': process_id,
                'nmr_id': nmr_id,
                'status': status,
            }
            serializer = nmr_rlt_serializers.AnalysisPropsSerializersAdd(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='add AnalysisProps success')
            return JsonResponse(data=[], code=1, msg='False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class AnalysisPropsUpdate(APIView):
    def get_prop_material_id(self,request):
        property_id = request.data.get('property_id')
        nmr_id = request.data.get('nmr_id')
        try:
            prop_material= models.NmrMaterialProp.objects.get(property=property_id, nmr__id= nmr_id)
            return prop_material.id
        except models.AnalysisProps.DoesNotExist:
             raise Http404

    def get_object(self, request, nmr_rlt_id):
        try:
            return models.AnalysisProps.objects.get(id=nmr_rlt_id)
        except models.AnalysisProps.DoesNotExist:
             raise Http404

    def post(self,request):
        nmr_rlt_id = request.data.get('nmr_rlt_id')
        sample_time = request.data.get('sample_time')
        property_id = request.data.get('property_id')
        process_id = request.data.get('process_id')
        nmr_id = request.data.get('nmr_id')
        value = request.data.get('value')
        status = request.data.get('status')
        if nmr_rlt_id != None:
            AnalysisProps = self.get_object(request, nmr_rlt_id)
            if sample_time == None:
                sample_time = AnalysisProps.add_time
            if process_id == None:
                process_id = AnalysisProps.pre_ana.id
            if nmr_id ==None:
                nmr_id = AnalysisProps.nmr_id.id
            if value ==None:
                value = AnalysisProps.value
            if status ==None:
                status = AnalysisProps.state
            if property_id ==None:
                prop_material = AnalysisProps.prop_material.id
            else:
                prop_material = self.get_prop_material_id(request)
            data = {
                'value': value,
                'sample_time': sample_time,
                'prop_material': prop_material ,
                'process_id': process_id,
                'nmr_id': nmr_id,
                'status': status,
            }
            serializer = nmr_rlt_serializers.AnalysisPropsSerializersAdd(AnalysisProps, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='add AnalysisProps success')
            return JsonResponse(data=[], code=1, msg='data valid False')
        else:
            return JsonResponse(data=[], code=1, msg='False')



class AnalysisPropsDelete(APIView):
    def get_object(self, request, nmr_rlt_id):
        try:
            return models.AnalysisProps.objects.get(id=nmr_rlt_id)
        except models.AnalysisProps.DoesNotExist:
             raise Http404

    def post(self, request):
        nmr_rlt_id = request.data.get('nmr_rlt_id')
        if nmr_rlt_id != None:
            AnalysisProps = self.get_object(request, nmr_rlt_id)
            AnalysisProps.delete()
            return JsonResponse(data=[], code= 0, msg='get AssayPropsDetail success')
        else:
            return JsonResponse(data=[], code=1, msg='False')
