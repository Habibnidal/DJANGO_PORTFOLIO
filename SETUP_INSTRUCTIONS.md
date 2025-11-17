# Setup Instructions for Render (Free Tier - No Shell Access)

Since Render's free tier doesn't provide shell access, use this URL endpoint to populate your database.

## Quick Setup (One-Time)

### Step 1: Visit the Setup URL

After your site is deployed on Render, visit this URL in your browser:

```
https://your-app.onrender.com/setup-data/?key=setup123
```

**Replace `your-app.onrender.com` with your actual Render URL.**

### Step 2: Check the Response

You should see a success message:
```
✅ Data populated successfully! Your portfolio should now display correctly.
```

### Step 3: Refresh Your Site

Visit your main site: `https://your-app.onrender.com`

You should now see:
- **"Habib Nidal"** instead of "Your Name"
- All your education, projects, skills, and certifications

## What Gets Created

The setup endpoint creates:
- ✅ Profile (Habib Nidal with all your details)
- ✅ Education records (3 entries)
- ✅ Projects (3 entries)
- ✅ Skill Categories (6 categories)
- ✅ Skills (23 skills)
- ✅ Certifications (5 entries)

## Security Note

The default key is `setup123`. For better security:

1. **Set a custom key in Render Environment Variables:**
   - Go to Render Dashboard → Your Service → Environment
   - Add: `SETUP_KEY` = `your-secret-key-here`
   - Then use: `https://your-app.onrender.com/setup-data/?key=your-secret-key-here`

2. **After setup, you can remove this endpoint** by deleting the `setup_data` view and URL from your code.

## Troubleshooting

### "Unauthorized" Error
- Make sure you're using the correct key: `?key=setup123`
- Or set `SETUP_KEY` environment variable in Render

### "Data already exists" Message
- The database already has data
- If you want to reset, delete data from admin panel first: `https://your-app.onrender.com/admin/`

### Still seeing "Your Name"
- Make sure the setup was successful (check the response message)
- Clear your browser cache
- Check that migrations ran: The database tables should exist

## Alternative: Use Admin Panel

If the setup endpoint doesn't work, you can manually add data:

1. Create a superuser (if you haven't):
   - You'll need to do this locally or find another way
   - Or use Render's database directly if you have access

2. Go to: `https://your-app.onrender.com/admin/`
3. Add a Profile record with your information
4. Add Education, Projects, Skills, and Certifications

## After Setup

Once your data is populated, you can:
- ✅ Remove the setup endpoint for security (optional)
- ✅ Update data through the admin panel
- ✅ Your site will display all your information correctly

---

**Note:** This is a one-time setup. After running it successfully, your portfolio will display all your data!

