# Environment Variables Configuration Guide

## What Are Environment Variables?

Environment variables are configuration values that change between environments (development, production, etc.). They allow the same code to work in different deployments.

## RecycleAI Environment Variables

### Backend Variables

| Variable | Purpose | Development | Production |
|----------|---------|-------------|------------|
| `FRONTEND_URL` | Allow requests from this frontend URL | `http://localhost:5173` | `https://recycleai-frontend.onrender.com` |
| `PORT` | Port to run the backend server | `8000` | `10000` (Render assigned) |
| `PYTHONUNBUFFERED` | Show Python logs in real-time | `true` | `true` |

### Frontend Variables

| Variable | Purpose | Development | Production |
|----------|---------|-------------|------------|
| `VITE_API_URL` | Backend API endpoint | `http://localhost:8000` | `https://recycleai-backend.onrender.com` |

## How to Set Variables in Render

### 1. For Backend Service:

1. Open backend service in Render dashboard
2. Click **"Environment"** tab
3. Click **"Add Environment Variable"** for each:
   \`\`\`
   FRONTEND_URL = https://recycleai-frontend.onrender.com
   PYTHONUNBUFFERED = true
   \`\`\`
4. Click **"Save"**
5. Service automatically redeploys

### 2. For Frontend Service:

1. Open frontend service in Render dashboard
2. Click **"Environment"** tab
3. Click **"Add Environment Variable"**:
   \`\`\`
   VITE_API_URL = https://recycleai-backend.onrender.com
   \`\`\`
4. Click **"Save"**
5. Service automatically redeploys with new build

## Getting Your Render URLs

### Backend URL:
1. Click on backend service
2. Click **"Settings"** or look at service header
3. Copy the domain URL (e.g., `recycleai-backend.onrender.com`)
4. Use: `https://recycleai-backend.onrender.com`

### Frontend URL:
1. Click on frontend service
2. Copy the domain URL
3. Use: `https://recycleai-frontend.onrender.com`

## Important Notes

- **FRONTEND_URL for Backend:** Must be exactly your frontend URL
  - Incorrect value = CORS errors
  - Missing value = API not accessible from frontend

- **VITE_API_URL for Frontend:** Must be your backend URL
  - Used during build time (compile time)
  - Must include `https://` or `http://`
  - No trailing slash

- **Auto-Redeploy:** When you save environment variables, both services redeploy automatically

## Verification

After setting all environment variables:

1. Wait for redeployment to complete
2. Open frontend URL
3. Check browser console (F12) for errors
4. Try submitting data
5. Verify data saves and loads

If you see CORS errors, the FRONTEND_URL in backend is incorrect.
