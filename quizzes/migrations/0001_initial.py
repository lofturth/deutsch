# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Verb'
        db.create_table(u'quizzes_verb', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('infinitive', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ich_present', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('du_present', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('er_present', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('wir_present', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('ihr_present', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('sie_present', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'quizzes', ['Verb'])

        # Adding model 'Sentence'
        db.create_table(u'quizzes_sentence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'quizzes', ['Sentence'])

        # Adding M2M table for field verb on 'Sentence'
        m2m_table_name = db.shorten_name(u'quizzes_sentence_verb')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sentence', models.ForeignKey(orm[u'quizzes.sentence'], null=False)),
            ('verb', models.ForeignKey(orm[u'quizzes.verb'], null=False))
        ))
        db.create_unique(m2m_table_name, ['sentence_id', 'verb_id'])

        # Adding model 'Quiz'
        db.create_table(u'quizzes_quiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('instructions', self.gf('django.db.models.fields.TextField')()),
            ('columns', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'quizzes', ['Quiz'])

        # Adding M2M table for field sentence on 'Quiz'
        m2m_table_name = db.shorten_name(u'quizzes_quiz_sentence')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quiz', models.ForeignKey(orm[u'quizzes.quiz'], null=False)),
            ('sentence', models.ForeignKey(orm[u'quizzes.sentence'], null=False))
        ))
        db.create_unique(m2m_table_name, ['quiz_id', 'sentence_id'])


    def backwards(self, orm):
        # Deleting model 'Verb'
        db.delete_table(u'quizzes_verb')

        # Deleting model 'Sentence'
        db.delete_table(u'quizzes_sentence')

        # Removing M2M table for field verb on 'Sentence'
        db.delete_table(db.shorten_name(u'quizzes_sentence_verb'))

        # Deleting model 'Quiz'
        db.delete_table(u'quizzes_quiz')

        # Removing M2M table for field sentence on 'Quiz'
        db.delete_table(db.shorten_name(u'quizzes_quiz_sentence'))


    models = {
        u'quizzes.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'columns': ('django.db.models.fields.SmallIntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {}),
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