from django.shortcuts import render
from .models import About

# Create your views here.

def about_detail(request):
    about = About.objects.all().order_by("-updated_on").first()
    return render(request, "about/about_page.html", {"about": about})
    