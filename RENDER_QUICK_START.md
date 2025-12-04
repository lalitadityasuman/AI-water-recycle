# Quick Start: Deploy RecycleAI to Render

## Prerequisites
- GitHub account with repository containing recycleAI code
- Render.com account (free)

## Step-by-Step Deployment

### 1. Sign Up for Render
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Authorize Render to access your repositories

### 2. Create Backend Service
1. Click "New +" → "Web Service"
2. Select your repository
3. Fill in:
   - **Name:** `recycleai-backend`
   - **Root Directory:** `backend`
   - **Runtime:** Python 3.11
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn -w 1 -b 0.0.0.0:$PORT --timeout 120 --worker-class uvicorn.workers.UvicornWorker main:app`
   - **Instance Type:** Free
4. Click "Create Web Service"
5. Wait for deployment (3-5 minutes)
6. Note your backend URL (e.g., `https://recycleai-backend.onrender.com`)

### 3. Configure Backend Environment Variables
1. Go to backend service settings
2. Click "Environment"
3. Add variable:
   \`\`\`
   FRONTEND_URL=https://recycleai-frontend.onrender.com
   \`\`\`
4. Save - service will redeploy automatically

### 4. Create Frontend Service
1. Click "New +" → "Web Service"
2. Select the same repository
3. Fill in:
   - **Name:** `recycleai-frontend`
   - **Root Directory:** `frontend`
   - **Runtime:** Node
   - **Build Command:** `npm install && npm run build`
   - **Start Command:** `npm run preview`
   - **Instance Type:** Free
4. Click "Create Web Service"
5. Wait for deployment
6. Note your frontend URL (e.g., `https://recycleai-frontend.onrender.com`)

### 5. Configure Frontend Environment Variables
1. Go to frontend service settings
2. Click "Environment"
3. Add variable:
   \`\`\`
   VITE_API_URL=https://recycleai-backend.onrender.com
   \`\`\`
4. Save - service will redeploy

### 6. Verify Deployment
1. Open your frontend URL
2. Try adding waste data
3. Check if it saves and appears in Dashboard
4. Open browser DevTools (F12) → Console to check for errors

## Testing Checklist
- [ ] Frontend loads without errors
- [ ] Can submit waste data
- [ ] Dashboard shows submitted data
- [ ] History page displays entries
- [ ] No CORS errors in browser console
- [ ] API calls show 200 status in Network tab

## Troubleshooting

### Backend not responding
- Check backend service logs in Render dashboard
- Verify FRONTEND_URL is set correctly
- Make sure backend shows "Deployed" status

### Frontend shows "Cannot reach API"
- Verify VITE_API_URL is correct
- Check backend service is running
- Clear browser cache (Ctrl+Shift+Delete)

### Services keep restarting
- Check Render logs for errors
- Verify all environment variables are set
- Try manual redeploy from dashboard

## Important Notes

**Free Tier Limitations:**
- Services spin down after 15 minutes of inactivity
- ~50ms wake-up time when accessed
- Perfect for development and testing
- Upgrade to paid tier for always-on services

**Auto-Deploy from GitHub:**
- Every push to main branch triggers automatic deployment
- Check "Auto-Deploy" is enabled in service settings
- Deployments take 2-5 minutes

## Support
- Render Docs: https://render.com/docs
- Check service logs in Render dashboard for debugging
