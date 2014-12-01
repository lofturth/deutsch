# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import get_object_or_404
import re

from .models import Quiz

def home(request):
    context = {}
    template = "home.html"
    return render(request, template, context)


def quiz(request, quiz_pk):

    print request.GET
    quiz_obj = get_object_or_404(Quiz, pk=quiz_pk)

    orginal_sentences = quiz_obj.sentence.all()
    sentences = []

    for s in orginal_sentences:
        s.render_text = re.sub('\[[^\]]+\]', '[blank]', s.text)
        sentences.append(s)

    context = {'quiz': quiz_obj, 'sentences': sentences}
    template = "quiz.html"
    return render(request, template, context)





# def get_questions(request):
#     if request.method == 'GET':
#         cat_pk = request.GET.get('cat_pk')
#
#         result = []
#         # Have to do this "backwards", find answers first and then get their questions.
#         answers = Answer.objects.filter(question__category__pk=cat_pk)
#         for answer in answers:
#             result.append({'q_id': answer.question.pk, 'q_text': answer.question.text, 'answer': answer.answer, 'placeholder': answer.placeholder})
#
#         return HttpResponse(
#             json.dumps(result),
#             content_type="application/json"
#         )
#
