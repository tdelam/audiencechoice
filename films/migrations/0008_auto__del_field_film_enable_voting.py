# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Film.enable_voting'
        db.delete_column(u'films_film', 'enable_voting')


    def backwards(self, orm):
        # Adding field 'Film.enable_voting'
        db.add_column(u'films_film', 'enable_voting',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


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
            'director': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'runtime': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['films']