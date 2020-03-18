from rest_framework import serializers
from fecodb import models

class PropAnalysisMethodSerializers(serializers.ModelSerializer):
    desc = serializers.CharField(source='description')
    params = serializers.CharField(source='conf_para')
    edit_date = serializers.DateField(source='edit_time')
    add_date = serializers.DateField(source='add_time')
    priority = serializers.IntegerField(source='order')
    analysis_method_id = serializers.PrimaryKeyRelatedField(source='ana_treat', read_only=True)
    material_id = serializers.PrimaryKeyRelatedField(source='prop_material.material.id', read_only=True)
    property_id = serializers.PrimaryKeyRelatedField(source='prop_material.property.id',read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(source='ana_process.owner.id', read_only=True)
    status = serializers.IntegerField(source='ana_process.state')

    class Meta:
        model = models.PropPreMethod
        fields = ('id','name','desc','params','edit_date','add_date','analysis_method_id','priority',
                  'material_id','property_id','owner_id','status')


class PropAnalysisMethodSerializersAdd(serializers.ModelSerializer):
    name = serializers.CharField(default='')
    desc = serializers.CharField(source='description', allow_null=True)
    params = serializers.CharField(source='conf_para', allow_null=True)
    edit_date = serializers.DateField(source='edit_time', read_only=True)
    add_date = serializers.DateField(source='add_time', read_only=True)
    priority = serializers.IntegerField(source='order')
    analysis_method_id = serializers.PrimaryKeyRelatedField(source='ana_treat',
                                                            queryset=models.AnalysisMethod.objects.all())
    material_id = serializers.PrimaryKeyRelatedField(source='prop_material.material.id', read_only=True)
    property_id = serializers.PrimaryKeyRelatedField(source='prop_material.property.id', read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(source='ana_process.owner.id', read_only=True)
    status = serializers.PrimaryKeyRelatedField(source='ana_process.state', read_only=True)
    analysis_process_id = serializers.PrimaryKeyRelatedField(source='ana_process',
                                                             queryset=models.PropAnalysisProcess.objects.all())

    def create(self, validated_data):
        name = validated_data['name']
        desc = validated_data['description']
        params = validated_data['conf_para']
        analysis_method_id = validated_data['ana_treat']
        prop_material = validated_data['prop_material']
        priority = validated_data['order']
        analysis_process_id = validated_data['ana_process']
        PropAnalysisMethod = models.PropAnalysisMethod(name=name, description=desc, conf_para=params, order=priority,
                                                     ana_treat=analysis_method_id, prop_material=prop_material,
                                                       ana_process = analysis_process_id)
        PropAnalysisMethod.save()
        return PropAnalysisMethod

    class Meta:
        model = models.PropAnalysisMethod
        fields = ('id', 'name', 'desc', 'params',  'analysis_method_id', 'prop_material','edit_date','add_date',
                  'material_id', 'property_id', 'owner_id', 'status','priority','analysis_process_id')


class PropAnalysisMethodSerializersUpdate(serializers.ModelSerializer):
    name = serializers.CharField(default='')
    desc = serializers.CharField(source='description', allow_null=True, default=None)
    params = serializers.CharField(source='conf_para', allow_null=True, default=None)
    edit_date = serializers.DateField(source='edit_time', read_only=True)
    add_date = serializers.DateField(source='add_time', read_only=True)
    priority = serializers.IntegerField(source='order')
    analysis_method_id = serializers.PrimaryKeyRelatedField(source='ana_treat',
                                                      queryset=models.AnalysisMethod.objects.all(),
                                                      allow_null=True, default=None)
    material_id = serializers.PrimaryKeyRelatedField(source='prop_material.material.id', read_only=True)
    property_id = serializers.PrimaryKeyRelatedField(source='prop_material.property.id', read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(source='ana_process.owner.id', read_only=True)
    status = serializers.PrimaryKeyRelatedField(source='ana_process.state', read_only=True)
    analysis_process_id = serializers.PrimaryKeyRelatedField(source='ana_process',
                                                             queryset=models.PropAnalysisProcess.objects.all())

    def update(self, instance, validated_data):
        print('update', type(instance), instance, validated_data)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.conf_para = validated_data.get('conf_para', instance.conf_para)
        instance.ana_treat = validated_data.get('ana_treat', instance.ana_treat)
        instance.prop_material = validated_data.get('prop_material', instance.prop_material)
        instance.order = validated_data.get('order', instance.order)
        instance.ana_process = validated_data.get('ana_process', instance.ana_process)
        instance.save()
        return instance


    class Meta:
        model = models.PropAnalysisMethod
        fields = ('id', 'name', 'desc', 'params', 'analysis_method_id', 'prop_material','edit_date','add_date',
                  'material_id', 'property_id', 'owner_id', 'status','priority','analysis_process_id')