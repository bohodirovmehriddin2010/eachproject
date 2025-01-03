from django.shortcuts import render
from .models import Flow


def home(request):
    flow = Flow.objects.all()
    context = {
        'flow': flow
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')