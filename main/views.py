from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View

import cv2

from main.models import Word

class WordView(ListView):
    '''
     Word selection page
    '''
    model = Word
    template_name = 'main/main.html'
    context_object_name = 'word'


class WordDetailView(View):
    model = Word
    template_name = 'main/word.html'
    context_object_name = 'detail_word'
    slug_url_kwarg = 'word_slug'
    
    def get(self, request, *args, **kwargs):
        detail_word = get_object_or_404(Word, slug=kwargs['word_slug'])
        return render(request, self.template_name, {'detail_word': detail_word})

    def post(self, request, *args, **kwargs):
        if request.POST.get('permission') == 'granted':
            enable_camera()
        return self.get(request, *args, **kwargs)

def enable_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error opening camera")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading frame from camera")
            break
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    


def start_page(request):
    return render(request, 'main/start_page.html')

def welcom(request):
    return render(request, 'main/welcom.html')

