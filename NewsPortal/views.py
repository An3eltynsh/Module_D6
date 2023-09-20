from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class NewsList(ListView):
    #model = Post
    #ordering = 'dtime_p'
    queryset = Post.objects.filter(choice = 'N').order_by('dtime_p').values('title', 'dtime_p', 'text_p')
    template_name = 'news.html'
    context_object_name = 'news'

class NewDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

class PublicationsList(ListView):
    model = Post
    ordering = 'dtime_p'
    template_name = 'publications.html'
    context_object_name = 'publications'