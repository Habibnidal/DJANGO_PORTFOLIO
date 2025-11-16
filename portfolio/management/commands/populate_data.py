from django.core.management.base import BaseCommand
from portfolio.models import Profile, Education, Project, SkillCategory, Skill, Certification
from django.core.files import File
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Populates the database with dummy portfolio data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate data...'))
        
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
        if created:
            self.stdout.write(self.style.SUCCESS('Created profile'))
        else:
            self.stdout.write(self.style.WARNING('Profile already exists'))
        
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
            education, created = Education.objects.get_or_create(
                degree=edu_data['degree'],
                institution=edu_data['institution'],
                defaults=edu_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created education: {education.degree}'))
        
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
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created skill category: {category.name}'))
            
            for skill_name in cat_data['skills']:
                skill, created = Skill.objects.get_or_create(
                    category=category,
                    name=skill_name,
                    defaults={'order': 0}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created skill: {skill_name}'))
        
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
            project, created = Project.objects.get_or_create(
                title=proj_data['title'],
                defaults=proj_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created project: {project.title}'))
        
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
            certification, created = Certification.objects.get_or_create(
                title=cert_data['title'],
                defaults=cert_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created certification: {certification.title}'))
        
        self.stdout.write(self.style.SUCCESS('\nSuccessfully populated all data!'))
        self.stdout.write(self.style.SUCCESS('You can now run migrations and start the server.'))


