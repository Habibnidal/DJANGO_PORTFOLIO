# How to Populate Data on Render

Your database on Render is empty, which is why "Your Name" is showing instead of your actual data.

## Solution: Run the populate_data command

### Step 1: Access Render Shell

1. Go to your Render Dashboard: https://dashboard.render.com
2. Click on your **django-portfolio** service
3. Click on the **"Shell"** tab (or look for "Open Shell" button)
4. This will open a terminal connected to your Render instance

### Step 2: Run the populate_data command

In the Render Shell, run:

```bash
python manage.py populate_data
```

This will create:
- Your profile (Habib Nidal)
- Education records
- Projects
- Skills and Skill Categories
- Certifications

### Step 3: (Optional) Upload Images

If you want to upload images and certificates:

```bash
python manage.py upload_images
python manage.py upload_certificates
```

### Step 4: Verify

1. Visit your site: `https://your-app.onrender.com`
2. You should now see "Habib Nidal" instead of "Your Name"
3. All your data should be displayed

## Alternative: Use Admin Panel

If you prefer to add data manually:

1. Create a superuser (if you haven't already):
   ```bash
   python manage.py createsuperuser
   ```

2. Go to: `https://your-app.onrender.com/admin/`
3. Log in with your superuser credentials
4. Add a Profile record with your information:
   - Name: Habib Nidal
   - Title: Computer Science Engineer | Python Fullstack Developer | Data Analyst
   - Bio: Your bio text
   - Email: habibnidal2003@gmail.com
   - Phone: +917306020083
   - LinkedIn URL: https://www.linkedin.com/in/habibnidal
   - GitHub URL: https://github.com/Habibnidal
5. Add Education, Projects, Skills, and Certifications as needed

## Quick Fix Command

Run this single command in Render Shell to populate everything:

```bash
python manage.py populate_data && python manage.py upload_images && python manage.py upload_certificates
```

---

**Note:** After running these commands, your site should display all your actual data instead of placeholder text.

