from django.shortcuts import render
from django.views.generic import ListView


def start_page(request):
    return render(request, 'main/start_page.html')

def welcom(request):
    return render(request, 'main/welcom.html')

def main(requset):
    return render(requset, 'main/main.html')

def words(request):
    return render(request, 'main/word.html')

