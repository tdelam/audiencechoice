# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'RatingUser.ip'
        db.alter_column(u'ratinguser_ratinguser', 'ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True))

    def backwards(self, orm):

        # Changing field 'RatingUser.ip'
        db.alter_column(u'ratinguser_ratinguser', 'ip', self.gf('django.db.models.fields.IPAddressField')(default='', max_length=15))

    models = {
        u'ratinguser.ratinguser': {
            'Meta': {'object_name': 'RatingUser'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'has_voted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'key_expires': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 3, 0, 0)'})
        }
    }

    complete_apps = ['ratinguser']