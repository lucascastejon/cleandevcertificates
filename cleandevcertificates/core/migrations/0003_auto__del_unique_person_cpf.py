# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Person', fields ['cpf']
        db.delete_unique(u'core_person', ['cpf'])


    def backwards(self, orm):
        # Adding unique constraint on 'Person', fields ['cpf']
        db.create_unique(u'core_person', ['cpf'])


    models = {
        u'core.person': {
            'Meta': {'ordering': "['name']", 'object_name': 'Person'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'course': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semester': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Person']", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']