# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RatingUser'
        db.create_table(u'ratinguser_ratinguser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
        ))
        db.send_create_signal(u'ratinguser', ['RatingUser'])


    def backwards(self, orm):
        # Deleting model 'RatingUser'
        db.delete_table(u'ratinguser_ratinguser')


    models = {
        u'ratinguser.ratinguser': {
            'Meta': {'object_name': 'RatingUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['ratinguser']