from rest_framework import serializers
from fecodb import models


class AnalysisPropsSerializers(serializers.ModelSerializer):
    status = serializers.IntegerField(source='state')
    location_id = serializers.PrimaryKeyRelatedField(source='nmr_id.location.id', read_only=True)
    material_id = serializers.PrimaryKeyRelatedField(source='nmr_id.material.id', read_only=True)
    property_id = serializers.PrimaryKeyRelatedField(source='prop_material.property.id', read_only=True)
    process_id = serializers.PrimaryKeyRelatedField(source='pre_ana', read_only=True)
    sample_time = serializers.DateField(source='add_time')

    class Meta:
        model = models.AnalysisProps
        fields = (
            'id', 'status', 'nmr_id', 'value', 'analysis_time', 'process_id', 'value', 'location_id', 'material_id',
            'property_id', 'sample_time')


class AnalysisPropsSerializersAdd(serializers.ModelSerializer):
    sample_time = serializers.DateField(source='add_time')
    location_id = serializers.PrimaryKeyRelatedField(source='nmr_id.location.id', read_only=True)
    material_id = serializers.PrimaryKeyRelatedField(source='nmr_id.material.id', read_only=True)
    property_id = serializers.PrimaryKeyRelatedField(source='prop_material.property.id', read_only=True)
    process_id = serializers.PrimaryKeyRelatedField(source='pre_ana', queryset=models.PreAnalysisProcess.objects.all())
    status = serializers.IntegerField(source='state')

    def create(self, validated_data):
        print('create', type(validated_data), validated_data)
        sample_time = validated_data['add_time']
        process_id = validated_data['pre_ana']
        status = validated_data['state']
        value = validated_data['value']
        prop_material = validated_data['prop_material']
        nmr_id = validated_data['nmr_id']
        AnalysisProps = models.AnalysisProps(add_time=sample_time, pre_ana=process_id, state=status, value=value,
                                             prop_material=prop_material, nmr_id=nmr_id)
        AnalysisProps.save()
        return AnalysisProps

    class Meta:
        model = models.AnalysisProps
        fields = (
        'id', 'status', 'nmr_id', 'value', 'analysis_time', 'process_id', 'value', 'prop_material', 'sample_time',
        'location_id', 'material_id', 'property_id')


class AnalysisPropsSerializersUpdate(serializers.ModelSerializer):
    sample_time = serializers.DateField(source='add_time')
    location_id = serializers.PrimaryKeyRelatedField(source='nmr_id.location.id', read_only=True)
    material_id = serializers.PrimaryKeyRelatedField(source='nmr_id.material.id', read_only=True)
    property_id = serializers.PrimaryKeyRelatedField(source='prop_material.property.id', read_only=True)
    process_id = serializers.PrimaryKeyRelatedField(source='pre_ana',
                                                    queryset=models.PreAnalysisProcess.objects.all())
    status = serializers.IntegerField(source='state')

    def update(self, instance, validated_data):
        print('update', type(instance), instance, validated_data)
        instance.add_time = validated_data.get('sample_time', instance.add_time)
        instance.pre_ana = validated_data.get('process_id', instance.pre_ana)
        instance.state = validated_data.get('status', instance.state)
        instance.value = validated_data.get('value', instance.value)
        instance.prop_material = validated_data.get('prop_material', instance.prop_material)
        instance.nmr_id = validated_data.get('nmr_id', instance.nmr_id)
        instance.save()
        return instance

    class Meta:
        model = models.AnalysisProps
        fields = (
            'id', 'status', 'nmr_id', 'value', 'analysis_time', 'process_id', 'value', 'prop_material',
            'sample_time', 'location_id', 'material_id', 'property_id')
