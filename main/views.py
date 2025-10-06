from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Skill, Project, Education, PersonalInfo
from .forms import ContactForm


def home(request):
    """Main portfolio view"""
    personal_info = PersonalInfo.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    education = Education.objects.all()
    
    context = {
        'personal_info': personal_info,
        'skills': skills,
        'projects': projects,
        'education': education,
    }
    return render(request, 'main/index.html', context)


def contact(request):
    """Handle contact form submission"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            
            # Send email notification (in production, configure SMTP)
            try:
                send_mail(
                    f'New Contact Form Submission: {contact_message.subject}',
                    f'Name: {contact_message.name}\nEmail: {contact_message.email}\n\nMessage:\n{contact_message.message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                # Log error in production
                pass
            
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('home')
    else:
        form = ContactForm()
    
    return render(request, 'main/index.html', {'contact_form': form})