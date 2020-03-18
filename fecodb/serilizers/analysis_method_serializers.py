from rest_framework import serializers
from fecodb import  models

class AnalysisMethodSerializers(serializers.ModelSerializer):
    desc = serializers.CharField(source='description')
    status = serializers.IntegerField(source='state')
    params = serializers.CharField(source='def_conf_para')
    class Meta:
        model = models.AnalysisMethod
        fields = ('id','name','desc','input','output','params','status')