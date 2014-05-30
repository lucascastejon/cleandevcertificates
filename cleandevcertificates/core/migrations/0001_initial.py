# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'core_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('university', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Person'], null=True, blank=True)),
            ('course', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('semester', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cpf', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'core_person')


    models = {
        u'core.person': {
            'Meta': {'ordering': "['name']", 'object_name': 'Person'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'course': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'cpf': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semester': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Person']", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']