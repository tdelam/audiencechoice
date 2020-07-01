# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'RatingUser', fields ['email']
        db.delete_unique(u'ratinguser_ratinguser', ['email'])


    def backwards(self, orm):
        # Adding unique constraint on 'RatingUser', fields ['email']
        db.create_unique(u'ratinguser_ratinguser', ['email'])


    models = {
        u'ratinguser.ratinguser': {
            'Meta': {'object_name': 'RatingUser'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['ratinguser']