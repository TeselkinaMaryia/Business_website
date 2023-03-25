from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models
from . import forms


class AskMain(ListView):
    model = models.Category
    template_name = 'ask/ask_main.html'


def all_question(request, category):
    questions = models.Question.objects.filter(category__name=category).order_by('-date_of_create')
    this_category = models.Category.objects.get(name=category)

    form = forms.QuestionForm()
    if request.method == 'POST':
        form = forms.QuestionForm(request.POST)
        if form.is_valid():
            question = models.Question(
                category=this_category,
                auther=form.cleaned_data['auther'],
                department=form.cleaned_data['department'],
                your_question=form.cleaned_data['your_question']
            )
            question.save()
    context = {
        'form': form,
        'questions': questions,
        'category': category
    }
    return render(request, 'ask/ask_questions.html', context)


def all_comments(request, pk, category):
    question = models.Question.objects.get(pk=pk)
    comments = models.Comments.objects.filter(question=question)

    form = forms.CommentForm()
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = models.Comments(
                question=question,
                your_comment=form.cleaned_data['your_comment'],
            )
            comment.save()
    context = {
        'form': form,
        'question': question,
        'comments': comments,
        'category': category
    }
    return render(request, 'ask/ask_comments.html', context)
