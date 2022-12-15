""" from django.http import HttpResponse


def audio(request):
    return HttpResponse("Hello, world. You're at the polls index.") """

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def audio(request):
    template = loader.get_template('voiceover.html')
    return HttpResponse(template.render())