from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Word

class WordView(ListView):
    '''
     Word selection page
    '''
    model = Word
    template_name = 'main/main.html'
    context_object_name = 'word'

class WordDetailView(DetailView):
    '''
    Selected word page and video request
    '''
    model = Word
    template_name = 'main/word.html'
    context_object_name = 'detail_word'
    slug_url_kwarg = 'word_slug'

def start_page(request):
    return render(request, 'main/start_page.html')

def welcom(request):
    return render(request, 'main/welcom.html')

