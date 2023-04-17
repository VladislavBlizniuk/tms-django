from django.shortcuts import render, get_object_or_404, redirect

from .models import Question


def index(request):
    questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id: int):
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def vote(request,question_id: int):
    question = get_object_or_404(Question, id=question_id)
    choice_id = int(request.POST['choice_id'])
    choice = question.choices.get(id=choice_id)
    choice.votes += 1
    choice.save()
    return redirect('polls:detail', question_id)

