# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'questions_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'questions', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'questions_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questions.Question'])),
            ('reactionGif', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'questions', ['Answer'])

        # Adding model 'WrongAnswer'
        db.create_table(u'questions_wronganswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wrongAnswer', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questions.Question'])),
            ('reactionGif', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'questions', ['WrongAnswer'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'questions_question')

        # Deleting model 'Answer'
        db.delete_table(u'questions_answer')

        # Deleting model 'WrongAnswer'
        db.delete_table(u'questions_wronganswer')


    models = {
        u'questions.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['questions.Question']"}),
            'reactionGif': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'questions.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'questions.wronganswer': {
            'Meta': {'object_name': 'WrongAnswer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['questions.Question']"}),
            'reactionGif': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'wrongAnswer': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['questions']