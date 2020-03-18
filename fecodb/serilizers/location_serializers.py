from rest_framework import serializers
from fecodb import  models

class NmrLocationMaterialSerializers(serializers.ModelSerializer):
    location_material_id = serializers.IntegerField(source='id')
    material_id = serializers.IntegerField(source='material.id')
    class Meta:
        model = models.NmrLocationMaterial
        fields = ('location_material_id','material_id')

class NmrLocationSerializers(serializers.ModelSerializer):
    location_material = NmrLocationMaterialSerializers(read_only=True, many=True)
    desc = serializers.CharField(source='description')
    status = serializers.IntegerField(source='state')
    class Meta:
        model = models.NmrLocation
        fields = ('id','name','desc','status','location_material')
