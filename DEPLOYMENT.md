# RecycleAI Deployment Guide

## Prerequisites
- GitHub account with your code pushed
- Railway account (https://railway.app)
- (Optional) Docker Desktop for local testing

## Local Testing with Docker Compose

Before deploying to Railway, test locally:

\`\`\`bash
docker-compose up --build
\`\`\`

Then visit:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

## Railway Deployment Steps

### Step 1: Connect GitHub to Railway

1. Visit https://railway.app and log in
2. Click "New Project" → "Deploy from GitHub"
3. Authorize Railway to access your GitHub account
4. Select your repository

### Step 2: Deploy Backend Service

1. In Railway dashboard, click "New Service"
2. Select "GitHub Repo" and choose your repository
3. In the service settings:
   - **Name:** recycleai-backend
   - **Root Directory:** `backend/`
4. Click "Deploy"

#### Configure Backend Environment Variables

After deployment starts, go to Variables and add:

| Variable | Value | Notes |
|----------|-------|-------|
| `PORT` | `8000` | Default port |
| `FRONTEND_URL` | `https://<frontend-url>.railway.app` | Add after frontend is deployed |
| `ENV` | `production` | Production environment |

### Step 3: Deploy Frontend Service

1. In the same Railway project, click "New Service"
2. Select "GitHub Repo" and choose your repository
3. In the service settings:
   - **Name:** recycleai-frontend
   - **Root Directory:** `frontend/`
   - **Build Command:** `npm run build`
   - **Start Command:** `serve -s dist -l 3000`

#### Configure Frontend Environment Variables

After deployment starts, go to Variables and add:

| Variable | Value | Notes |
|----------|-------|-------|
| `VITE_API_URL` | `https://<backend-url>.railway.app` | Add after backend is deployed |
| `PORT` | `3000` | Frontend port |

### Step 4: Add Volumes (Data Persistence)

For the backend service:
1. Go to Backend service settings
2. Click "Storage"
3. Add a volume:
   - **Mount Path:** `/app/data`
   - **Size:** 1GB (or more as needed)

This ensures data persists across deployments.

### Step 5: Link Services

In Railway, you can view service URLs:
- Backend URL: Found in Backend service → "View Domain"
- Frontend URL: Found in Frontend service → "View Domain"

Update the environment variables:
- Backend: Update `FRONTEND_URL` to point to your frontend
- Frontend: Update `VITE_API_URL` to point to your backend

Click "Redeploy" on both services to apply changes.

## Troubleshooting

### Backend won't start
- Check logs: Railway Dashboard → Backend Service → Logs
- Verify Python dependencies in `requirements.txt`
- Ensure `gunicorn` is in requirements.txt

### Frontend won't build
- Check build logs in Railway Dashboard
- Verify `npm run build` works locally
- Check that Vite config is correct

### API calls failing
- Verify `VITE_API_URL` is set correctly in frontend
- Check `FRONTEND_URL` in backend CORS settings
- Check browser console for CORS errors

### Data not persisting
- Verify volume is mounted at `/app/data` in backend
- Check that Railway storage is configured
- Data files are created automatically on first use

## GitHub Auto-Deploy

Railway automatically redeploys when you push to GitHub:

\`\`\`bash
git add .
git commit -m "Deploy to Railway"
git push origin main
\`\`\`

No additional action needed!
\`\`\`

```plaintext file="backend/.gitkeep"
# This file ensures the data directory is created
