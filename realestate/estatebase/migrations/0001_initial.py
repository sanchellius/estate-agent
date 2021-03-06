# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('estatebase_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('estatebase', ['UserProfile'])

        # Adding M2M table for field geo_groups on 'UserProfile'
        db.create_table('estatebase_userprofile_geo_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['estatebase.userprofile'], null=False)),
            ('geogroup', models.ForeignKey(orm['estatebase.geogroup'], null=False))
        ))
        db.create_unique('estatebase_userprofile_geo_groups', ['userprofile_id', 'geogroup_id'])

        # Adding model 'GeoGroup'
        db.create_table('estatebase_geogroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['GeoGroup'])

        # Adding model 'Region'
        db.create_table('estatebase_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
            ('geo_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.GeoGroup'], on_delete=models.PROTECT)),
        ))
        db.send_create_signal('estatebase', ['Region'])

        # Adding model 'Locality'
        db.create_table('estatebase_locality', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Region'], null=True, on_delete=models.PROTECT, blank=True)),
        ))
        db.send_create_signal('estatebase', ['Locality'])

        # Adding unique constraint on 'Locality', fields ['name', 'region']
        db.create_unique('estatebase_locality', ['name', 'region_id'])

        # Adding model 'Microdistrict'
        db.create_table('estatebase_microdistrict', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
            ('locality', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Locality'], on_delete=models.PROTECT)),
        ))
        db.send_create_signal('estatebase', ['Microdistrict'])

        # Adding model 'Street'
        db.create_table('estatebase_street', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
            ('locality', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Locality'], on_delete=models.PROTECT)),
        ))
        db.send_create_signal('estatebase', ['Street'])

        # Adding model 'Beside'
        db.create_table('estatebase_beside', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Beside'])

        # Adding model 'Electricity'
        db.create_table('estatebase_electricity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Electricity'])

        # Adding model 'Watersupply'
        db.create_table('estatebase_watersupply', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Watersupply'])

        # Adding model 'Gassupply'
        db.create_table('estatebase_gassupply', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Gassupply'])

        # Adding model 'Sewerage'
        db.create_table('estatebase_sewerage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Sewerage'])

        # Adding model 'Telephony'
        db.create_table('estatebase_telephony', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Telephony'])

        # Adding model 'Internet'
        db.create_table('estatebase_internet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Internet'])

        # Adding model 'Driveway'
        db.create_table('estatebase_driveway', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Driveway'])

        # Adding model 'Document'
        db.create_table('estatebase_document', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Document'])

        # Adding M2M table for field estate_type on 'Document'
        db.create_table('estatebase_document_estate_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('document', models.ForeignKey(orm['estatebase.document'], null=False)),
            ('estatetype', models.ForeignKey(orm['estatebase.estatetype'], null=False))
        ))
        db.create_unique('estatebase_document_estate_type', ['document_id', 'estatetype_id'])

        # Adding model 'EstateParam'
        db.create_table('estatebase_estateparam', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('estatebase', ['EstateParam'])

        # Adding model 'EstateStatus'
        db.create_table('estatebase_estatestatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['EstateStatus'])

        # Adding model 'EstateClientStatus'
        db.create_table('estatebase_estateclientstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['EstateClientStatus'])

        # Adding model 'EstateTypeCategory'
        db.create_table('estatebase_estatetypecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('estatebase', ['EstateTypeCategory'])

        # Adding model 'EstateType'
        db.create_table('estatebase_estatetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('estate_type_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.EstateTypeCategory'], on_delete=models.PROTECT)),
            ('object_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('template', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('placeable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('estatebase', ['EstateType'])

        # Adding model 'HistoryMeta'
        db.create_table('estatebase_historymeta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='creators', on_delete=models.PROTECT, to=orm['auth.User'])),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updators', null=True, on_delete=models.PROTECT, to=orm['auth.User'])),
            ('modificated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('estatebase', ['HistoryMeta'])

        # Adding model 'EstateClient'
        db.create_table('estatebase_estateclient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Client'])),
            ('estate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Estate'])),
            ('estate_client_status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.EstateClientStatus'])),
        ))
        db.send_create_signal('estatebase', ['EstateClient'])

        # Adding model 'Estate'
        db.create_table('estatebase_estate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('estate_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.EstateType'], on_delete=models.PROTECT)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Region'], on_delete=models.PROTECT)),
            ('locality', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Locality'], null=True, on_delete=models.PROTECT, blank=True)),
            ('microdistrict', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Microdistrict'], null=True, on_delete=models.PROTECT, blank=True)),
            ('street', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Street'], null=True, on_delete=models.PROTECT, blank=True)),
            ('estate_number', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Origin'], null=True, on_delete=models.PROTECT, blank=True)),
            ('beside', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Beside'], null=True, on_delete=models.PROTECT, blank=True)),
            ('beside_distance', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('saler_price', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('agency_price', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('estate_status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.EstateStatus'], on_delete=models.PROTECT)),
            ('electricity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Electricity'], null=True, on_delete=models.PROTECT, blank=True)),
            ('electricity_distance', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('watersupply', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Watersupply'], null=True, on_delete=models.PROTECT, blank=True)),
            ('watersupply_distance', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('gassupply', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Gassupply'], null=True, on_delete=models.PROTECT, blank=True)),
            ('gassupply_distance', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('sewerage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Sewerage'], null=True, on_delete=models.PROTECT, blank=True)),
            ('sewerage_distance', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('telephony', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Telephony'], null=True, on_delete=models.PROTECT, blank=True)),
            ('internet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Internet'], null=True, on_delete=models.PROTECT, blank=True)),
            ('driveway', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Driveway'], null=True, on_delete=models.PROTECT, blank=True)),
            ('driveway_distance', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=255, null=True, blank=True)),
            ('history', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['estatebase.HistoryMeta'], unique=True, null=True, blank=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Contact'], null=True, on_delete=models.PROTECT, blank=True)),
            ('valid', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('estatebase', ['Estate'])

        # Adding M2M table for field estate_params on 'Estate'
        db.create_table('estatebase_estate_estate_params', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('estate', models.ForeignKey(orm['estatebase.estate'], null=False)),
            ('estateparam', models.ForeignKey(orm['estatebase.estateparam'], null=False))
        ))
        db.create_unique('estatebase_estate_estate_params', ['estate_id', 'estateparam_id'])

        # Adding model 'EstatePhoto'
        db.create_table('estatebase_estatephoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, blank=True)),
            ('estate', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['estatebase.Estate'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        ))
        db.send_create_signal('estatebase', ['EstatePhoto'])

        # Adding model 'WallConstrucion'
        db.create_table('estatebase_wallconstrucion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['WallConstrucion'])

        # Adding model 'ExteriorFinish'
        db.create_table('estatebase_exteriorfinish', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['ExteriorFinish'])

        # Adding model 'WindowType'
        db.create_table('estatebase_windowtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['WindowType'])

        # Adding model 'Roof'
        db.create_table('estatebase_roof', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Roof'])

        # Adding model 'Heating'
        db.create_table('estatebase_heating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Heating'])

        # Adding model 'WallFinish'
        db.create_table('estatebase_wallfinish', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['WallFinish'])

        # Adding model 'Flooring'
        db.create_table('estatebase_flooring', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Flooring'])

        # Adding model 'Ceiling'
        db.create_table('estatebase_ceiling', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Ceiling'])

        # Adding model 'Interior'
        db.create_table('estatebase_interior', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Interior'])

        # Adding model 'LevelName'
        db.create_table('estatebase_levelname', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['LevelName'])

        # Adding model 'Level'
        db.create_table('estatebase_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.LevelName'])),
            ('bidg', self.gf('django.db.models.fields.related.ForeignKey')(related_name='levels', to=orm['estatebase.Bidg'])),
        ))
        db.send_create_signal('estatebase', ['Level'])

        # Adding model 'LayoutType'
        db.create_table('estatebase_layouttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['LayoutType'])

        # Adding model 'Furniture'
        db.create_table('estatebase_furniture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Furniture'])

        # Adding model 'LayoutFeature'
        db.create_table('estatebase_layoutfeature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['LayoutFeature'])

        # Adding model 'Layout'
        db.create_table('estatebase_layout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Level'])),
            ('layout_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.LayoutType'], on_delete=models.PROTECT)),
            ('area', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('furniture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Furniture'], null=True, on_delete=models.PROTECT, blank=True)),
            ('layout_feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.LayoutFeature'], null=True, on_delete=models.PROTECT, blank=True)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('estatebase', ['Layout'])

        # Adding model 'Bidg'
        db.create_table('estatebase_bidg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estate', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bidgs', to=orm['estatebase.Estate'])),
            ('estate_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.EstateType'], on_delete=models.PROTECT)),
            ('room_number', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('year_built', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('floor', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('floor_count', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('elevator', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wall_construcion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.WallConstrucion'], null=True, on_delete=models.PROTECT, blank=True)),
            ('exterior_finish', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.ExteriorFinish'], null=True, on_delete=models.PROTECT, blank=True)),
            ('window_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.WindowType'], null=True, on_delete=models.PROTECT, blank=True)),
            ('roof', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Roof'], null=True, on_delete=models.PROTECT, blank=True)),
            ('heating', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Heating'], null=True, on_delete=models.PROTECT, blank=True)),
            ('ceiling_height', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('room_count', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('total_area', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('used_area', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('wall_finish', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.WallFinish'], null=True, on_delete=models.PROTECT, blank=True)),
            ('flooring', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Flooring'], null=True, on_delete=models.PROTECT, blank=True)),
            ('ceiling', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Ceiling'], null=True, on_delete=models.PROTECT, blank=True)),
            ('interior', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Interior'], null=True, on_delete=models.PROTECT, blank=True)),
            ('basic', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('estatebase', ['Bidg'])

        # Adding M2M table for field documents on 'Bidg'
        db.create_table('estatebase_bidg_documents', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bidg', models.ForeignKey(orm['estatebase.bidg'], null=False)),
            ('document', models.ForeignKey(orm['estatebase.document'], null=False))
        ))
        db.create_unique('estatebase_bidg_documents', ['bidg_id', 'document_id'])

        # Adding model 'Shape'
        db.create_table('estatebase_shape', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Shape'])

        # Adding model 'LandType'
        db.create_table('estatebase_landtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['LandType'])

        # Adding model 'Purpose'
        db.create_table('estatebase_purpose', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Purpose'])

        # Adding model 'Stead'
        db.create_table('estatebase_stead', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estate', self.gf('django.db.models.fields.related.OneToOneField')(related_name='stead', unique=True, to=orm['estatebase.Estate'])),
            ('total_area', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('face_area', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('shape', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Shape'], null=True, on_delete=models.PROTECT, blank=True)),
            ('land_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.LandType'], null=True, on_delete=models.PROTECT, blank=True)),
            ('purpose', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Purpose'], null=True, on_delete=models.PROTECT, blank=True)),
        ))
        db.send_create_signal('estatebase', ['Stead'])

        # Adding model 'ClientType'
        db.create_table('estatebase_clienttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['ClientType'])

        # Adding model 'Origin'
        db.create_table('estatebase_origin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['Origin'])

        # Adding model 'Client'
        db.create_table('estatebase_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('client_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.ClientType'], on_delete=models.PROTECT)),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Origin'], null=True, on_delete=models.PROTECT, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('history', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['estatebase.HistoryMeta'], unique=True, null=True, blank=True)),
            ('broker', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='clientbrokers', null=True, on_delete=models.PROTECT, to=orm['auth.User'])),
        ))
        db.send_create_signal('estatebase', ['Client'])

        # Adding model 'ContactType'
        db.create_table('estatebase_contacttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['ContactType'])

        # Adding model 'ContactState'
        db.create_table('estatebase_contactstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('estatebase', ['ContactState'])

        # Adding model 'ContactHistory'
        db.create_table('estatebase_contacthistory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 1, 0, 0))),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.PROTECT, blank=True)),
            ('contact_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.ContactState'], on_delete=models.PROTECT)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.Contact'])),
        ))
        db.send_create_signal('estatebase', ['ContactHistory'])

        # Adding model 'Contact'
        db.create_table('estatebase_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contacts', to=orm['estatebase.Client'])),
            ('contact_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estatebase.ContactType'], on_delete=models.PROTECT)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('contact_state', self.gf('django.db.models.fields.related.ForeignKey')(default=5, to=orm['estatebase.ContactState'], on_delete=models.PROTECT)),
        ))
        db.send_create_signal('estatebase', ['Contact'])

        # Adding model 'Bid'
        db.create_table('estatebase_bid', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bids', to=orm['estatebase.Client'])),
            ('estate_filter', self.gf('picklefield.fields.PickledObjectField')(null=True, blank=True)),
            ('history', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['estatebase.HistoryMeta'], unique=True, null=True, blank=True)),
            ('broker', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='brokers', null=True, on_delete=models.PROTECT, to=orm['auth.User'])),
            ('agency_price_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('agency_price_max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('estatebase', ['Bid'])

        # Adding M2M table for field estates on 'Bid'
        db.create_table('estatebase_bid_estates', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bid', models.ForeignKey(orm['estatebase.bid'], null=False)),
            ('estate', models.ForeignKey(orm['estatebase.estate'], null=False))
        ))
        db.create_unique('estatebase_bid_estates', ['bid_id', 'estate_id'])

        # Adding M2M table for field estate_types on 'Bid'
        db.create_table('estatebase_bid_estate_types', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bid', models.ForeignKey(orm['estatebase.bid'], null=False)),
            ('estatetype', models.ForeignKey(orm['estatebase.estatetype'], null=False))
        ))
        db.create_unique('estatebase_bid_estate_types', ['bid_id', 'estatetype_id'])

        # Adding M2M table for field regions on 'Bid'
        db.create_table('estatebase_bid_regions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bid', models.ForeignKey(orm['estatebase.bid'], null=False)),
            ('region', models.ForeignKey(orm['estatebase.region'], null=False))
        ))
        db.create_unique('estatebase_bid_regions', ['bid_id', 'region_id'])

        # Adding M2M table for field localities on 'Bid'
        db.create_table('estatebase_bid_localities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bid', models.ForeignKey(orm['estatebase.bid'], null=False)),
            ('locality', models.ForeignKey(orm['estatebase.locality'], null=False))
        ))
        db.create_unique('estatebase_bid_localities', ['bid_id', 'locality_id'])

        # Adding model 'EstateRegister'
        db.create_table('estatebase_estateregister', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('history', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['estatebase.HistoryMeta'], unique=True, null=True, blank=True)),
            ('broker', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='estate_registers', null=True, on_delete=models.PROTECT, to=orm['auth.User'])),
        ))
        db.send_create_signal('estatebase', ['EstateRegister'])

        # Adding M2M table for field estates on 'EstateRegister'
        db.create_table('estatebase_estateregister_estates', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('estateregister', models.ForeignKey(orm['estatebase.estateregister'], null=False)),
            ('estate', models.ForeignKey(orm['estatebase.estate'], null=False))
        ))
        db.create_unique('estatebase_estateregister_estates', ['estateregister_id', 'estate_id'])

        # Adding M2M table for field bids on 'EstateRegister'
        db.create_table('estatebase_estateregister_bids', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('estateregister', models.ForeignKey(orm['estatebase.estateregister'], null=False)),
            ('bid', models.ForeignKey(orm['estatebase.bid'], null=False))
        ))
        db.create_unique('estatebase_estateregister_bids', ['estateregister_id', 'bid_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Locality', fields ['name', 'region']
        db.delete_unique('estatebase_locality', ['name', 'region_id'])

        # Deleting model 'UserProfile'
        db.delete_table('estatebase_userprofile')

        # Removing M2M table for field geo_groups on 'UserProfile'
        db.delete_table('estatebase_userprofile_geo_groups')

        # Deleting model 'GeoGroup'
        db.delete_table('estatebase_geogroup')

        # Deleting model 'Region'
        db.delete_table('estatebase_region')

        # Deleting model 'Locality'
        db.delete_table('estatebase_locality')

        # Deleting model 'Microdistrict'
        db.delete_table('estatebase_microdistrict')

        # Deleting model 'Street'
        db.delete_table('estatebase_street')

        # Deleting model 'Beside'
        db.delete_table('estatebase_beside')

        # Deleting model 'Electricity'
        db.delete_table('estatebase_electricity')

        # Deleting model 'Watersupply'
        db.delete_table('estatebase_watersupply')

        # Deleting model 'Gassupply'
        db.delete_table('estatebase_gassupply')

        # Deleting model 'Sewerage'
        db.delete_table('estatebase_sewerage')

        # Deleting model 'Telephony'
        db.delete_table('estatebase_telephony')

        # Deleting model 'Internet'
        db.delete_table('estatebase_internet')

        # Deleting model 'Driveway'
        db.delete_table('estatebase_driveway')

        # Deleting model 'Document'
        db.delete_table('estatebase_document')

        # Removing M2M table for field estate_type on 'Document'
        db.delete_table('estatebase_document_estate_type')

        # Deleting model 'EstateParam'
        db.delete_table('estatebase_estateparam')

        # Deleting model 'EstateStatus'
        db.delete_table('estatebase_estatestatus')

        # Deleting model 'EstateClientStatus'
        db.delete_table('estatebase_estateclientstatus')

        # Deleting model 'EstateTypeCategory'
        db.delete_table('estatebase_estatetypecategory')

        # Deleting model 'EstateType'
        db.delete_table('estatebase_estatetype')

        # Deleting model 'HistoryMeta'
        db.delete_table('estatebase_historymeta')

        # Deleting model 'EstateClient'
        db.delete_table('estatebase_estateclient')

        # Deleting model 'Estate'
        db.delete_table('estatebase_estate')

        # Removing M2M table for field estate_params on 'Estate'
        db.delete_table('estatebase_estate_estate_params')

        # Deleting model 'EstatePhoto'
        db.delete_table('estatebase_estatephoto')

        # Deleting model 'WallConstrucion'
        db.delete_table('estatebase_wallconstrucion')

        # Deleting model 'ExteriorFinish'
        db.delete_table('estatebase_exteriorfinish')

        # Deleting model 'WindowType'
        db.delete_table('estatebase_windowtype')

        # Deleting model 'Roof'
        db.delete_table('estatebase_roof')

        # Deleting model 'Heating'
        db.delete_table('estatebase_heating')

        # Deleting model 'WallFinish'
        db.delete_table('estatebase_wallfinish')

        # Deleting model 'Flooring'
        db.delete_table('estatebase_flooring')

        # Deleting model 'Ceiling'
        db.delete_table('estatebase_ceiling')

        # Deleting model 'Interior'
        db.delete_table('estatebase_interior')

        # Deleting model 'LevelName'
        db.delete_table('estatebase_levelname')

        # Deleting model 'Level'
        db.delete_table('estatebase_level')

        # Deleting model 'LayoutType'
        db.delete_table('estatebase_layouttype')

        # Deleting model 'Furniture'
        db.delete_table('estatebase_furniture')

        # Deleting model 'LayoutFeature'
        db.delete_table('estatebase_layoutfeature')

        # Deleting model 'Layout'
        db.delete_table('estatebase_layout')

        # Deleting model 'Bidg'
        db.delete_table('estatebase_bidg')

        # Removing M2M table for field documents on 'Bidg'
        db.delete_table('estatebase_bidg_documents')

        # Deleting model 'Shape'
        db.delete_table('estatebase_shape')

        # Deleting model 'LandType'
        db.delete_table('estatebase_landtype')

        # Deleting model 'Purpose'
        db.delete_table('estatebase_purpose')

        # Deleting model 'Stead'
        db.delete_table('estatebase_stead')

        # Deleting model 'ClientType'
        db.delete_table('estatebase_clienttype')

        # Deleting model 'Origin'
        db.delete_table('estatebase_origin')

        # Deleting model 'Client'
        db.delete_table('estatebase_client')

        # Deleting model 'ContactType'
        db.delete_table('estatebase_contacttype')

        # Deleting model 'ContactState'
        db.delete_table('estatebase_contactstate')

        # Deleting model 'ContactHistory'
        db.delete_table('estatebase_contacthistory')

        # Deleting model 'Contact'
        db.delete_table('estatebase_contact')

        # Deleting model 'Bid'
        db.delete_table('estatebase_bid')

        # Removing M2M table for field estates on 'Bid'
        db.delete_table('estatebase_bid_estates')

        # Removing M2M table for field estate_types on 'Bid'
        db.delete_table('estatebase_bid_estate_types')

        # Removing M2M table for field regions on 'Bid'
        db.delete_table('estatebase_bid_regions')

        # Removing M2M table for field localities on 'Bid'
        db.delete_table('estatebase_bid_localities')

        # Deleting model 'EstateRegister'
        db.delete_table('estatebase_estateregister')

        # Removing M2M table for field estates on 'EstateRegister'
        db.delete_table('estatebase_estateregister_estates')

        # Removing M2M table for field bids on 'EstateRegister'
        db.delete_table('estatebase_estateregister_bids')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'estatebase.beside': {
            'Meta': {'ordering': "['name']", 'object_name': 'Beside'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.bid': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Bid'},
            'agency_price_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'agency_price_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'broker': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'brokers'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['auth.User']"}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bids'", 'to': "orm['estatebase.Client']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estate_filter': ('picklefield.fields.PickledObjectField', [], {'null': 'True', 'blank': 'True'}),
            'estate_types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['estatebase.EstateType']", 'null': 'True', 'blank': 'True'}),
            'estates': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['estatebase.Estate']", 'null': 'True', 'blank': 'True'}),
            'history': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['estatebase.HistoryMeta']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['estatebase.Locality']", 'null': 'True', 'blank': 'True'}),
            'regions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['estatebase.Region']", 'null': 'True', 'blank': 'True'})
        },
        'estatebase.bidg': {
            'Meta': {'ordering': "['id']", 'object_name': 'Bidg'},
            'basic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ceiling': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Ceiling']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'ceiling_height': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'documents': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['estatebase.Document']", 'null': 'True', 'blank': 'True'}),
            'elevator': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bidgs'", 'to': "orm['estatebase.Estate']"}),
            'estate_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.EstateType']", 'on_delete': 'models.PROTECT'}),
            'exterior_finish': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.ExteriorFinish']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'floor': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'floor_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'flooring': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Flooring']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'heating': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Heating']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interior': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Interior']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'roof': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Roof']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'room_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'room_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'total_area': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'used_area': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'wall_construcion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.WallConstrucion']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'wall_finish': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.WallFinish']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'window_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.WindowType']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'year_built': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'estatebase.ceiling': {
            'Meta': {'ordering': "['name']", 'object_name': 'Ceiling'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.client': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Client'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'broker': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'clientbrokers'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['auth.User']"}),
            'client_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.ClientType']", 'on_delete': 'models.PROTECT'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'history': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['estatebase.HistoryMeta']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Origin']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'})
        },
        'estatebase.clienttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ClientType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.contact': {
            'Meta': {'ordering': "['contact_state__id', 'contact_type__id']", 'object_name': 'Contact'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': "orm['estatebase.Client']"}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'contact_state': ('django.db.models.fields.related.ForeignKey', [], {'default': '5', 'to': "orm['estatebase.ContactState']", 'on_delete': 'models.PROTECT'}),
            'contact_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.ContactType']", 'on_delete': 'models.PROTECT'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'estatebase.contacthistory': {
            'Meta': {'object_name': 'ContactHistory'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Contact']"}),
            'contact_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.ContactState']", 'on_delete': 'models.PROTECT'}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 1, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'})
        },
        'estatebase.contactstate': {
            'Meta': {'ordering': "['name']", 'object_name': 'ContactState'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.contacttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ContactType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.document': {
            'Meta': {'ordering': "['name']", 'object_name': 'Document'},
            'estate_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estatebase.EstateType']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.driveway': {
            'Meta': {'ordering': "['name']", 'object_name': 'Driveway'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.electricity': {
            'Meta': {'ordering': "['name']", 'object_name': 'Electricity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.estate': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Estate'},
            'agency_price': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'beside': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Beside']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'beside_distance': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'clients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'estates'", 'symmetrical': 'False', 'through': "orm['estatebase.EstateClient']", 'to': "orm['estatebase.Client']"}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Contact']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'driveway': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Driveway']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'driveway_distance': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'electricity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Electricity']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'electricity_distance': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'estate_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'estate_params': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['estatebase.EstateParam']", 'null': 'True', 'blank': 'True'}),
            'estate_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.EstateStatus']", 'on_delete': 'models.PROTECT'}),
            'estate_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.EstateType']", 'on_delete': 'models.PROTECT'}),
            'gassupply': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Gassupply']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'gassupply_distance': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'history': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['estatebase.HistoryMeta']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Internet']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'locality': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Locality']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'microdistrict': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Microdistrict']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Origin']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Region']", 'on_delete': 'models.PROTECT'}),
            'saler_price': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sewerage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Sewerage']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'sewerage_distance': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Street']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'telephony': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Telephony']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'watersupply': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Watersupply']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'watersupply_distance': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'estatebase.estateclient': {
            'Meta': {'object_name': 'EstateClient'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Client']"}),
            'estate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Estate']"}),
            'estate_client_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.EstateClientStatus']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'estatebase.estateclientstatus': {
            'Meta': {'ordering': "['name']", 'object_name': 'EstateClientStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.estateparam': {
            'Meta': {'ordering': "['order']", 'object_name': 'EstateParam'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'})
        },
        'estatebase.estatephoto': {
            'Meta': {'ordering': "['order']", 'object_name': 'EstatePhoto'},
            'estate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['estatebase.Estate']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'})
        },
        'estatebase.estateregister': {
            'Meta': {'ordering': "['-id']", 'object_name': 'EstateRegister'},
            'bids': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'estate_registers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['estatebase.Bid']"}),
            'broker': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'estate_registers'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['auth.User']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estates': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['estatebase.Estate']", 'null': 'True', 'blank': 'True'}),
            'history': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['estatebase.HistoryMeta']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.estatestatus': {
            'Meta': {'ordering': "['name']", 'object_name': 'EstateStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.estatetype': {
            'Meta': {'ordering': "['name']", 'object_name': 'EstateType'},
            'estate_type_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.EstateTypeCategory']", 'on_delete': 'models.PROTECT'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'object_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'placeable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'estatebase.estatetypecategory': {
            'Meta': {'ordering': "['order']", 'object_name': 'EstateTypeCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'})
        },
        'estatebase.exteriorfinish': {
            'Meta': {'ordering': "['name']", 'object_name': 'ExteriorFinish'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.flooring': {
            'Meta': {'ordering': "['name']", 'object_name': 'Flooring'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.furniture': {
            'Meta': {'ordering': "['name']", 'object_name': 'Furniture'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.gassupply': {
            'Meta': {'ordering': "['name']", 'object_name': 'Gassupply'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.geogroup': {
            'Meta': {'ordering': "['name']", 'object_name': 'GeoGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.heating': {
            'Meta': {'ordering': "['name']", 'object_name': 'Heating'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.historymeta': {
            'Meta': {'object_name': 'HistoryMeta'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creators'", 'on_delete': 'models.PROTECT', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificated': ('django.db.models.fields.DateTimeField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updators'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['auth.User']"})
        },
        'estatebase.interior': {
            'Meta': {'ordering': "['name']", 'object_name': 'Interior'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.internet': {
            'Meta': {'ordering': "['name']", 'object_name': 'Internet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.landtype': {
            'Meta': {'ordering': "['name']", 'object_name': 'LandType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.layout': {
            'Meta': {'object_name': 'Layout'},
            'area': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'furniture': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Furniture']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout_feature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.LayoutFeature']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'layout_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.LayoutType']", 'on_delete': 'models.PROTECT'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Level']"}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'estatebase.layoutfeature': {
            'Meta': {'ordering': "['name']", 'object_name': 'LayoutFeature'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.layouttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'LayoutType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.level': {
            'Meta': {'ordering': "['level_name']", 'object_name': 'Level'},
            'bidg': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'levels'", 'to': "orm['estatebase.Bidg']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.LevelName']"})
        },
        'estatebase.levelname': {
            'Meta': {'ordering': "['name']", 'object_name': 'LevelName'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.locality': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'region'),)", 'object_name': 'Locality'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Region']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'})
        },
        'estatebase.microdistrict': {
            'Meta': {'ordering': "['name']", 'object_name': 'Microdistrict'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locality': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Locality']", 'on_delete': 'models.PROTECT'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.origin': {
            'Meta': {'ordering': "['name']", 'object_name': 'Origin'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.purpose': {
            'Meta': {'ordering': "['name']", 'object_name': 'Purpose'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.region': {
            'Meta': {'ordering': "['name']", 'object_name': 'Region'},
            'geo_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.GeoGroup']", 'on_delete': 'models.PROTECT'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.roof': {
            'Meta': {'ordering': "['name']", 'object_name': 'Roof'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.sewerage': {
            'Meta': {'ordering': "['name']", 'object_name': 'Sewerage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.shape': {
            'Meta': {'ordering': "['name']", 'object_name': 'Shape'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.stead': {
            'Meta': {'object_name': 'Stead'},
            'estate': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'stead'", 'unique': 'True', 'to': "orm['estatebase.Estate']"}),
            'face_area': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'land_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.LandType']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'purpose': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Purpose']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'shape': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Shape']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'total_area': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'})
        },
        'estatebase.street': {
            'Meta': {'ordering': "['name']", 'object_name': 'Street'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locality': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Locality']", 'on_delete': 'models.PROTECT'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.telephony': {
            'Meta': {'ordering': "['name']", 'object_name': 'Telephony'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'geo_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estatebase.GeoGroup']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'estatebase.wallconstrucion': {
            'Meta': {'ordering': "['name']", 'object_name': 'WallConstrucion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.wallfinish': {
            'Meta': {'ordering': "['name']", 'object_name': 'WallFinish'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.watersupply': {
            'Meta': {'ordering': "['name']", 'object_name': 'Watersupply'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.windowtype': {
            'Meta': {'ordering': "['name']", 'object_name': 'WindowType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['estatebase']