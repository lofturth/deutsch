# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Quiz.slug'
        db.delete_column(u'quizzes_quiz', 'slug')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Quiz.slug'
        raise RuntimeError("Cannot reverse this migration. 'Quiz.slug' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Quiz.slug'
        db.add_column(u'quizzes_quiz', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=50),
                      keep_default=False)


    models = {
        u'quizzes.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'columns': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sentence': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quizzes.Sentence']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'quizzes.sentence': {
            'Meta': {'object_name': 'Sentence'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'verb': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quizzes.Verb']", 'symmetrical': 'False'})
        },
        u'quizzes.verb': {
            'Meta': {'object_name': 'Verb'},
            'du_present': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'er_present': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ich_present': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ihr_present': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'infinitive': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sie_present': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'wir_present': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['quizzes']