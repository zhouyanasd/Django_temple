from rest_framework import serializers
from fecodb import models

class PropPreMethodSerializers(serializers.ModelSerializer):
    desc = serializers.CharField(source='description')
    params = serializers.CharField(source='conf_para')
    edit_date = serializers.DateField(source='edit_time',read_only=True)
    add_date = serializers.DateField(source='add_time', read_only=True)
    priority = serializers.IntegerField( source='order')
    pre_treat_id = serializers.PrimaryKeyRelatedField(source='pre_treat', read_only=True)
    material_id = serializers.PrimaryKeyRelatedField(source='prop_material.material.id', read_only=True)
    property_id = serializers.PrimaryKeyRelatedField(source='prop_material.property.id',read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(source='pre_process.owner.id', read_only=True)
    status = serializers.IntegerField(source='pre_process.state')
    pre_process_id = serializers.PrimaryKeyRelatedField(source='pre_process.id', read_only=True)

    class Meta:
        model = models.PropPreMethod
        fields = ('id','name','desc','params','edit_date','add_date','pre_treat_id','priority',
                  'material_id','property_id','owner_id','status','pre_process_id')


class PropPreMethodSerializersAdd(serializers.ModelSerializer):
    name = serializers.CharField(default='')
    desc = serializers.CharField(source='description', allow_null=True)
    params = serializers.CharField(source='conf_para', allow_null=True)
    edit_date = serializers.DateField(source='edit_time', read_only=True)
    add_date = serializers.DateField(source='add_time', read_only=True)
    priority = serializers.IntegerField( source='order')
    pre_treat_id = serializers.PrimaryKeyRelatedField(source='pre_treat', queryset=models.PreTreatmentMethod.objects.all())
    material_id = serializers.PrimaryKeyRelatedField(source='prop_material.material.id', read_only=True)
    property_id = serializers.PrimaryKeyRelatedField(source='prop_material.property.id',read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(source='pre_process.owner.id', read_only=True)
    status = serializers.PrimaryKeyRelatedField(source='pre_process.state', read_only=True)
    pre_process_id = serializers.PrimaryKeyRelatedField(source='pre_process', queryset=models.PropPreProcess.objects.all())

    def create(self, validated_data):
        name = validated_data['name']
        desc = validated_data['description']
        params = validated_data['conf_para']
        pre_treat_id = validated_data['pre_treat']
        prop_material = validated_data['prop_material']
        priority = validated_data['order']
        pre_process_id =validated_data['pre_process']
        PropPreMethod = models.PropPreMethod(name=name, description=desc, conf_para=params, pre_treat = pre_treat_id,
                                             prop_material=prop_material, pre_process=pre_process_id, order=priority)
        PropPreMethod.save()
        return PropPreMethod

    class Meta:
        model = models.PropPreMethod
        fields = ('id', 'name', 'desc', 'params',  'pre_treat_id', 'priority', 'prop_material','edit_date','add_date',
                  'material_id', 'property_id', 'owner_id', 'status','pre_process_id')


class PropPreMethodSerializersUpdate(serializers.ModelSerializer):
    name = serializers.CharField(default='')
    desc = serializers.CharField(source='description', allow_null=True, default=None)
    params = serializers.CharField(source='conf_para', allow_null=True, default=None)
    edit_date = serializers.DateField(source='edit_time', read_only=True)
    add_date = serializers.DateField(source='add_time', read_only=True)
    priority = serializers.IntegerField(source='order')
    pre_treat_id = serializers.PrimaryKeyRelatedField(source='pre_treat',
                                                      queryset=models.PreTreatmentMethod.objects.all(),
                                                      allow_null=True, default=None)
    material_id = serializers.PrimaryKeyRelatedField(source='prop_material.material.id', read_only=True)
    property_id = serializers.PrimaryKeyRelatedField(source='prop_material.property.id', read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(source='pre_process.owner.id', read_only=True)
    status = serializers.PrimaryKeyRelatedField(source='pre_process.state', read_only=True)
    pre_process_id = serializers.PrimaryKeyRelatedField(source='pre_process',
                                                        queryset=models.PropPreProcess.objects.all(),
                                                        allow_null=True, default=None)

    def update(self, instance, validated_data):
        print('update', type(instance), instance, validated_data)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.conf_para = validated_data.get('conf_para', instance.conf_para)
        instance.pre_treat = validated_data.get('pre_treat', instance.pre_treat)
        instance.prop_material = validated_data.get('prop_material', instance.prop_material)
        instance.order = validated_data.get('order', instance.order)
        instance.pre_process = validated_data.get('pre_process', instance.pre_process)
        instance.save()
        return instance


    class Meta:
        model = models.PropPreMethod
        fields = ('id', 'name', 'desc', 'params',  'pre_treat_id', 'priority', 'prop_material','edit_date','add_date',
                  'material_id', 'property_id', 'owner_id', 'status','pre_process_id')