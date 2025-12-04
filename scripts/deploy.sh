#!/bin/bash

# RecycleAI Deployment Helper Script

echo "RecycleAI Deployment Assistant"
echo "=============================="
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit for Railway deployment"
fi

echo "Deployment Checklist:"
echo "✓ Backend code prepared"
echo "✓ Frontend code prepared"
echo "✓ Docker configurations ready"
echo ""

echo "Next steps:"
echo "1. Push code to GitHub:"
echo "   git push origin main"
echo ""
echo "2. Go to https://railway.app"
echo "3. Create new project from GitHub"
echo "4. Deploy backend service (root: backend/)"
echo "5. Deploy frontend service (root: frontend/)"
echo "6. Set environment variables (see DEPLOYMENT.md)"
echo "7. Verify both services deployed successfully"
echo ""
echo "For more details, see DEPLOYMENT.md"
