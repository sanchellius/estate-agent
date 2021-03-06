# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Citizenship'
        db.create_table('devrep_citizenship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('devrep', ['Citizenship'])

        # Adding field 'ExtraProfile.citizenship'
        db.add_column('devrep_extraprofile', 'citizenship',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devrep.Citizenship'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'ExtraProfile.bad_habits'
        db.add_column('devrep_extraprofile', 'bad_habits',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ExtraProfile.progress'
        db.add_column('devrep_extraprofile', 'progress',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ExtraProfile.pc_skills'
        db.add_column('devrep_extraprofile', 'pc_skills',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


        # Changing field 'ExtraProfile.birthplace'
        db.alter_column('devrep_extraprofile', 'birthplace', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'ExtraProfile.passport_number'
        db.alter_column('devrep_extraprofile', 'passport_number', self.gf('django.db.models.fields.CharField')(max_length=6, null=True))

        # Changing field 'ExtraProfile.passport_series'
        db.alter_column('devrep_extraprofile', 'passport_series', self.gf('django.db.models.fields.CharField')(max_length=4, null=True))

        # Changing field 'ExtraProfile.birthday'
        db.alter_column('devrep_extraprofile', 'birthday', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):
        # Deleting model 'Citizenship'
        db.delete_table('devrep_citizenship')

        # Deleting field 'ExtraProfile.citizenship'
        db.delete_column('devrep_extraprofile', 'citizenship_id')

        # Deleting field 'ExtraProfile.bad_habits'
        db.delete_column('devrep_extraprofile', 'bad_habits')

        # Deleting field 'ExtraProfile.progress'
        db.delete_column('devrep_extraprofile', 'progress')

        # Deleting field 'ExtraProfile.pc_skills'
        db.delete_column('devrep_extraprofile', 'pc_skills')


        # Changing field 'ExtraProfile.birthplace'
        db.alter_column('devrep_extraprofile', 'birthplace', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'ExtraProfile.passport_number'
        db.alter_column('devrep_extraprofile', 'passport_number', self.gf('django.db.models.fields.CharField')(default='', max_length=6))

        # Changing field 'ExtraProfile.passport_series'
        db.alter_column('devrep_extraprofile', 'passport_series', self.gf('django.db.models.fields.CharField')(default='', max_length=4))

        # Changing field 'ExtraProfile.birthday'
        db.alter_column('devrep_extraprofile', 'birthday', self.gf('django.db.models.fields.DateField')())

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
        'devrep.address': {
            'Meta': {'ordering': "['id']", 'object_name': 'Address'},
            'estate_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locality': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Locality']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'microdistrict': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Microdistrict']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Region']", 'on_delete': 'models.PROTECT'}),
            'street': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Street']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'})
        },
        'devrep.citizenship': {
            'Meta': {'ordering': "['name']", 'object_name': 'Citizenship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'devrep.clientpartner': {
            'Meta': {'unique_together': "(('client', 'partner'),)", 'object_name': 'ClientPartner'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devrep.Partner']"}),
            'partner_client_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devrep.PartnerClientStatus']"})
        },
        'devrep.devprofile': {
            'Meta': {'object_name': 'DevProfile'},
            'coverage_localities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'person_coverage'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['estatebase.Locality']"}),
            'coverage_regions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'person_coverage'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['estatebase.Region']"}),
            'experience': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devrep.Experience']", 'null': 'True', 'blank': 'True'}),
            'gears': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'owners'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['devrep.Gear']"}),
            'has_transport': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quality': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devrep.Quality']", 'null': 'True', 'blank': 'True'}),
            'work_types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devrep.WorkType']", 'null': 'True', 'through': "orm['devrep.WorkTypeProfile']", 'blank': 'True'})
        },
        'devrep.experience': {
            'Meta': {'ordering': "['name']", 'object_name': 'Experience'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'devrep.extraprofile': {
            'Meta': {'object_name': 'ExtraProfile'},
            'adress': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'extra_profile'", 'unique': 'True', 'null': 'True', 'to': "orm['devrep.Address']"}),
            'bad_habits': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2015, 4, 14, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'birthplace': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'citizenship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devrep.Citizenship']", 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'passport_number': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'passport_series': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'patronymic': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'pc_skills': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'progress': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'devrep.gear': {
            'Meta': {'ordering': "['name']", 'object_name': 'Gear'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'devrep.measure': {
            'Meta': {'ordering': "['name']", 'object_name': 'Measure'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'devrep.partner': {
            'Meta': {'ordering': "['name']", 'object_name': 'Partner'},
            'address': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'partner'", 'unique': 'True', 'null': 'True', 'to': "orm['devrep.Address']"}),
            'clients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['estatebase.Client']", 'null': 'True', 'through': "orm['devrep.ClientPartner']", 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'history': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['estatebase.HistoryMeta']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['devrep.Partner']"}),
            'partner_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partner'", 'to': "orm['devrep.PartnerType']"}),
            'person_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'devrep.partnerclientstatus': {
            'Meta': {'ordering': "['name']", 'object_name': 'PartnerClientStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'devrep.partnertype': {
            'Meta': {'ordering': "['name']", 'object_name': 'PartnerType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'devrep.quality': {
            'Meta': {'ordering': "['name']", 'object_name': 'Quality'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'devrep.worktype': {
            'Meta': {'ordering': "['name']", 'object_name': 'WorkType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['devrep.WorkType']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'devrep.worktypeprofile': {
            'Meta': {'unique_together': "(('work_type', 'dev_profile'),)", 'object_name': 'WorkTypeProfile'},
            'dev_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devrep.DevProfile']"}),
            'experience': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devrep.Experience']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devrep.Measure']"}),
            'price_max': ('django.db.models.fields.IntegerField', [], {}),
            'price_min': ('django.db.models.fields.IntegerField', [], {}),
            'quality': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devrep.Quality']", 'null': 'True', 'blank': 'True'}),
            'work_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devrep.WorkType']"})
        },
        'estatebase.client': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Client'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'client_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.ClientType']", 'on_delete': 'models.PROTECT'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dev_profile': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'client'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['devrep.DevProfile']", 'blank': 'True', 'unique': 'True'}),
            'extra_profile': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'client'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['devrep.ExtraProfile']", 'blank': 'True', 'unique': 'True'}),
            'has_dev_profile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'history': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['estatebase.HistoryMeta']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Origin']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'})
        },
        'estatebase.clienttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ClientType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.geogroup': {
            'Meta': {'ordering': "['name']", 'object_name': 'GeoGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.historymeta': {
            'Meta': {'object_name': 'HistoryMeta'},
            'created': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creators'", 'on_delete': 'models.PROTECT', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificated': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updators'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['auth.User']"})
        },
        'estatebase.locality': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'region'),)", 'object_name': 'Locality'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locality_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.LocalityType']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_gent': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_loct': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Region']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'})
        },
        'estatebase.localitytype': {
            'Meta': {'ordering': "['name']", 'object_name': 'LocalityType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'prep_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'sort_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'estatebase.microdistrict': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'locality'),)", 'object_name': 'Microdistrict'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locality': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Locality']", 'on_delete': 'models.PROTECT'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.origin': {
            'Meta': {'ordering': "['name']", 'object_name': 'Origin'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'estatebase.region': {
            'Meta': {'ordering': "['name']", 'object_name': 'Region'},
            'geo_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.GeoGroup']", 'on_delete': 'models.PROTECT'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metropolis': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'metropolis_region'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['estatebase.Locality']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'regular_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'regular_name_gent': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'estatebase.street': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'locality', 'street_type'),)", 'object_name': 'Street'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locality': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.Locality']", 'on_delete': 'models.PROTECT'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'street_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estatebase.StreetType']", 'on_delete': 'models.PROTECT'})
        },
        'estatebase.streettype': {
            'Meta': {'ordering': "['name']", 'object_name': 'StreetType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'sort_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['devrep']