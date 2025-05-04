from django.shortcuts import render
from django.views.generic import *

from blog.models import Post


#

# Create your views here.

def index(request):
    return render(request, "landing_page.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


# def blog_list(request):
#     return render(request, "blog/blog-list.html")


class BlogListView(ListView):
    model = Post
    template_name = "blog/blog-list.html"
    queryset = Post.objects.filter(post_status=True)
    context_object_name = "posts"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/blog-single.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.post_views += 1
        obj.save()
        return obj
