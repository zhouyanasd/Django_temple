from rest_framework import serializers
from fecodb import  models


class PropAnalysisMethodSerializers(serializers.ModelSerializer):
    prop_analysis_id = serializers.PrimaryKeyRelatedField(source='id',read_only=True)
    material_id = serializers.PrimaryKeyRelatedField(source='prop_material.material.id', read_only=True)
    property_id = serializers.PrimaryKeyRelatedField(source='prop_material.property.id',read_only=True)
    priority = serializers.IntegerField(source='order')
    analysis_method_id = serializers.PrimaryKeyRelatedField(source='ana_treat', read_only=True)

    class Meta:
        model = models.PropAnalysisMethod
        fields = ('prop_analysis_id','material_id','property_id','priority','analysis_method_id')

class PropAnalysisProcessSerializers(serializers.ModelSerializer):
    property_material = PropAnalysisMethodSerializers(read_only=True, many=True)
    desc = serializers.CharField(source='description')
    status = serializers.IntegerField(source='state')
    own_id = serializers.PrimaryKeyRelatedField(source='owner', read_only=True)
    edit_date=serializers.CharField(source='edit_time')
    add_date=serializers.CharField(source='add_time')

    class Meta:
        model = models.PropAnalysisMethod
        fields = ('id','name','desc','own_id','edit_date','add_date','status','property_material')

class PropAnalysisProcessSerializersAdd(serializers.ModelSerializer):
    property_material = PropAnalysisMethodSerializers(read_only= True,many=True)
    name = serializers.CharField(allow_blank=True, allow_null=False, default='')
    desc = serializers.CharField(source='description', allow_null=True, default=None)
    status = serializers.IntegerField(source='state', allow_null=True, default=0)
    own_id = serializers.PrimaryKeyRelatedField(source='owner',queryset=models.UserName.objects.all())
    edit_date=serializers.CharField(source='edit_time', read_only=True)
    add_date=serializers.CharField(source='add_time', read_only=True)

    class Meta:
        model = models.PropAnalysisProcess
        fields = ( 'id','name','desc','own_id','edit_date','add_date','status','property_material')


class PropAnalysisProcessSerializersUpdate(serializers.ModelSerializer):
    property_material = PropAnalysisMethodSerializers(read_only= True,many=True)
    name = serializers.CharField(allow_blank=True, allow_null=False, default='')
    desc = serializers.CharField(source='description', allow_null=True, default=None)
    status = serializers.IntegerField(source='state', allow_null=True, default=0)
    own_id = serializers.PrimaryKeyRelatedField(source='owner',queryset=models.UserName.objects.all())
    edit_date=serializers.CharField(source='edit_time', read_only=True)
    add_date=serializers.CharField(source='add_time', read_only=True)

    class Meta:
        model = models.PropAnalysisProcess
        fields = ( 'id','name','desc','own_id','edit_date','add_date','status','property_material')