from django.shortcuts import render
from .models import Project, Message
# Create your views here.


def home(request):
    context = {
    }
    return render(request, "index.html", context)


def contact(request):
    context = {
    }
    return render(request, "contact.html", context)


def services(request):
    context = {
    }
    return render(request, "services.html", context)


def portfolio(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, "portfolio.html", context)


def skills(request):
    context = {
    }
    return render(request, "skills.html", context)


def about(request):
    context = {
    }
    return render(request, "about.html", context)
