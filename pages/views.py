from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

import os

def home_view(request, *args, **kwargs):
    template = loader.get_template('pages/index.html')
    fruit_list = ['apple', 'banana', 'orange']

    message = os.environ.get('TEST_MESSAGE', '')
    secret_message = os.environ.get('TEST_SECRET_MESSAGE', '')
    color_class = os.environ.get('TEST_COLOR', '')

    print(message)

    context = {
        'message': message,
        'secret_message': secret_message,
        'color_class': color_class,
        'fruit_list': fruit_list
    }

    return HttpResponse(template.render(context, request))
