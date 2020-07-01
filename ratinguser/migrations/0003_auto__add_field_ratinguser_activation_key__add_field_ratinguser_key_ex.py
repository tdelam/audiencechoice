# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RatingUser.activation_key'
        db.add_column(u'ratinguser_ratinguser', 'activation_key',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True),
                      keep_default=False)

        # Adding field 'RatingUser.key_expires'
        db.add_column(u'ratinguser_ratinguser', 'key_expires',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 9, 2, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RatingUser.activation_key'
        db.delete_column(u'ratinguser_ratinguser', 'activation_key')

        # Deleting field 'RatingUser.key_expires'
        db.delete_column(u'ratinguser_ratinguser', 'key_expires')


    models = {
        u'ratinguser.ratinguser': {
            'Meta': {'object_name': 'RatingUser'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_expires': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 2, 0, 0)'})
        }
    }

    complete_apps = ['ratinguser']