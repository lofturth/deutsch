from django.db import models
from django.contrib.auth.models import User


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

    def __unicode__(self):
        return "%s - %s" % (self.id, self.title)


class Quiz(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    sentence = models.ManyToManyField(Sentence)
    columns = models.SmallIntegerField(blank=True, default=1)

    class Meta:
        verbose_name_plural = "Quizzes"

    def __unicode__(self):
        return "%s" % self.title

