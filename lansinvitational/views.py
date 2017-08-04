from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse('Welcome to Lans invitational')
