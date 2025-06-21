from django.shortcuts import render, redirect
from .models import ContactMessage

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(name=name, email=email, message=message)
        return redirect('success')

    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')
