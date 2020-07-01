# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rating'
        db.create_table(u'ratings_rating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('total_rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total_votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('avg_rating', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('percent', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'ratings', ['Rating'])

        # Adding model 'RatingEvent'
        db.create_table(u'ratings_ratingevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'ratings', ['RatingEvent'])


    def backwards(self, orm):
        # Deleting model 'Rating'
        db.delete_table(u'ratings_rating')

        # Deleting model 'RatingEvent'
        db.delete_table(u'ratings_ratingevent')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['ratings']