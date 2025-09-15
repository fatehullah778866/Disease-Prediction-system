from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def prediction(request):
    return render(request, "prediction.html")

def home(request):
    return render(request, "home.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('dashboard:contact')
        else:
            messages.error(request, 'Please fill in all the fields.')

    return render(request, 'contact.html')


def about(request):
    return render(request, "about.html")




