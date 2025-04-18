from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "landing_page.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
