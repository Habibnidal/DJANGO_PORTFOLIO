from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Education, Project, SkillCategory, Certification, ContactMessage

def home(request):
    try:
        profile = Profile.objects.first()
    except:
        profile = None
    
    educations = Education.objects.all()
    projects = Project.objects.all()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    certifications = Certification.objects.all()
    
    context = {
        'profile': profile,
        'educations': educations,
        'projects': projects,
        'skill_categories': skill_categories,
        'certifications': certifications,
    }
    return render(request, 'portfolio/index.html', context)

def contact_submit(request):
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
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return redirect('home')
