# Deployment Guide for Render

This guide will help you deploy your Django portfolio to Render.

## Prerequisites

1. A GitHub account
2. Your code pushed to a GitHub repository
3. A Render account (sign up at https://render.com)

## Step-by-Step Deployment

### 1. Push Your Code to GitHub

If you haven't already, push your code to GitHub:

```bash
git init
git add .
git commit -m "Initial commit - ready for deployment"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

### 2. Create a Render Account

1. Go to https://dashboard.render.com
2. Sign up or log in (you can use your GitHub account)

### 3. Create a New Web Service

1. Click **"New +"** button in the dashboard
2. Select **"Web Service"**
3. Connect your GitHub repository
4. Select the repository containing your Django portfolio

### 4. Configure the Service

Render will auto-detect the `render.yaml` file, but you can also configure manually:

- **Name**: `django-portfolio` (or your preferred name)
- **Environment**: `Python 3`
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn portfolio_project.wsgi:application`
- **Plan**: Free (or choose a paid plan)

### 5. Set Environment Variables

In the Render dashboard, go to **Environment** section and add:

1. **SECRET_KEY**: 
   - Click "Generate" or use: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
   - Or let Render auto-generate it (already configured in render.yaml)

2. **DEBUG**: Set to `False`

3. **ALLOWED_HOSTS**: 
   - After deployment, Render will give you a URL like `your-app.onrender.com`
   - Set this to: `your-app.onrender.com` (replace with your actual URL)
   - You can add multiple hosts separated by commas if needed

### 6. Deploy

1. Click **"Create Web Service"**
2. Render will start building and deploying your application
3. Wait for the build to complete (usually 2-5 minutes)

### 7. Post-Deployment Setup

After successful deployment:

1. **Create a superuser** (for admin access):
   - Go to Render dashboard → Your service → Shell
   - Run: `python manage.py createsuperuser`
   - Follow the prompts

2. **Populate initial data** (if needed):
   ```bash
   python manage.py populate_data
   python manage.py upload_images
   python manage.py upload_certificates
   ```

3. **Access your site**:
   - Your portfolio: `https://your-app.onrender.com`
   - Admin panel: `https://your-app.onrender.com/admin/`

## Important Notes

### Media Files

⚠️ **Important**: On Render's free tier, the filesystem is **ephemeral**. This means:
- Files uploaded through the admin panel will be **lost** when the service restarts
- Files committed to your repository (in `media/` folder) will persist
- For production, consider using cloud storage:
  - AWS S3
  - Cloudinary
  - Google Cloud Storage

### Database

- Currently using SQLite (fine for small projects)
- For production with user uploads, consider PostgreSQL:
  - Render offers free PostgreSQL databases
  - Update `DATABASES` in `settings.py` to use PostgreSQL

### Static Files

- Static files are handled by WhiteNoise
- They are collected during build and served automatically
- No additional configuration needed

## Troubleshooting

### Build Fails

1. Check build logs in Render dashboard
2. Ensure all dependencies are in `requirements.txt`
3. Verify Python version matches `runtime.txt`

### 500 Error After Deployment

1. Check environment variables are set correctly
2. Verify `ALLOWED_HOSTS` includes your Render URL
3. Check application logs in Render dashboard

### Static Files Not Loading

1. Ensure `collectstatic` runs during build (included in `build.sh`)
2. Check WhiteNoise is properly configured in `settings.py`

### Media Files Not Showing

1. Verify media files are committed to your repository
2. Check `MEDIA_ROOT` and `MEDIA_URL` settings
3. For uploaded files, use cloud storage (see Media Files section above)

## Updating Your Deployment

1. Push changes to your GitHub repository
2. Render will automatically redeploy (if `autoDeploy: true` is set)
3. Or manually trigger deployment from Render dashboard

## Support

- Render Documentation: https://render.com/docs
- Django Deployment: https://docs.djangoproject.com/en/stable/howto/deployment/

