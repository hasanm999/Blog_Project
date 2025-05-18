from django.shortcuts import render
from django.views.generic import *

from blog.models import *


#

# Create your views here.

def index(request):
    return render(request, "landing_page.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


class BlogListView(ListView):
    model = Post
    template_name = "blog/blog-list.html"
    queryset = Post.objects.filter(post_status=True)
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['posts'] = Post.objects.filter(post_status=True).order_by('-created_at')[:3]
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/blog-single.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.post_views += 1
        obj.save()
        return obj
