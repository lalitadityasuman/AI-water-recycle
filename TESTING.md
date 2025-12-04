# RecycleAI Testing Guide

## Environment Variables Summary

### Backend Environment Variables
\`\`\`env
PORT=8000
FRONTEND_URL=https://your-frontend.railway.app
ENV=production
\`\`\`

### Frontend Environment Variables
\`\`\`env
VITE_API_URL=https://your-backend.railway.app
\`\`\`

## Pre-Deployment Testing (Local)

### 1. Local Setup
\`\`\`bash
# Clone/navigate to your project
cd recycleAI

# Test with Docker Compose
docker-compose up --build
\`\`\`

### 2. Test Backend APIs

Open a terminal and test these endpoints:

\`\`\`bash
# Add usage data
curl -X POST http://localhost:8000/usage \
  -H "Content-Type: application/json" \
  -d '{
    "shower": 50,
    "washing_machine": 40,
    "bathroom_sink": 10,
    "kitchen_sink": 5
  }'

# Get greywater total
curl http://localhost:8000/greywater

# Get coins earned
curl http://localhost:8000/coins

# Get recommendation
curl http://localhost:8000/recommendation

# Analyze water quality
curl -X POST http://localhost:8000/analyze-water \
  -H "Content-Type: application/json" \
  -d '{
    "turbidity": 5.0,
    "pH": 7.0,
    "tds": 300,
    "temperature": 25
  }'

# Get analysis summary
curl http://localhost:8000/analysis-summary

# Get history
curl http://localhost:8000/history
\`\`\`

### 3. Test Frontend

Open browser to http://localhost:3000 and test:

- [ ] **Input Page** - Submit water usage data
- [ ] **Dashboard Page** - View greywater stats and coins
- [ ] **History Page** - See usage history
- [ ] **Navigation** - All links work correctly
- [ ] **Console** - No errors in browser console

## Post-Deployment Testing (Railway)

### 1. Verify Deployments

- Backend: Visit `https://<backend-service>.railway.app/docs` (FastAPI docs)
- Frontend: Visit `https://<frontend-service>.railway.app`

### 2. Test API Connectivity

Open browser console and check:
\`\`\`javascript
// In browser console at frontend URL
fetch('https://<backend-service>.railway.app/history')
  .then(r => r.json())
  .then(d => console.log('Backend connected!', d))
  .catch(e => console.error('Backend error:', e))
\`\`\`

### 3. Complete Functionality Test

Navigate to each page and verify:

**Input Page:**
- [ ] Fill in water usage values
- [ ] Click Submit
- [ ] See success message
- [ ] Check browser console for no errors

**Dashboard Page:**
- [ ] See greywater total
- [ ] See coins earned
- [ ] See recommendation text
- [ ] See latest water analysis (if available)

**History Page:**
- [ ] See list of all submissions
- [ ] Data is persistent after refresh
- [ ] Dates are formatted correctly

### 4. Data Persistence Test

1. Submit data on Input page
2. Refresh the page
3. Go to Dashboard - verify data still shows
4. Close browser completely
5. Reopen and visit Dashboard - data should persist

## Troubleshooting

### Issue: "API not reachable" / CORS errors

**Solution:**
1. Check frontend logs for correct VITE_API_URL
2. Verify backend FRONTEND_URL matches frontend deployment URL
3. Redeploy both services after updating env vars
4. Check browser console for exact error

### Issue: Data not saving

**Solution:**
1. Check backend logs in Railway dashboard
2. Verify `/app/data` volume is mounted
3. Check that POST requests return success (200/201 status)
4. Verify write permissions on volume

### Issue: Slow page loads

**Solution:**
1. Check Railway service logs for errors
2. Verify both services are in "Running" state
3. Consider upgrading Railway plan if needed
4. Check network tab in browser DevTools

### Issue: Frontend build fails on Railway

**Solution:**
1. Verify `npm run build` works locally
2. Check Node.js version matches (20+)
3. Verify all dependencies in package.json
4. Check Railway build logs for specific errors

## Performance Monitoring

On Railway dashboard, monitor:
- CPU usage
- Memory usage
- Build times
- Deployment status

## Final Verification Checklist

- [ ] Backend service deployed and running
- [ ] Frontend service deployed and running
- [ ] Environment variables configured
- [ ] CORS properly configured
- [ ] API endpoints responding
- [ ] Frontend can communicate with backend
- [ ] Data persists after refresh
- [ ] All pages load without errors
- [ ] No console errors
- [ ] Forms submit successfully
- [ ] Application ready for production

If all checks pass, your deployment is complete!
\`\`\`
