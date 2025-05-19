from django.shortcuts import render
from django.views.generic import *
from .forms import ContactForm
from blog.models import *


#

# Create your views here.

def index(request):
    return render(request, "landing_page.html")


def about(request):
    return render(request, "about.html")


# def contact(request):
#     return render(request, "contact.html")


class BlogListView(ListView):
    model = Post
    template_name = "blog/blog-list.html"
    context_object_name = "posts"
    paginate_by = 10  # اضافه کردن pagination

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['recent_posts'] = Post.objects.filter(post_status=True).order_by('-created_at')[:3]
        return context

    def get_queryset(self):
        queryset = super().get_queryset().filter(post_status=True)

        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        category = self.kwargs.get("category")
        if category:
            queryset = queryset.filter(category__name=category)

        author = self.kwargs.get("author")
        if author:
            queryset = queryset.filter(author__user__username=author)

        tag = self.kwargs.get("tag")
        if tag:
            queryset = queryset.filter(tags__name=tag)

        return queryset.order_by('-created_at')


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/blog-single.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.post_views += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/contact/"

    def form_valid(self, form):
        Contact.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            subject=form.cleaned_data['subject'],
            message=form.cleaned_data['message']
        )
        return super().form_valid(form)


class SearchView(ListView):
    model = Post
    queryset = Post.objects.filter(title__icontains='title')
    template_name = "blog/blog_search_widget.html"
