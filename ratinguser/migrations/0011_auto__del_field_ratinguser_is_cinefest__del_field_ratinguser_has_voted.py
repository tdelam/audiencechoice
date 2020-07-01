# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'RatingUser.is_cinefest'
        db.delete_column(u'ratinguser_ratinguser', 'is_cinefest')

        # Deleting field 'RatingUser.has_voted'
        db.delete_column(u'ratinguser_ratinguser', 'has_voted')


    def backwards(self, orm):
        # Adding field 'RatingUser.is_cinefest'
        db.add_column(u'ratinguser_ratinguser', 'is_cinefest',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'RatingUser.has_voted'
        db.add_column(u'ratinguser_ratinguser', 'has_voted',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    models = {
        u'ratinguser.ratinguser': {
            'Meta': {'object_name': 'RatingUser'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'key_expires': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 4, 0, 0)'})
        }
    }

    complete_apps = ['ratinguser']