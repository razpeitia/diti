from django.shortcuts import render_to_response
from main.models import Slide, Page

def home(request):
    response = {
        "slides_list": Slide.objects.all(),
        "pages_list": Page.objects.all(),
    }
    return render_to_response('index.html', response)
