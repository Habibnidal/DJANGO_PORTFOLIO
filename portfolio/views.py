from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile, Education, Project, SkillCategory, Skill, Certification, ContactMessage
import os

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

def setup_data(request):
    """
    One-time setup endpoint to populate database with portfolio data.
    Access via: /setup-data/?key=YOUR_SECRET_KEY
    """
    # Simple security check - use a secret key from environment or default
    secret_key = os.environ.get('SETUP_KEY', 'setup123')
    provided_key = request.GET.get('key', '')
    
    if provided_key != secret_key:
        return HttpResponse('Unauthorized. Provide correct key parameter.', status=403)
    
    # Check if data already exists
    if Profile.objects.exists():
        return HttpResponse('Data already exists! If you want to reset, delete existing data first from admin panel.', status=200)
    
    try:
        # Create Profile
        profile, created = Profile.objects.get_or_create(
            name='Habib Nidal',
            defaults={
                'title': 'Computer Science Engineer | Python Fullstack Developer | Data Analyst',
                'bio': 'I\'m a passionate Computer Science Engineer from Kerala with a deep interest in fullstack development, App developing and data analytics. I love contributing to innovative projects and aim to build robust and smart solutions.',
                'email': 'habibnidal2003@gmail.com',
                'phone': '+917306020083',
                'linkedin_url': 'https://www.linkedin.com/in/habibnidal',
                'github_url': 'https://github.com/Habibnidal',
            }
        )
        
        # Create Education
        educations_data = [
            {
                'degree': 'B.Tech - Computer Science',
                'institution': 'College of Engineering Trikaripur',
                'start_year': 2021,
                'end_year': 2025,
                'order': 1
            },
            {
                'degree': 'HSE',
                'institution': 'St Michaels AIHSS Kannur',
                'start_year': 2019,
                'end_year': 2021,
                'order': 2
            },
            {
                'degree': 'SSLC',
                'institution': 'St Michaels AIHSS Kannur',
                'start_year': 2019,
                'end_year': None,
                'order': 3
            },
        ]
        
        for edu_data in educations_data:
            Education.objects.get_or_create(
                degree=edu_data['degree'],
                institution=edu_data['institution'],
                defaults=edu_data
            )
        
        # Create Skill Categories and Skills
        skill_categories_data = [
            {
                'name': 'Languages',
                'skills': ['Python', 'C', 'JavaScript'],
                'order': 1
            },
            {
                'name': 'Web Technologies',
                'skills': ['HTML', 'CSS', 'JavaScript', 'Flutter'],
                'order': 2
            },
            {
                'name': 'Database',
                'skills': ['SQL', 'SQLAlchemy', 'Oracle'],
                'order': 3
            },
            {
                'name': 'Tools',
                'skills': ['VS Code', 'PyCharm', 'SQLplus', 'Canva', 'Excel', 'Word', 'Power BI'],
                'order': 4
            },
            {
                'name': 'Libraries',
                'skills': ['NumPy', 'Pandas', 'React'],
                'order': 5
            },
            {
                'name': 'Frameworks',
                'skills': ['Django', 'Flask', 'Tailwind CSS'],
                'order': 6
            },
        ]
        
        for cat_data in skill_categories_data:
            category, created = SkillCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults={'order': cat_data['order']}
            )
            
            for skill_name in cat_data['skills']:
                Skill.objects.get_or_create(
                    category=category,
                    name=skill_name,
                    defaults={'order': 0}
                )
        
        # Create Projects
        projects_data = [
            {
                'title': 'College Space Parking Management System',
                'description': 'Developed using HTML, CSS, JS, PHP and MySQL. Handled frontend and presentation duties.',
                'technologies': 'HTML, CSS, JavaScript, PHP, MySQL',
                'github_link': 'https://github.com/Habibnidal/College-Parking-Management',
                'live_link': '',
                'order': 1
            },
            {
                'title': 'Wearable Emergency Alert System',
                'description': 'Uses Raspberry Pi, GPS, Microphone and Flutter frontend with Flask backend. Created for emergency live monitoring.',
                'technologies': 'Raspberry Pi, GPS, Flutter, Flask, Python',
                'github_link': 'https://github.com/Habibnidal/WEAS',
                'live_link': '',
                'order': 2
            },
            {
                'title': 'Shopping App for Dresses',
                'description': 'Designed a complete e-commerce web and mobile app with HTML, CSS, JavaScript, Flask, Flutter, deployed on Render',
                'technologies': 'HTML, CSS, JavaScript, Flask, Flutter',
                'github_link': '',
                'live_link': 'https://digidress.onrender.com',
                'order': 3
            },
        ]
        
        for proj_data in projects_data:
            Project.objects.get_or_create(
                title=proj_data['title'],
                defaults=proj_data
            )
        
        # Create Certifications
        certifications_data = [
            {
                'title': 'YIP(7.O) District winner for project WEAS',
                'issuer': 'YIP',
                'order': 1
            },
            {
                'title': 'Data Mining in python - MES Perinthalmanna Techfest',
                'issuer': 'MES Perinthalmanna',
                'order': 2
            },
            {
                'title': 'Temperature & Mask Scan System - National Techfest',
                'issuer': 'National Techfest',
                'order': 3
            },
            {
                'title': 'Volunteer - INQUA Techfest',
                'issuer': 'INQUA Techfest',
                'order': 4
            },
            {
                'title': 'Volunteer - Reviens 4.0 IEEE',
                'issuer': 'IEEE',
                'order': 5
            },
        ]
        
        for cert_data in certifications_data:
            Certification.objects.get_or_create(
                title=cert_data['title'],
                defaults=cert_data
            )
        
        return HttpResponse('✅ Data populated successfully! Your portfolio should now display correctly. You can delete this endpoint after setup.', status=200)
        
    except Exception as e:
        return HttpResponse(f'Error: {str(e)}', status=500)
