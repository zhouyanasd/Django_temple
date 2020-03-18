from rest_framework import serializers
from fecodb import  models

class NmrMaterialPropSerializers(serializers.ModelSerializer):
    process_id = serializers.IntegerField(source='conf_id')
    material_id = serializers.IntegerField(source='material.id')
    property_material_id = serializers.IntegerField(source='id')
    class Meta:
        model = models.NmrMaterialProp
        fields = ('property_material_id','material_id','process_id')


class PropNameSerializers(serializers.ModelSerializer):
    property_material = NmrMaterialPropSerializers(read_only= True, many=True)
    desc = serializers.CharField(source='description')
    status = serializers.IntegerField(source='state')
    class Meta:
        model = models.PropName
        fields = ('id','name','desc','status','range','error','property_material')
