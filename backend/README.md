🔧 1. Install Prerequisites

Ensure you have:

Python 3.11+

pip

🧪 2. Create a Virtual Environment (Recommended)

macOS / Linux
python3 -m venv .venv
source ./.venv/bin/activate

Windows
python -m venv .venv
.\.venv\Scripts\activate

📦 3. Install Dependencies
pip install -r requirements.txt

▶️ 4. Run the FastAPI Server

Inside the backend folder:

uvicorn main:app --reload

This runs the server with auto-reload on file changes.

🌐 5. API Documentation

Once running:

Swagger UI

👉 http://127.0.0.1:8000/docs
