from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/blog_post_category_widget.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}
