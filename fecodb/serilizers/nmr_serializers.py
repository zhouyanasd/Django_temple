from rest_framework import serializers
from fecodb import models

class NmrSerializers(serializers.ModelSerializer):
    status = serializers.IntegerField(source='state')
    location_id = serializers.IntegerField(source='location.id')
    material_id = serializers.IntegerField(source='material.id')

    class Meta:
        model = models.Nmr
        fields = ('id','sample_time','import_time','status','value','location_id','material_id', 'is_evaluate')


class NmrSerializersAdd(serializers.ModelSerializer):
    status = serializers.IntegerField(source='state')
    location_id = serializers.PrimaryKeyRelatedField(source='location', queryset=models.NmrLocation.objects.all())
    material_id = serializers.PrimaryKeyRelatedField(source='material', queryset=models.NmrMaterial.objects.all())
    value = serializers.CharField(max_length=100000)
    is_evaluate = serializers.IntegerField()
    sample_time = serializers.DateField()

    class Meta:
        model = models.Nmr
        fields = ('id','sample_time','status','value','location_id','material_id', 'is_evaluate')


class NmrSerializersUpdate(serializers.ModelSerializer):
    status = serializers.IntegerField(source='state',allow_null=True, default=None)
    location_id = serializers.PrimaryKeyRelatedField(source='location', queryset=models.NmrLocation.objects.all(),
                                                     allow_null=True, default=None)
    material_id = serializers.PrimaryKeyRelatedField(source='material', queryset=models.NmrMaterial.objects.all(),
                                                     allow_null=True, default=None)
    value = serializers.CharField(max_length=100000,allow_null=True, default=None)
    is_evaluate = serializers.IntegerField()

    class Meta:
        model = models.Nmr
        fields = ('id','sample_time','status','value','location_id','material_id','is_evaluate')