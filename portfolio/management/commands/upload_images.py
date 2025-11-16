from django.core.management.base import BaseCommand
from portfolio.models import Profile, Project
from django.core.files import File
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Uploads existing images and videos to the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to upload images...'))
        
        base_dir = settings.BASE_DIR
        
        # Update Profile with images
        profile = Profile.objects.first()
        if profile:
            # Profile image
            profile_img_path = os.path.join(base_dir, 'port2-removebg-preview.png')
            if os.path.exists(profile_img_path) and not profile.profile_image:
                with open(profile_img_path, 'rb') as f:
                    profile.profile_image.save('port2-removebg-preview.png', File(f), save=True)
                self.stdout.write(self.style.SUCCESS('Uploaded profile image'))
            
            # Background image
            bg_img_path = os.path.join(base_dir, 'back.jpg')
            if os.path.exists(bg_img_path) and not profile.background_image:
                with open(bg_img_path, 'rb') as f:
                    profile.background_image.save('back.jpg', File(f), save=True)
                self.stdout.write(self.style.SUCCESS('Uploaded background image'))
            
            # Resume
            resume_path = os.path.join(base_dir, 'Habib_Nidal_Resume.pdf')
            if os.path.exists(resume_path) and not profile.resume:
                with open(resume_path, 'rb') as f:
                    profile.resume.save('Habib_Nidal_Resume.pdf', File(f), save=True)
                self.stdout.write(self.style.SUCCESS('Uploaded resume'))
        
        # Update Projects with videos
        projects = Project.objects.all()
        video_files = {
            'College Space Parking Management System': 'IMG_6118.MP4',
            'Wearable Emergency Alert System': 'IMG_6009.mp4',
            'Shopping App for Dresses': 'dressvideo.MOV',
        }
        
        for project in projects:
            if project.title in video_files:
                video_filename = video_files[project.title]
                video_path = os.path.join(base_dir, video_filename)
                if os.path.exists(video_path) and not project.video:
                    with open(video_path, 'rb') as f:
                        project.video.save(video_filename, File(f), save=True)
                    self.stdout.write(self.style.SUCCESS(f'Uploaded video for {project.title}'))
        
        self.stdout.write(self.style.SUCCESS('\nSuccessfully uploaded all images and videos!'))

