# RecycleAI - Render.com Deployment Guide

## Overview
This guide will help you deploy RecycleAI (FastAPI backend + Vue.js frontend) on Render.com completely free.

**What You'll Get:**
- FastAPI backend running on free tier
- Vue.js frontend hosted on free tier
- Automatic deployments from GitHub
- Free SSL certificates
- No credit card required for free tier

---

## Step 1: Create Render Account and Connect GitHub

### 1.1 Sign Up for Render
1. Go to [render.com](https://render.com)
2. Click "Get Started"
3. Sign up with your GitHub account (recommended)
4. Authorize Render to access your repositories

### 1.2 Create a New Project
1. After login, click "New +" → "Web Service"
2. Select your GitHub repository containing recycleAI
3. Click "Connect"

---

## Step 2: Deploy Backend Service

### 2.1 Create Backend Service
1. **Service Details:**
   - **Name:** `recycleai-backend`
   - **Root Directory:** `backend`
   - **Runtime:** Python 3.11
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT`
   - **Instance Type:** Free

2. **Click "Create Web Service"**

### 2.2 Wait for Initial Deployment
- Render will build and deploy your backend
- Monitor the deployment logs
- Once deployed, you'll get a URL like: `https://recycleai-backend.onrender.com`

### 2.3 Configure Backend Environment Variables
1. Go to your backend service
2. Click on "Environment"
3. Add these environment variables:

\`\`\`
FRONTEND_URL=https://recycleai-frontend.onrender.com
PORT=10000
PYTHONUNBUFFERED=true
\`\`\`

4. Click "Save Changes"
5. The service will redeploy with new variables

---

## Step 3: Deploy Frontend Service

### 3.1 Create Frontend Service
1. Go back to Dashboard
2. Click "New +" → "Web Service"
3. Select the same GitHub repository
4. Click "Connect"

**Service Details:**
- **Name:** `recycleai-frontend`
- **Root Directory:** `frontend`
- **Runtime:** Node
- **Build Command:** `npm install && npm run build`
- **Start Command:** `npm run preview` (or use `serve -s dist`)
- **Instance Type:** Free

2. **Click "Create Web Service"**

### 3.2 Wait for Initial Deployment
- Render will build and deploy your frontend
- Once deployed, you'll get a URL like: `https://recycleai-frontend.onrender.com`

---

## Step 4: Configure Environment Variables

### 4.1 Update Frontend Environment Variables
1. Go to your frontend service
2. Click on "Environment"
3. Add this environment variable:

\`\`\`
VITE_API_URL=https://recycleai-backend.onrender.com
\`\`\`

4. Click "Save Changes"
5. The frontend will rebuild and redeploy

### 4.2 Update Backend FRONTEND_URL
1. Go back to backend service
2. Update the `FRONTEND_URL` environment variable to match your actual frontend URL
3. Save and redeploy

---

## Step 5: Test Your Application

### 5.1 Verify Deployment
1. Open your frontend URL: `https://recycleai-frontend.onrender.com`
2. Check the browser console for any errors
3. Try adding some waste data
4. Verify it saves and shows in Dashboard
5. Check History page

### 5.2 Monitor Logs
- In Render dashboard, click your service
- View "Logs" to see any errors
- Use browser DevTools Console tab to debug frontend issues

### 5.3 Check Backend Connectivity
- Open frontend → open Browser DevTools (F12)
- Go to Network tab
- Try submitting data
- Look for API calls to your backend
- Check if requests return 200 status (success)

---

## Common Issues & Solutions

### Issue: Frontend shows "API Error" or blank page
**Solution:**
1. Check `VITE_API_URL` is correctly set in frontend environment
2. Verify backend service is running (check Render dashboard)
3. Open browser console and look for CORS errors
4. Restart both services: click "Manual Deploy" in Render

### Issue: Backend service keeps restarting
**Solution:**
1. Check deployment logs for errors
2. Verify `requirements.txt` has all dependencies
3. Ensure `main.py` is in the root of `backend/` folder
4. Try redeploying manually

### Issue: "Free tier spinning down" - App goes slow after inactivity
**Note:** This is normal on Render's free tier. Services spin down after 15 minutes of inactivity. When you visit, they wake up (takes ~30 seconds). Consider upgrading if you need always-on services.

---

## Important Notes

### Free Tier Limitations:
- Services spin down after 15 minutes of inactivity
- Limited to 0.5 CPU and 512MB RAM
- Perfect for development and testing
- Can upgrade anytime if needed

### GitHub Auto-Deploy
- Every time you push to GitHub, Render automatically redeploys
- Check "Auto-Deploy" in service settings (should be ON by default)
- Deployments take 2-5 minutes

### Data Persistence
- Backend data is stored in `data/water_usage.json`
- On free tier, files persist but are not guaranteed between restarts
- For production, consider upgrading or using a database

---

## Deployment Checklist

- [ ] GitHub account connected to Render
- [ ] Repository pushed to GitHub with all files
- [ ] Backend service created with `backend/` root
- [ ] Frontend service created with `frontend/` root
- [ ] Backend environment variables set (FRONTEND_URL, PORT)
- [ ] Frontend environment variables set (VITE_API_URL)
- [ ] Both services deployed successfully
- [ ] Frontend loads without errors
- [ ] Backend is responding to API calls
- [ ] Data saves and loads correctly
- [ ] Dashboard shows submitted data
- [ ] History page shows past entries

---

## Next Steps

1. Monitor your services in Render dashboard
2. Check logs if anything goes wrong
3. Push code changes - they'll auto-deploy
4. Share your live URLs with others
5. When ready for production, consider upgrading to paid tier or adding a database

---

## Getting Your Live URLs

After both services are deployed:
- **Frontend:** Go to frontend service → Custom Domain section
- **Backend:** Go to backend service → Custom Domain section

Copy these URLs to share your app!
