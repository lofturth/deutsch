# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from .models import Question, Answer, WrongAnswer


def home(request):
    questions = Question.objects.all()

    submission = request.GET.get('submission')
    reactionGif = ""
    if submission:
        question_id = request.GET.get('question_id')
        #question_obj = Question.objects.filter(id=question_id)
        answer_obj = Answer.objects.filter(question__id=question_id)
        if submission == answer_obj[0].answer:
            reactionGif = answer_obj[0].reactionGif
        else:
            wrongAnswer_obj = WrongAnswer.objects.filter(question__id=question_id)
            reactionGif = wrongAnswer_obj[0].reactionGif       

    print reactionGif
    context = {'questions': questions, 'reactionGif': reactionGif}
    template = "home.html"
    return render(request, template, context)
