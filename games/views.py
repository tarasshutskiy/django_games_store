from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def main(request):
    return render(request, 'games/main.html')


def about(request):
    return render(request, 'games/about.html')


def contact(request):
    return render(request, 'games/contact.html')


def post_list(request):
    return render(request, 'games/post_list.html')


def post_detail(request):
    return render(request, 'games/post_detail.html')



