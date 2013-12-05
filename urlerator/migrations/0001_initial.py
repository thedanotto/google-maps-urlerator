# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'urlChecker'
        db.create_table(u'urlerator_urlchecker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_address', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('to_address', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('url_output', self.gf('django.db.models.fields.CharField')(max_length=600, null=True, blank=True)),
            ('html_output', self.gf('django.db.models.fields.CharField')(max_length=700, null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'urlerator', ['urlChecker'])


    def backwards(self, orm):
        # Deleting model 'urlChecker'
        db.delete_table(u'urlerator_urlchecker')


    models = {
        u'urlerator.urlchecker': {
            'Meta': {'object_name': 'urlChecker'},
            'from_address': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'html_output': ('django.db.models.fields.CharField', [], {'max_length': '700', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'to_address': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'url_output': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['urlerator']