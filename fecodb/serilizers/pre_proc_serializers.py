from rest_framework import serializers
from fecodb import  models

class PropPreMethodSerializers(serializers.ModelSerializer):
    prop_pre_id = serializers.PrimaryKeyRelatedField(source='id',read_only=True)
    material_id = serializers.PrimaryKeyRelatedField(source='prop_material.material.id', read_only=True)
    property_id = serializers.PrimaryKeyRelatedField(source='prop_material.property.id',read_only=True)
    priority = serializers.IntegerField(source='order')
    pre_treat_id = serializers.PrimaryKeyRelatedField(source='pre_treat',read_only=True)

    class Meta:
        model = models.PropPreMethod
        fields = ('prop_pre_id','material_id','property_id','priority','pre_treat_id','name')


# class PropPreMethodSerializersAdd(serializers.ModelSerializer):
#     desc = serializers.CharField(source='description', allow_null=True)
#     params = serializers.CharField(source='conf_para', allow_null=True)
#     priority = serializers.IntegerField(source='order')
#     pre_treat_id = serializers.PrimaryKeyRelatedField(source='pre_treat',
#                                                       queryset=models.PreTreatmentMethod.objects.all())
#
#     class Meta:
#         model = models.PropPreMethod
#         fields = ('desc','params','priority','pre_treat_id')


class PropPreProcessSerializers(serializers.ModelSerializer):
    property_material = PropPreMethodSerializers(read_only= True,many=True)
    desc = serializers.CharField(source='description')
    status = serializers.IntegerField(source='state')
    own_id = serializers.PrimaryKeyRelatedField(source='owner',read_only=True)
    edit_date=serializers.CharField(source='edit_time')
    add_date=serializers.CharField(source='add_time')

    class Meta:
        model = models.PropPreProcess
        fields = ( 'id','name','desc','own_id','edit_date','add_date','status','property_material','section')


class PropPreProcessSerializersAdd(serializers.ModelSerializer):
    property_material = PropPreMethodSerializers(read_only= True,many=True)
    name = serializers.CharField(allow_blank=True, allow_null=False, default='')
    desc = serializers.CharField(source='description', allow_null=True, default=None)
    status = serializers.IntegerField(source='state', allow_null=True, default=0)
    own_id = serializers.PrimaryKeyRelatedField(source='owner',queryset=models.UserName.objects.all())
    edit_date=serializers.CharField(source='edit_time', read_only=True)
    add_date=serializers.CharField(source='add_time', read_only=True)

    class Meta:
        model = models.PropPreProcess
        fields = ( 'id','name','desc','own_id','edit_date','add_date','status','property_material','section')


# class PropPreProcessSerializersAddPreList(serializers.ModelSerializer):
#     property_material = PropPreMethodSerializersAdd(many=True)
#
#     name = serializers.CharField(allow_blank=True, allow_null=False, default='')
#     desc = serializers.CharField(source='description', allow_null=True, default=None)
#     status = serializers.IntegerField(source='state', allow_null=True, default=0)
#     own_id = serializers.PrimaryKeyRelatedField(source='owner',queryset=models.UserName.objects.all())
#     edit_date=serializers.CharField(source='edit_time', read_only=True)
#     add_date=serializers.CharField(source='add_time', read_only=True)
#
#     def create(self, validated_data):
#         print('create', type(validated_data), validated_data)
#         prop_pre_list = validated_data.pop('property_material')
#         PropPreProcess = models.PropPreProcess.objects.create(**validated_data)
#         for prop_pre in prop_pre_list:
#             print(prop_pre)
#             models.PropPreMethod.objects.create(pre_process=PropPreProcess, **prop_pre)
#         return PropPreProcess
#
#     class Meta:
#         model = models.PropPreProcess
#         fields = ( 'id','name','desc','own_id','edit_date','add_date','status','property_material')


class PropPreProcessSerializersUpdate(serializers.ModelSerializer):
    property_material = PropPreMethodSerializers(read_only= True,many=True)
    name = serializers.CharField(allow_blank=True, allow_null=False, default='')
    desc = serializers.CharField(source='description', allow_null=True, default=None)
    status = serializers.IntegerField(source='state', allow_null=True, default=0)
    own_id = serializers.PrimaryKeyRelatedField(source='owner',queryset=models.UserName.objects.all())
    edit_date=serializers.CharField(source='edit_time', read_only=True)
    add_date=serializers.CharField(source='add_time', read_only=True)

    class Meta:
        model = models.PropPreProcess
        fields = ( 'id','name','desc','own_id','edit_date','add_date','status','property_material','section')

