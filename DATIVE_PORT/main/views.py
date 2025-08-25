# views.py
from django.shortcuts import redirect, render, get_object_or_404
from .models import Project, ResearchPaper, TeamMember, Service, Testimonial, PricingPackage
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

def home(request):
    services = Service.objects.filter(is_active=True)
    featured_projects = Project.objects.filter(featured=True)[:6]
    testimonials = Testimonial.objects.filter(is_approved=True)[:3]
    team_members = TeamMember.objects.filter(is_active=True)
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message to database
            message = form.save()
            
            # Prepare email content
            subject = f"New Contact Form Submission: {form.cleaned_data['subject']}"
            from_email = form.cleaned_data['email']
            message_content = f"""
            Name: {form.cleaned_data['name']}
            Email: {from_email}
            Company: {form.cleaned_data.get('company', 'Not provided')}
            Phone: {form.cleaned_data.get('phone', 'Not provided')}
            Service: {form.cleaned_data.get('service', 'Not specified')}
            Budget: {form.cleaned_data.get('budget', 'Not specified')}
            
            Message:
            {form.cleaned_data['message']}
            """
            
            # Send email
            try:
                send_mail(
                    subject,
                    message_content,
                    from_email,
                    [settings.DEFAULT_FROM_EMAIL],  # Your receiving email
                    fail_silently=False,
                )
                
                # Update message status
                message.status = 'read'
                message.save()
                
                messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
                
            except BadHeaderError:
                messages.error(request, 'Invalid header found.')
            except Exception as e:
                messages.error(request, f'There was an error sending your message: {str(e)}')
                
            return redirect('index')
    else:
        form = ContactForm()
    
    context = {
        'services': services,
        'featured_projects': featured_projects,
        'testimonials': testimonials,
        'team_members': team_members,
        'form': form,
    }
    return render(request, 'index.html', context)

def project_list(request):
    projects = Project.objects.all().order_by('-completion_date')
    return render(request, 'projects.html', {'projects': projects})



def research_list(request):
    papers = ResearchPaper.objects.filter(is_published=True).order_by('-publication_date')
    return render(request, 'research.html', {'papers': papers})
