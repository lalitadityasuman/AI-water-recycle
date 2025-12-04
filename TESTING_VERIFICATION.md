# Testing & Verification Guide

## Step-by-Step Testing Process

### 1. Verify Both Services Are Deployed

**Backend:**
1. Go to your Render dashboard
2. Click on `recycleai-backend` service
3. Verify status shows **"Live"** or **"Deployed"**
4. Check Logs tab for any errors
5. Copy and save your backend URL

**Frontend:**
1. Click on `recycleai-frontend` service
2. Verify status shows **"Live"** or **"Deployed"**
3. Check Logs tab for any errors
4. Copy and save your frontend URL

### 2. Test Frontend Loads

1. Open your frontend URL in a web browser
2. You should see the RecycleAI dashboard
3. Check for any error messages
4. Open **Browser DevTools** (F12)
   - Go to **Console** tab
   - Look for red error messages
   - Common issue: API connection errors

### 3. Check Environment Variables

**Check Frontend Variable:**
1. In your browser console, type:
   \`\`\`javascript
   console.log(import.meta.env.VITE_API_URL)
   \`\`\`
2. Should show: `https://recycleai-backend.onrender.com`
3. If empty or undefined, the variable wasn't set correctly

**Check Backend Logs:**
1. Go to backend service in Render
2. Click **Logs**
3. Look for lines showing the API is running
4. Should show something like: `INFO: Uvicorn running...`

### 4. Test API Connectivity

**Using Browser Network Tab:**
1. Open DevTools (F12)
2. Go to **Network** tab
3. In your frontend, try any action (submit data, go to dashboard)
4. Look for API calls to your backend
5. Check the status code:
   - **200** = Success
   - **404** = Not found
   - **CORS error** = Backend FRONTEND_URL not set correctly
   - **Connection refused** = Backend not running

### 5. Complete Application Test Flow

Follow this exact flow to verify everything works:

#### Test Input Page:
1. Navigate to "Input" page
2. Fill in test data:
   - Shower: 50
   - Washing Machine: 30
   - Bathroom Sink: 20
   - Kitchen Sink: 10
3. Click "Add Usage"
4. Look for success message
5. Check browser console for errors

#### Test Dashboard Page:
1. Navigate to "Dashboard" page
2. Should display:
   - Greywater total (should show the amount from your input)
   - Recycle coins (should be calculated)
   - Recommendations
   - Latest analysis summary
3. If blank, data didn't save properly

#### Test History Page:
1. Navigate to "History" page
2. Should show a list of all submitted entries
3. Should show the entry you just added
4. Each entry should show date and values

#### Test Water Analysis (if available):
1. Navigate to any analysis page
2. Fill in water quality metrics:
   - Turbidity: 2.5
   - pH: 7.0
   - TDS: 500
   - Temperature: 25
3. Submit and verify it saves

### 6. Network Debugging

If API calls fail:

**Check CORS Errors:**
1. Console shows: `Access to XMLHttpRequest blocked by CORS policy`
2. Solution: Update backend's `FRONTEND_URL` to match frontend URL exactly

**Check Network Errors:**
1. Network tab shows red (connection error)
2. Solution: Verify backend is running (check Render logs)

**Check 404 Errors:**
1. Network shows 404 status
2. Solution: Verify endpoint paths are correct in API service

### 7. Testing Checklist

Run through all these checks:

- [ ] Frontend URL opens without errors
- [ ] Browser console has no red errors
- [ ] Can navigate between all pages
- [ ] Can submit waste data successfully
- [ ] Dashboard updates with new data
- [ ] History page shows saved entries
- [ ] Network tab shows 200 status codes
- [ ] No CORS errors in console
- [ ] API URL is correctly configured
- [ ] Backend service shows as "Deployed"

## Troubleshooting Failed Tests

### Issue: "Cannot reach API" or "API Error"

**Check:**
1. Backend service status in Render
2. VITE_API_URL environment variable (frontend)
3. FRONTEND_URL environment variable (backend)
4. Browser console for specific errors
5. Network tab for actual error response

**Fix:**
1. Verify URLs exactly match your Render services
2. Restart both services from Render dashboard
3. Clear browser cache (Ctrl+Shift+Delete)
4. Redeploy frontend to rebuild with correct URLs

### Issue: Data Not Saving

**Check:**
1. POST request returns error (check Network tab)
2. Backend logs for exceptions
3. Data format matches expected structure

**Fix:**
1. Check Network response for error details
2. Review backend logs in Render
3. Ensure data types are correct

### Issue: Blank Dashboard or History

**Check:**
1. GET requests are failing
2. No data is being returned from backend
3. Frontend isn't processing response

**Fix:**
1. Check Network tab status codes
2. Verify backend data files exist
3. Restart backend service

## Performance Testing

After all tests pass:

1. **Response Time Test:**
   - First load might take 30 seconds (free tier spin-up)
   - Subsequent loads should be 1-3 seconds
   - This is normal on free tier

2. **Data Persistence Test:**
   - Submit data
   - Refresh page
   - Data should still appear
   - If lost, check backend data storage

3. **Multiple Actions Test:**
   - Submit several entries
   - Navigate between pages
   - Verify all data loads correctly

## Live Deployment Status

Once all tests pass successfully:

- Your application is live and accessible
- Share your frontend URL with others
- Users can access from anywhere
- Each code push to GitHub triggers auto-redeploy

## Important Notes

- Free tier services sleep after 15 minutes of inactivity
- First request after sleep takes ~30 seconds
- No data loss occurs during sleep
- Perfect for development and testing
\`\`\`
