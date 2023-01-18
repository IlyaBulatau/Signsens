from django.shortcuts import render, redirect
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

    # def get(self, request, *args, **kwargs):
    #     last_word = request.session.get('last_word')
    #     current_word = self.kwargs.get(self.slug_url_kwarg)
    #     if last_word != current_word:
    #         request.session['last_word'] = current_word
    #         return redirect('word')
    #     return super().get(request, *args, **kwargs)

def start_page(request):
    return render(request, 'main/start_page.html')

def welcom(request):
    return render(request, 'main/welcom.html')

