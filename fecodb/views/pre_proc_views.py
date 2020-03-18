from django.http import Http404
from rest_framework.views import APIView

from fecodb import models
from fecodb.serilizers import pre_proc_serializers,prop_pre_serializers
from fecodb.utils.json import JsonResponse
import json

class PropPreProcessList(APIView):
    def get_object(self,request):
        property_id = request.GET.get('property_id')
        material_id = request.GET.get('material_id')
        status = request.GET.get('status')
        kwargs = {}
        if status != None:
            kwargs['state'] = status
        if property_id != None:
            kwargs['property_material__prop_material__property'] = property_id
        if material_id != None:
            kwargs['property_material__prop_material__material'] = material_id
        try:
            Queryset = models.PropPreProcess.objects.filter(**kwargs)
            return Queryset
        except models.PropPreProcess.DoesNotExist:
            raise Http404

    def get(self, request):
        PropPreProcess = self.get_object(request)
        serializer = pre_proc_serializers.PropPreProcessSerializers(PropPreProcess, many=True)
        return JsonResponse(data=serializer.data, code=0, msg='get PropPreProcessList success')



class PropPreProcessDetail(APIView):
    def get_object(self, request, pre_proc_id):
        try:
            return models.PropPreProcess.objects.get(id=pre_proc_id)
        except models.PropPreProcess.DoesNotExist:
             raise Http404

    def get(self, request):
        pre_proc_id = request.GET.get('pre_proc_id')
        if pre_proc_id != None:
            PropPreProcess = self.get_object(request, pre_proc_id)
            serializer = pre_proc_serializers.PropPreProcessSerializers(PropPreProcess)
            return JsonResponse(data=serializer.data, code= 0, msg='get PropPreProcessDetail success')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class PropPreProcessAdd(APIView):
    def post(self, request):
        data = request.data.copy()
        serializer = pre_proc_serializers.PropPreProcessSerializersAdd(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, code=0, msg='add PropPreProcess success')
        return JsonResponse(data=[], code=1, msg='data valid False')


# class PropPreProcessAddPreList(APIView):
#     def post(self, request):
#         data = request.data.copy()
#         property_material = json.loads(data.get('prop_pre_list'))
#         data.update({'property_material': property_material})
#         data.pop('prop_pre_list')
#         print(data)
#         serializer = pre_proc_serializers.PropPreProcessSerializersAddPreList(data=data)
#         if serializer.is_valid():
#             # serializer.save()
#             return JsonResponse(data=serializer.data, code=0, msg='add PropPreProcess success')
#         return JsonResponse(data=[], code=1, msg='data valid False')

class PropPreProcessAddPreList(APIView):
    def get_object(self, request, pre_proc_id):
        try:
            return models.PropPreProcess.objects.get(id=pre_proc_id)
        except models.PropPreProcess.DoesNotExist:
             raise Http404

    def get_prop_material_id(self,request):
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        try:
            prop_material= models.NmrMaterialProp.objects.get(property=property_id, material= material_id)
            return prop_material.id
        except models.NmrMaterialProp.DoesNotExist:
             raise Http404

    def post(self, request):
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        if property_id!=None and material_id!=None:
            prop_material = self.get_prop_material_id(request)
            data = request.data.copy()
            prop_pre_list = json.loads(data.get('prop_pre_list'))
            serializer = pre_proc_serializers.PropPreProcessSerializersAdd(data=data)
            if serializer.is_valid():
                serializer.save()
                #----save methods--------------
                for prop_pre in prop_pre_list:
                    prop_pre['prop_material'] = prop_material
                    prop_pre['pre_process_id'] = serializer.data['id']
                    serializer_method=prop_pre_serializers.PropPreMethodSerializersAdd(data=prop_pre)
                    if serializer_method.is_valid():
                        serializer_method.save()
                    else:
                        return JsonResponse(data=[], code=1, msg='prop_pre_list valid False')
                #---------------------------------
                PropPreProcess = self.get_object(request, serializer.data['id'])
                serializer = pre_proc_serializers.PropPreProcessSerializers(PropPreProcess)
                return JsonResponse(data=serializer.data, code=0, msg='add PropPreProcess success')
            else:
                return JsonResponse(data=[], code=1, msg='data valid False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class PropPreProcessUpdate(APIView):
    def get_object(self, request, pre_proc_id):
        try:
            return models.PropPreProcess.objects.get(id=pre_proc_id)
        except models.PropPreProcess.DoesNotExist:
             raise Http404

    def get_object_method(self, request, prop_pre_id):
        try:
            return models.PropPreMethod.objects.get(id=prop_pre_id)
        except models.PropPreMethod.DoesNotExist:
            raise Http404

    def get_prop_material_id(self,request):
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        try:
            prop_material= models.NmrMaterialProp.objects.get(property=property_id, material= material_id)
            return prop_material.id
        except models.NmrMaterialProp.DoesNotExist:
             raise Http404

    def post(self, request):
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        pre_proc_id = request.data.get('pre_proc_id')
        if pre_proc_id != None:
            PropPreProcess = self.get_object(request, pre_proc_id)
            data = request.data.copy()
            prop_pre_list = json.loads(data.get('prop_pre_list'))
            serializer = pre_proc_serializers.PropPreProcessSerializersUpdate(PropPreProcess, data=data)
            if serializer.is_valid():
                serializer.save()
                #----updata methods--------------
                for prop_pre in prop_pre_list:
                    prop_pre_id = prop_pre['prop_pre_id']
                    if prop_pre_id != None:
                        PropPreMethod = self.get_object(request, prop_pre_id)
                        if property_id != None and material_id != None:
                            prop_material = self.get_prop_material_id(request)
                        else:
                            prop_material = PropPreMethod.prop_material.id
                        prop_pre['prop_material'] = prop_material
                        serializer = prop_pre_serializers.PropPreMethodSerializersUpdate(PropPreMethod, data=prop_pre)
                        if serializer.is_valid():
                            serializer.save()
                        else:
                            return JsonResponse(data=[], code=1, msg='data valid False')
                #---------------------------------
                return JsonResponse(data=serializer.data, code=0, msg='update PropPreProcess success')
            return JsonResponse(data=[], code=1, msg='data valid False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class PropPreProcessUpdatePreList(APIView):
    def get_object(self, request, pre_proc_id):
        try:
            return models.PropPreProcess.objects.get(id=pre_proc_id)
        except models.PropPreProcess.DoesNotExist:
             raise Http404

    def post(self, request):
        pre_proc_id = request.data.get('pre_proc_id')
        if pre_proc_id != None:
            PropPreProcess = self.get_object(request, pre_proc_id)
            data = request.data.copy()
            serializer = pre_proc_serializers.PropPreProcessSerializersUpdate(PropPreProcess, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='update PropPreProcess success')
            return JsonResponse(data=[], code=1, msg='data valid False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class PropPreProcessDelete(APIView):
    def get_object(self, request, pre_proc_id):
        try:
            return models.PropPreProcess.objects.get(id=pre_proc_id)
        except models.PropPreProcess.DoesNotExist:
             raise Http404

    def post(self, request):
        pre_proc_id = request.data.get('pre_proc_id')
        if pre_proc_id != None:
            PropPreProcess = self.get_object(request, pre_proc_id)
            PropPreProcess.delete()
            return JsonResponse(data=[], code= 0, msg='delete PropPreProcess success')
        else:
            return JsonResponse(data=[], code=1, msg='False')
