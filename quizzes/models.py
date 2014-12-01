
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import re
from django.db.models.signals import post_save

class Verb(models.Model):
    infinitive = models.CharField(max_length=50)
    ich_present = models.CharField(max_length=50, blank=True)
    du_present = models.CharField(max_length=50, blank=True)
    er_present = models.CharField(max_length=50, blank=True)
    wir_present = models.CharField(max_length=50, blank=True)
    ihr_present = models.CharField(max_length=50, blank=True)
    sie_present = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "Verbs"

    def __unicode__(self):
        return "%s" % self.infinitive


class Sentence(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    verb = models.ManyToManyField(Verb)

    # def save(self):
    #     verbs = []
    #     brackets = re.findall('\[[^\]]+\]', getattr(self, 'text'))
    #     for b in brackets:
    #         split = b.strip('[]').split(':')
    #         try:
    #             self.verb.add(Verb.objects.get(infinitive=split[0]))
    #         except Verb.DoesNotExist:
    #             print 'Error put something better here'
    #     super(Sentence, self).save()

    def __unicode__(self):
        return "%s - %s" % (self.id, self.title)

def add_model_verb(sender, instance, created, **kwargs):
    print "asdf"
    test = Verb.objects.get(infinitive='mögen')
    instance.verb.add(test)

post_save.connect(add_model_verb, sender=Sentence)


class Quiz(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    sentence = models.ManyToManyField(Sentence, blank=True)
    columns = models.SmallIntegerField(blank=True, default=1)

    class Meta:
        verbose_name_plural = "Quizzes"

    def __unicode__(self):
        return "%s" % self.title

