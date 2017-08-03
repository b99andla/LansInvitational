from django.shortcuts import render
from django.http import HttpResponse
from .models import Round, Score
from django.template import loader

# Create your views here.


def index(request):
    latest_round_list = Round.objects.order_by('name')
    template = loader.get_template('round/index.html')
    context = {'latest_round_list': latest_round_list, }

    return HttpResponse(template.render(context, request))


def detail(request, round_id):
    score_list = Score.objects.filter(
        team__round_id=round_id).order_by('team__name')
    template = loader.get_template('round/detail.html')
    context = {'score_list': score_list}
    return HttpResponse(template.render(context, request))
