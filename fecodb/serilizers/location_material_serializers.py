from rest_framework import serializers
from fecodb import  models

class NmrLocationMaterialSerializers(serializers.ModelSerializer):
    location_id = serializers.IntegerField(source='location.id')
    location_name = serializers.CharField(source='location.name')
    location_desc = serializers.CharField(source='location.description')
    location_status = serializers.IntegerField(source='location.state')
    material_id = serializers.IntegerField(source='material.id')
    material_name = serializers.CharField(source='material.name')
    material_desc = serializers.CharField(source='material.description')
    material_status = serializers.IntegerField(source='material.state')
    material_property_id = serializers.PrimaryKeyRelatedField(source='material.property_id',
                                                              many=True, read_only=True)
    status = serializers.IntegerField(source='state')

    class Meta:
        model = models.NmrLocationMaterial
        fields = ('id', 'location_id','location_name','location_desc',
                  'location_status', 'material_id','material_name','material_desc',
                  'material_status', 'material_property_id','status')


class NmrLocationMaterialSerializersAdd(serializers.ModelSerializer):
    status = serializers.IntegerField(source='state')
    location_id = serializers.PrimaryKeyRelatedField(source='location',queryset=models.NmrLocation.objects.all())
    material_id = serializers.PrimaryKeyRelatedField(source='material',queryset=models.NmrMaterial.objects.all())

    class Meta:
        model = models.NmrLocationMaterial
        fields = ('id', 'location_id','material_id','status')


class NmrLocationMaterialSerializersUpdate(serializers.ModelSerializer):
    status = serializers.IntegerField(source='state')
    location_id = serializers.PrimaryKeyRelatedField(source='location', queryset=models.NmrLocation.objects.all())
    material_id = serializers.PrimaryKeyRelatedField(source='material', queryset=models.NmrMaterial.objects.all())

    class Meta:
        model = models.NmrLocationMaterial
        fields = ('id', 'location_id','material_id','status')