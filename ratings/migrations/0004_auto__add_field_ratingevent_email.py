# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RatingEvent.email'
        db.add_column(u'ratings_ratingevent', 'email',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratinguser.RatingUser'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RatingEvent.email'
        db.delete_column(u'ratings_ratingevent', 'email_id')


    models = {
        u'ratings.rating': {
            'Meta': {'object_name': 'Rating'},
            'avg_rating': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'percent': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'total_rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.ratingevent': {
            'Meta': {'object_name': 'RatingEvent'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratinguser.RatingUser']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratinguser.ratinguser': {
            'Meta': {'object_name': 'RatingUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['ratings']