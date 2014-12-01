
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import re
from django.db.models.signals import post_save
from django.contrib import messages
import pprint as pp

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

    def save(self):
        verb_obj = []


        super(Sentence, self).save()

    def __unicode__(self):
        return "%s - %s" % (self.id, self.title)

def add_model_verb(sender, instance, created, **kwargs):
    # Find all brackets of the form fx. [mögen:er, können:sie]
    print "Clear all verbs"
    instance.verb.clear()
    verbs = re.findall('(?:\[|,) *(\w+):', getattr(instance, 'text'), re.UNICODE)
    for verb in verbs:
        try:
            verb_obj = Verb.objects.get(infinitive=verb)
            if verb_obj not in instance.verb.all():
                instance.verb.add(verb_obj)
                print "add verb " + verb_obj.infinitive
        except Verb.DoesNotExist:
            print "verb " + verb + " does not exist."


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

