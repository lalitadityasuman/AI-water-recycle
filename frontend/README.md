📦 1. Install Prerequisites

You need:

Node.js 20+

npm or yarn

Check versions:

node -v
npm -v

📥 2. Install Dependencies

Inside the frontend folder:

npm install

▶️ 3. Run the Development Server

npm run dev

Vite will start at:

👉 http://localhost:5173

🔌 4. Backend Connection

The frontend uses this API base URL:

http://localhost:8000

This is defined inside:

src/services/api.js

Make sure the backend (FastAPI) is running