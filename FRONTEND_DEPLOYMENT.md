# Frontend Deployment on Render - Detailed Guide

## Overview
Deploy your Vue.js RecycleAI frontend to Render with automatic GitHub integration.

## Prerequisites
- Backend service already deployed on Render
- Backend URL noted (e.g., `https://recycleai-backend.onrender.com`)
- GitHub repository with frontend code pushed

## Frontend Deployment Steps

### 1. Create Frontend Web Service

**In Render Dashboard:**

1. Click **"New +"** button (top right)
2. Select **"Web Service"**
3. Select your GitHub repository
4. Click **"Connect"**

### 2. Configure Frontend Service

Fill in the service configuration:

| Field | Value |
|-------|-------|
| **Name** | `recycleai-frontend` |
| **Root Directory** | `frontend` |
| **Runtime** | Node |
| **Build Command** | `npm install && npm run build` |
| **Start Command** | `npm run preview` |
| **Instance Type** | Free |

### 3. Important: Build Command Explanation

The build command creates an optimized production build:
\`\`\`bash
npm install && npm run build
\`\`\`

This will:
1. Install all dependencies from `package.json`
2. Build Vue.js app with Vite (output to `dist/` folder)
3. Optimize assets for production

The start command then serves this built app:
\`\`\`bash
npm run preview
\`\`\`

### 4. Wait for Initial Build

- Render will start building your frontend
- Check **Logs** tab to monitor progress
- Build takes 2-5 minutes
- Wait for "Deployment successful" message
- Copy your **Frontend URL** (e.g., `https://recycleai-frontend.onrender.com`)

### 5. Add Environment Variables

Once deployed, add the API URL:

1. Click on your frontend service
2. Go to **Environment** tab
3. Click **"Add Environment Variable"**
4. Enter:
   - **Key:** `VITE_API_URL`
   - **Value:** `https://recycleai-backend.onrender.com`
5. Click **"Save"**

**Important:** The service will automatically redeploy with the new variable.

### 6. Verify Deployment

After redeployment completes:

1. Open your frontend URL in browser
2. Check browser console (F12) for any errors
3. Try the following:
   - Navigate between pages (Input, Dashboard, History)
   - Submit waste data in the Input page
   - Check if data appears in Dashboard
   - Verify History page shows saved entries

## What Happens During Build

1. **npm install** - Downloads Vue.js, Axios, Vue Router, and all dependencies
2. **npm run build** - Compiles Vue components into optimized HTML/CSS/JS
3. **Service starts** - Runs `npm run preview` to serve the built app

The `dist/` folder created during build contains your entire app ready for production.

## Troubleshooting

### Build Fails - "Cannot find module"
- Check `package.json` has all dependencies
- Verify Node version is compatible
- Try redeploying from Render dashboard

### Frontend loads but shows "Cannot reach API"
- Verify `VITE_API_URL` environment variable is set
- Check backend service is running (not "Deploy failed")
- Make sure API URL doesn't have trailing slash
- Clear browser cache (Ctrl+Shift+Delete)

### Blank white page
- Open browser console (F12)
- Look for JavaScript errors
- Check Network tab to verify files are loading
- Verify all environment variables are set

### Services keep restarting
- Check service logs for errors
- Verify all environment variables are correct
- Ensure backend is accessible

## Performance Notes

**Free Tier:**
- Services spin down after 15 minutes of inactivity
- First request takes ~30 seconds (spin-up time)
- Perfect for development and testing
- After first request, response time is normal

**To Keep Services Warm:**
- Services stay active if you access them regularly
- No additional cost on free tier

## Next Steps

1. Verify both services are deployed and running
2. Test the full application flow
3. Share the frontend URL with users
4. Monitor logs for any issues
5. Consider upgrading if you need always-on services
