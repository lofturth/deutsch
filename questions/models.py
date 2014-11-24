from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.TextField()

    def __unicode__(self):
        return "%s" % (self.text.replace("[1]","______"))



class Answer(models.Model):
    answer = models.CharField(max_length=100)
    question = models.ForeignKey(Question)
    reactionGif = models.URLField()

    def __unicode__(self):
        return "%s" % (self.answer)

class WrongAnswer(models.Model):
    wrongAnswer = models.CharField(max_length=100)
    question = models.ForeignKey(Question)
    reactionGif = models.URLField()    

    def __unicode__(self):
        return "%s" % (self.wrongAnswer)