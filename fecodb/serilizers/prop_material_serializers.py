from rest_framework import serializers
from fecodb import  models

class NmrMaterialPropSerializers(serializers.ModelSerializer):
    property_id = serializers.IntegerField(source='property.id')
    property_name = serializers.CharField(source='property.name')
    property_desc = serializers.CharField(source='property.description')
    property_status = serializers.IntegerField(source='property.state')
    property_range = serializers.CharField(source='property.range')
    property_error = serializers.CharField(source='property.error')
    material_id = serializers.IntegerField(source='material.id')
    material_name = serializers.CharField(source='material.name')
    material_desc = serializers.CharField(source='material.description')
    material_status = serializers.IntegerField(source='material.state')
    material_location_id = serializers.PrimaryKeyRelatedField(source='material.location_id',
                                                            many=True, read_only=True)
    process_id = serializers.IntegerField(source='conf_id')
    status = serializers.IntegerField(source='state')

    class Meta:
        model = models.NmrMaterialProp
        fields = ('id','property_id','property_name','property_desc','property_status',
                  'property_range','property_error','material_id','material_name','material_desc',
                  'material_status', 'process_id','material_location_id','status')


class NmrMaterialPropSerializersAdd(serializers.ModelSerializer):
    status = serializers.IntegerField(source='state')
    process_id = serializers.IntegerField(source='conf_id')
    material_id = serializers.PrimaryKeyRelatedField(source='material', queryset=models.NmrMaterial.objects.all())
    property_id = serializers.PrimaryKeyRelatedField(source='property', queryset=models.PropName.objects.all())

    class Meta:
        model = models.NmrMaterialProp
        fields = ('id', 'material_id','property_id','process_id','status')


class NmrMaterialPropSerializersUpdate(serializers.ModelSerializer):
    status = serializers.IntegerField(source='state', allow_null=True, default=None)
    process_id = serializers.IntegerField(source='conf_id',allow_null=True, default=None)
    material_id = serializers.PrimaryKeyRelatedField(source='material', queryset=models.NmrMaterial.objects.all(),
                                                     allow_null=True, default=None)
    property_id = serializers.PrimaryKeyRelatedField(source='property', queryset=models.PropName.objects.all(),
                                                     allow_null=True, default=None)

    class Meta:
        model = models.NmrMaterialProp
        fields = ('id', 'material_id','property_id','process_id','status')