# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'films_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'films', ['Category'])

        # Adding model 'Film'
        db.create_table(u'films_film', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('thumb', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('director', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('runtime', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('description_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['films.Category'])),
        ))
        db.send_create_signal(u'films', ['Film'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'films_category')

        # Deleting model 'Film'
        db.delete_table(u'films_film')


    models = {
        u'films.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'films.film': {
            'Meta': {'object_name': 'Film'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.Category']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'director': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'runtime': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['films']