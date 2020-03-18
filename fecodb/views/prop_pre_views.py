from django.http import Http404
from rest_framework.views import APIView

from fecodb import models
from fecodb.serilizers import prop_pre_serializers
from fecodb.utils.json import JsonResponse


class PropPreMethodList(APIView):
    def get_object(self, request):
        pre_treat_id = request.GET.get('pre_treat_id')
        property_id = request.GET.get('property_id')
        material_id = request.GET.get('material_id')
        status = request.GET.get('status')
        kwargs = {}
        if pre_treat_id != None:
            kwargs['pre_treat'] = pre_treat_id
        if property_id != None:
            kwargs['prop_material__property'] = property_id
        if material_id != None:
            kwargs['prop_material__material'] = material_id
        if status != None:
            kwargs['pre_process__state'] = status
        try:
            Queryset = models.PropPreMethod.objects.filter(**kwargs)
            return Queryset
        except models.PropPreMethod.DoesNotExist:
            raise Http404

    def get(self, request):
        PropPreMethod = self.get_object(request)
        serializer = prop_pre_serializers.PropPreMethodSerializers(PropPreMethod, many=True)
        return JsonResponse(data=serializer.data, code=0)


class PropPreMethodDetail(APIView):
    def get_object(self, request, prop_pre_id):
        try:
            return models.PropPreMethod.objects.get(id=prop_pre_id)
        except models.PropPreMethod.DoesNotExist:
            raise Http404

    def get(self, request):
        prop_pre_id= request.GET.get('prop_pre_id')
        if prop_pre_id != None:
            PropPreMethod = self.get_object(request, prop_pre_id)
            serializer = prop_pre_serializers.PropPreMethodSerializers(PropPreMethod)
            return JsonResponse(data=serializer.data, code=0, msg='get PropPreMethodDetail success')
        else:
            return JsonResponse(data=[], code= 1, msg='False')


class PropPreMethodAdd(APIView):
    def get_prop_material_id(self,request):
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        try:
            prop_material= models.NmrMaterialProp.objects.get(property=property_id, material= material_id)
            return prop_material.id
        except models.NmrMaterialProp.DoesNotExist:
             raise Http404

    def post(self,request):
        name = request.data.get('name')
        desc = request.data.get('desc')
        params = request.data.get('params')
        pre_treat_id = request.data.get('pre_treat_id')
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        pre_process_id = request.data.get('pre_process_id')
        priority = request.data.get('priority')
        if pre_treat_id !=None and property_id != None and material_id != None \
                and pre_process_id != None and priority != None:
            prop_material = self.get_prop_material_id(request)
            data = {
                'name': name,
                'desc': desc,
                'prop_material': prop_material,
                'params': params,
                'pre_treat_id': pre_treat_id,
                'pre_process_id': pre_process_id,
                'priority': priority,
            }
            serializer = prop_pre_serializers.PropPreMethodSerializersAdd(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='add PropPreMethodProps success')
            return JsonResponse(data=[], code=1, msg='False')
        else:
            return JsonResponse(data=[], code=1, msg='False')




class PropPreMethodUpdate(APIView):
    def get_prop_material_id(self,request):
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        try:
            prop_material= models.NmrMaterialProp.objects.get(property=property_id, material= material_id)
            return prop_material.id
        except models.AnalysisProps.DoesNotExist:
             raise Http404

    def get_object(self, request, prop_pre_id):
        try:
            return models.PropPreMethod.objects.get(id=prop_pre_id)
        except models.PropPreMethod.DoesNotExist:
            raise Http404

    def post(self, request):
        prop_pre_id = request.data.get('prop_pre_id')
        property_id = request.data.get('property_id')
        material_id = request.data.get('material_id')
        # name = request.data.get('name')
        # desc = request.data.get('desc')
        # params = request.data.get('params')
        # pre_treat_id = request.data.get('pre_treat_id')
        # pre_process_id = request.data.get('pre_process_id')
        # priority = request.data.get('priority')

        if prop_pre_id != None:
            PropPreMethod = self.get_object(request, prop_pre_id)
            # if name ==None:
            #     name = PropPreMethod.name
            # if desc == None:
            #     desc = PropPreMethod.description
            # if params == None:
            #     params = PropPreMethod.conf_para
            # if pre_treat_id == None:
            #     pre_treat_id = PropPreMethod.pre_treat.id
            # if pre_process_id == None:
            #     pre_process_id = PropPreMethod.pre_process.id
            # if priority ==None:
            #     priority = PropPreMethod.order
            if property_id !=None and material_id != None:
                prop_material = self.get_prop_material_id(request)
            else:
                prop_material = PropPreMethod.prop_material.id
            # data = {
            #     'name': name,
            #     'desc': desc,
            #     'params': params,
            #     'pre_treat_id': pre_treat_id,
            #     'pre_process_id': pre_process_id,
            #     'priority': priority,
            #     'prop_material': prop_material,
            # }
            data = request.data.copy()
            data.update({'prop_material':prop_material})
            serializer = prop_pre_serializers.PropPreMethodSerializersUpdate(PropPreMethod, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, code=0, msg='add PropPreMethodProps success')
            return JsonResponse(data=[], code=1, msg='data valid False')
        else:
            return JsonResponse(data=[], code=1, msg='False')


class PropPreMethodDelete(APIView):
    def get_object(self, request, prop_pre_id):
        try:
            return models.PropPreMethod.objects.get(id=prop_pre_id)
        except models.PropPreMethod.DoesNotExist:
            raise Http404

    def get(self, request):
        prop_pre_id= request.GET.get('prop_pre_id')
        if prop_pre_id != None:
            PropPreMethod = self.get_object(request, prop_pre_id)
            PropPreMethod.delete()
            return JsonResponse(data=[], code=0, msg='get PropPreMethod success')
        else:
            return JsonResponse(data=[], code= 1, msg='False')