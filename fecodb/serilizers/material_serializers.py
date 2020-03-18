from rest_framework import serializers
from fecodb import  models

class NmrMaterialPropSerializers(serializers.ModelSerializer):
    property_id = serializers.IntegerField(source='property.id')
    property_material_id = serializers.IntegerField(source='id')
    class Meta:
        model = models.NmrMaterialProp
        fields = ('property_material_id','property_id')


class NmrLocationMaterialSerializers(serializers.ModelSerializer):
    location_material_id = serializers.IntegerField(source='id')
    location_id = serializers.IntegerField(source='location.id')
    class Meta:
        model = models.NmrLocationMaterial
        fields = ('location_material_id','location_id')


class NmrMaterialSerializers(serializers.ModelSerializer):
    property_material = NmrMaterialPropSerializers(read_only=True, many=True)
    location_material = NmrLocationMaterialSerializers(read_only=True, many=True)
    desc = serializers.CharField(source='description')
    status = serializers.IntegerField(source='state')
    class Meta:
        model = models.NmrMaterial
        fields = ('id','name','desc','status','property_material','location_material')








