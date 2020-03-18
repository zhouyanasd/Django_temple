from rest_framework import serializers
from fecodb import models


class PreAnalysisProcessHandSerializers(serializers.Serializer):
    desc = serializers.CharField(source='description')
    edit_date = serializers.DateField(source='edit_time')
    add_date = serializers.DateField(source='add_time')
    status = serializers.IntegerField(source='state')
    name = serializers.CharField()
    id = serializers.IntegerField()
    analysis_proc_id = serializers.IntegerField(source='p_ana_pro', read_only=True)
    pre_proc_id = serializers.IntegerField(source='p_pre_pro', read_only=True)
    material_id = serializers.IntegerField(source='p_pre_pro__property_material__prop_material__material',read_only=True)
    property_id = serializers.IntegerField(source='p_pre_pro__property_material__prop_material__property',read_only=True)


class PreAnalysisProcessHandSerializersAdd(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(allow_blank=True)
    desc = serializers.CharField(source='description',allow_null=True,default=True)
    status = serializers.IntegerField(source='state',allow_null=True,default=True)
    analysis_proc_id = serializers.PrimaryKeyRelatedField(source='p_ana_pro',allow_null=True,default=None,
                                                          queryset=models.PropAnalysisProcess.objects.all())
    pre_proc_id = serializers.PrimaryKeyRelatedField(source='p_pre_pro',allow_null=True,default=None,
                                                     queryset=models.PropPreProcess.objects.all())
    own_id = serializers.PrimaryKeyRelatedField(source='owner_id', write_only=True,allow_null=True,default=None,
                                                queryset=models.UserName.objects.all())
    prop_material = serializers.IntegerField(allow_null=True, default=None, write_only=True)
    edit_date = serializers.DateField(source='edit_time',read_only=True)
    add_date = serializers.DateField(source='add_time',read_only=True)
    material_id = serializers.IntegerField(read_only=True)
    property_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        name = validated_data['name']
        desc = validated_data['description']
        pre_proc_id = validated_data['p_pre_pro']
        analysis_proc_id = validated_data['p_ana_pro']
        prop_material = validated_data['prop_material']
        own_id = validated_data['owner_id']
        status = validated_data['state']
        PreAnalysisProcess = models.PreAnalysisProcess(name=name, description=desc, p_pre_pro=pre_proc_id, p_ana_pro=analysis_proc_id,
                                             prop_material=prop_material, owner_id=own_id, state=status)
        PreAnalysisProcess.save()
        return PreAnalysisProcess


class PreAnalysisProcessHandSerializersUpdate(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(allow_blank=True)
    desc = serializers.CharField(source='description',allow_null=True,default=True)
    status = serializers.IntegerField(source='state',allow_null=True,default=True)
    analysis_proc_id = serializers.PrimaryKeyRelatedField(source='p_ana_pro',allow_null=True,default=None,
                                                          queryset=models.PropAnalysisProcess.objects.all())
    pre_proc_id = serializers.PrimaryKeyRelatedField(source='p_pre_pro',allow_null=True,default=None,
                                                     queryset=models.PropPreProcess.objects.all())
    own_id = serializers.PrimaryKeyRelatedField(source='owner_id', write_only=True,
                                                queryset=models.UserName.objects.all())
    prop_material = serializers.IntegerField(allow_null=True, default=None, write_only=True)
    edit_date = serializers.DateField(source='edit_time',read_only=True)
    add_date = serializers.DateField(source='add_time',read_only=True)
    material_id = serializers.IntegerField(read_only=True)
    property_id = serializers.IntegerField(read_only=True)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.state = validated_data.get('state', instance.state)
        instance.prop_material = validated_data.get('prop_material', instance.prop_material)
        instance.p_ana_pro = validated_data.get('p_ana_pro', instance.p_ana_pro)
        instance.p_pre_pro = validated_data.get('p_pre_pro', instance.p_pre_pro)
        instance.owner_id = validated_data.get('owner_id', instance.owner_id)
        instance.save()
        return instance

