from django.core.management.base import BaseCommand
from portfolio.models import Certification
from django.core.files import File
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Uploads certificate images to the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to upload certificates...'))
        
        base_dir = settings.BASE_DIR
        
        # Map certifications to their image files
        cert_files = {
            'YIP(7.O) District winner for project WEAS': 'yip.jpg',
            'Data Mining in python - MES Perinthalmanna Techfest': 'IMG_6124.JPG',
            'Temperature & Mask Scan System - National Techfest': 'IMG_6125.JPG',
            'Volunteer - INQUA Techfest': 'IMG_6126.JPEG',
            'Volunteer - Reviens 4.0 IEEE': 'IMG_6127.JPG',
        }
        
        for cert in Certification.objects.all():
            if cert.title in cert_files:
                cert_filename = cert_files[cert.title]
                cert_path = os.path.join(base_dir, cert_filename)
                if os.path.exists(cert_path) and not cert.certificate_image:
                    with open(cert_path, 'rb') as f:
                        cert.certificate_image.save(cert_filename, File(f), save=True)
                    self.stdout.write(self.style.SUCCESS(f'Uploaded certificate image for {cert.title}'))
        
        self.stdout.write(self.style.SUCCESS('\nSuccessfully uploaded all certificate images!'))

