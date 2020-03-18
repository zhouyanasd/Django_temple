# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AnalysisMethod(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    def_conf_para = models.TextField(db_column='DEF_CONF_PARA', blank=True, null=True)  # Field name made lowercase.
    def_conf_stru = models.TextField(db_column='DEF_CONF_STRU', blank=True, null=True)  # Field name made lowercase.
    input = models.TextField(db_column='INPUT', blank=True, null=True)  # Field name made lowercase.
    output = models.TextField(db_column='OUTPUT', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'analysis_method'


class AnalysisProps(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    value = models.FloatField(db_column='VALUE', blank=True, null=True)  # Field name made lowercase.
    analysis_time = models.DateField(db_column='ANALYSIS_TIME', blank=True, null=True)  # Field name made lowercase.
    nmr_id = models.ForeignKey('Nmr',models.DO_NOTHING, db_column='NMR_ID', blank=True, null=True)  # Field name made lowercase.
    pre_ana = models.ForeignKey('PreAnalysisProcess', models.DO_NOTHING, db_column='PRE_ANA_ID', blank=True, null=True)  # Field name made lowercase.
    prop_material = models.ForeignKey('NmrMaterialProp', models.DO_NOTHING, related_name= 'nmr', db_column='PROP_NAME_ID', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    add_time = models.DateField(db_column='ADD_TIME', blank=True, null=True,auto_now_add=True)  # Field name made lowercase.
    edit_time = models.DateField(db_column='EDIT_TIME', blank=True, null=True,auto_now=True)  # Field name made lowercase.
    owner = models.ForeignKey('UserName', models.DO_NOTHING, db_column='OWNER_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'analysis_props'


class AssayProps(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    value = models.FloatField(db_column='VALUE', blank=True, null=True)  # Field name made lowercase.
    assay_time = models.DateField(db_column='ASSAY_TIME', blank=True, null=True)  # Field name made lowercase.
    nmr_id = models.ForeignKey('Nmr', models.DO_NOTHING, db_column='NMR_ID', blank=True, null=True)  # Field name made lowercase.
    prop_name = models.ForeignKey('NmrMaterialProp', models.DO_NOTHING, db_column='PROP_NAME_ID', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    add_time = models.DateField(db_column='ADD_TIME', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    edit_time = models.DateField(db_column='EDIT_TIME', blank=True, null=True, auto_now=True)  # Field name made lowercase.
    owner = models.ForeignKey('UserName', models.DO_NOTHING, db_column='OWNER_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assay_props'


class Authority(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'authority'


class Log(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    creat_time = models.DateField(db_column='CREAT_TIME', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey('UserName', models.DO_NOTHING, db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    operater_type = models.CharField(db_column='OPERATER_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    params = models.TextField(db_column='PARAMS', blank=True, null=True)  # Field name made lowercase.
    src = models.CharField(db_column='SRC', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log'


class Nmr(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sample_time = models.DateField(db_column='SAMPLE_TIME', blank=True, null=True)  # Field name made lowercase.
    import_time = models.DateField(db_column='IMPORT_TIME', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    location = models.ForeignKey('NmrLocation', models.DO_NOTHING, db_column='LOCATION_ID', blank=True, null=True)  # Field name made lowercase.
    material = models.ForeignKey('NmrMaterial', models.DO_NOTHING, db_column='MATERIAL_ID', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    edit_time = models.DateField(db_column='EDIT_TIME', blank=True, null=True, auto_now=True)  # Field name made lowercase.
    owner = models.ForeignKey('UserName', models.DO_NOTHING, db_column='OWNER_ID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='VALUE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_evaluate = models.IntegerField(db_column='IS_EVALUATE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nmr'


class NmrLocation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateField(db_column='ADDTIME', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    edittime = models.DateField(db_column='EDITTIME', blank=True, null=True, auto_now=True)  # Field name made lowercase.
    material_id = models.ManyToManyField('NmrMaterial', through='NmrLocationMaterial', related_name='location')

    class Meta:
        managed = False
        db_table = 'nmr_location'


class NmrLocationMaterial(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    location = models.ForeignKey('NmrLocation', models.DO_NOTHING,related_name='location_material', db_column='LOCATION_ID', blank=True, null=True)  # Field name made lowercase.
    material = models.ForeignKey('NmrMaterial', models.DO_NOTHING,related_name='location_material', db_column='MATERIAL_ID', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nmr_location_material'


class NmrMaterialProp(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    property = models.ForeignKey('PropName',models.DO_NOTHING, related_name='property_material', db_column='PROPERTY_ID', blank=True, null=True)  # Field name made lowercase.
    material = models.ForeignKey('NmrMaterial', models.DO_NOTHING, related_name='property_material', db_column='MATERIAL_ID', blank=True, null=True)  # Field name made lowercase.
    conf_id = models.IntegerField(db_column='DEF_CONF_ID', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nmr_material_prop'


class NmrMaterial(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateField(db_column='ADDTIME', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    edittime = models.DateField(db_column='EDITTIME', blank=True, null=True, auto_now=True)  # Field name made lowercase.
    location_id = models.ManyToManyField('NmrLocation',through='NmrLocationMaterial')
    property_id = models.ManyToManyField('PropName', through='NmrMaterialProp')

    class Meta:
        managed = False
        db_table = 'nmr_material'


class PreAnalysisProcess(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    owner_id = models.ForeignKey('UserName', models.DO_NOTHING, db_column='OWNERID', blank=True, null=True)  # Field name made lowercase.
    add_time = models.DateField(db_column='ADD_TIME', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    edit_time = models.DateField(db_column='EDIT_TIME', blank=True, null=True, auto_now=True)  # Field name made lowercase.
    p_pre_pro = models.ForeignKey('PropPreProcess', models.DO_NOTHING, db_column='P_PRE_PRO_ID', blank=True, null=True)  # Field name made lowercase.
    p_ana_pro = models.ForeignKey('PropAnalysisProcess', models.DO_NOTHING, db_column='P_ANA_PRO_ID', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    prop_material = models.IntegerField(db_column='PROP_NAME_ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_analysis_process'


class PreTreatmentMethod(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    input = models.TextField(db_column='INPUT', blank=True, null=True)  # Field name made lowercase.
    output = models.TextField(db_column='OUTPUT', blank=True, null=True)  # Field name made lowercase.
    def_conf_para = models.TextField(db_column='DEF_CONF_PARA', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='PRIORITY', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_treatment_method'


class PropAnalysisMethod(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    prop_material = models.ForeignKey('NmrMaterialProp', models.DO_NOTHING, db_column='PROP_NAME_ID', blank=True, null=True)  # Field name made lowercase.
    ana_treat = models.ForeignKey('AnalysisMethod', models.DO_NOTHING, db_column='ANA_TREAT_ID', blank=True, null=True)  # Field name made lowercase.
    conf_para = models.TextField(db_column='CONF_PARA', blank=True, null=True)  # Field name made lowercase.
    add_time = models.DateField(db_column='ADD_TIME', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    edit_time = models.DateField(db_column='EDIT_TIME', blank=True, null=True, auto_now=True)  # Field name made lowercase.
    ana_process = models.ForeignKey('PropAnalysisProcess', models.DO_NOTHING, related_name='property_material',db_column='ANA_PROCESS_ID', blank=True, null=True)  # Field name made lowercase.
    order = models.IntegerField(db_column='ORDER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prop_analysis_method'


class PropAnalysisProcess(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    add_time = models.DateField(db_column='ADD_TIME', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    edit_time = models.DateField(db_column='EDIT_TIME', blank=True, null=True, auto_now=True)  # Field name made lowercase.
    owner = models.ForeignKey('UserName', models.DO_NOTHING, db_column='OWNER_ID', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prop_analysis_process'


class PropName(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    error = models.CharField(db_column='ERROR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    range = models.CharField(db_column='RANGE', max_length=255, blank=True, null=True)
    material_id = models.ManyToManyField('NmrMaterial',through='NmrMaterialProp')

    class Meta:
        managed = False
        db_table = 'prop_name'


class PropPreMethod(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    prop_material = models.ForeignKey('NmrMaterialProp', models.DO_NOTHING, db_column='PROP_NAME_ID', blank=True, null=True)  # Field name made lowercase.
    pre_treat = models.ForeignKey('PreTreatmentMethod', models.DO_NOTHING, db_column='PRE_TREAT_ID', blank=True, null=True)  # Field name made lowercase.
    conf_para = models.TextField(db_column='CONF_PARA', blank=True, null=True)  # Field name made lowercase.
    add_time = models.DateField(db_column='ADD_TIME', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    edit_time = models.DateField(db_column='EDIT_TIME', blank=True, null=True, auto_now=True)  # Field name made lowercase.
    pre_process = models.ForeignKey('PropPreProcess',models.DO_NOTHING, related_name='property_material', db_column='PRE_PROCESS_ID', blank=True, null=True)  # Field name made lowercase.
    order = models.IntegerField(db_column='ORDER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prop_pre_method'


class PropPreProcess(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    add_time = models.DateField(db_column='ADD_TIME', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    edit_time = models.DateField(db_column='EDIT_TIME', blank=True, null=True, auto_now=True)  # Field name made lowercase.
    owner = models.ForeignKey('UserName', models.DO_NOTHING, db_column='OWNER_ID', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='SECTION', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prop_pre_process'


class Role(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'role'


class RoleAuthority(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    auth = models.ForeignKey(Authority, models.DO_NOTHING, db_column='AUTH_ID', blank=True, null=True)  # Field name made lowercase.
    role = models.ForeignKey(Role, models.DO_NOTHING, db_column='ROLE_ID', blank=True, null=True)  # Field name made lowercase.
    access = models.IntegerField(db_column='ACCESS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'role_authority'


class UserName(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_name'


class UserRole(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey(UserName, models.DO_NOTHING, db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    role = models.ForeignKey(Role, models.DO_NOTHING, db_column='ROLE_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_role'
