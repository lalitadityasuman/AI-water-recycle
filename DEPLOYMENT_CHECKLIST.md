# Complete Deployment Checklist

## Pre-Deployment
- [ ] All code committed and pushed to GitHub
- [ ] `.env.example` files created for reference
- [ ] Dockerfiles present in both backend and frontend folders
- [ ] `render.yaml` configuration file created

## Backend Deployment (Render)
- [ ] Render account created and GitHub connected
- [ ] Backend service created with name `recycleai-backend`
- [ ] Root directory set to `backend`
- [ ] Python 3.11 runtime selected
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `gunicorn -w 1 -b 0.0.0.0:$PORT --timeout 120 --worker-class uvicorn.workers.UvicornWorker main:app`
- [ ] Instance type: Free
- [ ] Service deployed successfully
- [ ] Backend URL copied (e.g., `https://recycleai-backend.onrender.com`)

## Backend Configuration
- [ ] Environment variable `PYTHONUNBUFFERED` set to `true`
- [ ] Environment variable `FRONTEND_URL` set to frontend URL
- [ ] Service redeploys after setting variables
- [ ] Logs show no errors

## Frontend Deployment (Render)
- [ ] Frontend service created with name `recycleai-frontend`
- [ ] Root directory set to `frontend`
- [ ] Node runtime selected
- [ ] Build command: `npm install && npm run build`
- [ ] Start command: `npm run preview`
- [ ] Instance type: Free
- [ ] Service deployed successfully
- [ ] Frontend URL copied (e.g., `https://recycleai-frontend.onrender.com`)

## Frontend Configuration
- [ ] Environment variable `VITE_API_URL` set to backend URL
- [ ] Service redeploys after setting variable
- [ ] Logs show no errors

## Testing & Verification
- [ ] Frontend URL loads without errors
- [ ] Browser console shows no JavaScript errors
- [ ] Can navigate between Input, Dashboard, and History pages
- [ ] Can submit waste data via Input form
- [ ] Dashboard displays submitted data
- [ ] History page shows past entries
- [ ] Network tab shows successful API calls (200 status)
- [ ] No CORS errors in browser console

## Production Ready
- [ ] Both services show "Deployed" status
- [ ] Auto-deploy from GitHub is enabled
- [ ] Services are responsive to requests
- [ ] Data persists across page reloads
- [ ] Application is accessible via public URLs

## Monitoring
- [ ] Check service logs regularly
- [ ] Monitor error messages
- [ ] Test application weekly
- [ ] Update code and push to trigger auto-deploy

## Optional Upgrades
- [ ] Consider upgrading from free tier if needed
- [ ] Add custom domain for frontend
- [ ] Set up automated backups for data
- [ ] Add database integration for persistent storage
