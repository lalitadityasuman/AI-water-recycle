from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os
from datetime import datetime
from ai_model import WastewaterQualityModel, generate_water_recommendation

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = FastAPI()
model = WastewaterQualityModel()

# -------------------------------
# CORS (Frontend at :5173)
# -------------------------------
frontend_url = os.getenv("FRONTEND_URL", "*")
cors_origins = []

if frontend_url == "*":
    cors_origins = ["*"]
else:
    # Allow both the frontend URL and localhost for development
    cors_origins = [frontend_url, "http://localhost:5173", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Data files
# -------------------------------
USAGE_FILE = "data/usage_log.json"
WATER_ANALYSIS_FILE = "data/water_analysis_log.json"

# Ensure data directory exists
if not os.path.exists("data"):
    os.makedirs("data")

# Ensure both log files exist
if not os.path.exists(USAGE_FILE):
    with open(USAGE_FILE, "w") as f:
        json.dump({"history": []}, f)

if not os.path.exists(WATER_ANALYSIS_FILE):
    with open(WATER_ANALYSIS_FILE, "w") as f:
        json.dump({"analysis": []}, f)

# -------------------------------
# Models
# -------------------------------
class UsageInput(BaseModel):
    shower: float
    washing_machine: float
    bathroom_sink: float
    kitchen_sink: float

class WaterAnalysisInput(BaseModel):
    turbidity: float
    pH: float
    tds: float
    temperature: float


# -------------------------------
# Helper
# -------------------------------
def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


# -------------------------------
# Greywater calculations
# -------------------------------
def calculate_greywater(entry):
    return (
        entry["shower"] * 0.7 +
        entry["washing_machine"] * 0.6 +
        entry["bathroom_sink"] * 0.5 + 
        entry["kitchen_sink"] * 0.2 
    )

def calculate_coins(greywater):
    return round(greywater / 10, 1)

def generate_recommendation(greywater):
    if greywater > 100:
        return "High reusable greywater available — ideal for gardening and toilet flushing."
    elif greywater > 50:
        return "Good amount of greywater available for toilet flushing."
    elif greywater > 20:
        return "Limited greywater available — suitable for mopping."
    else:
        return "Low greywater — consider capturing more from showers."


# -------------------------------
# Usage Endpoints
# -------------------------------
@app.post("/usage")
def add_usage(data: UsageInput):
    entry = data.dict()
    entry["total"] = entry["shower"] + entry["washing_machine"] + entry["bathroom_sink"] + entry["kitchen_sink"]
    entry["date"] = datetime.now().strftime("%Y-%m-%d %H:%M")

    db = load_json(USAGE_FILE)
    db["history"].append(entry)
    save_json(USAGE_FILE, db)

    return {"message": "Usage added successfully"}


@app.get("/greywater")
def get_greywater():
    db = load_json(USAGE_FILE)
    total = sum(calculate_greywater(e) for e in db["history"])
    return {"greywater": round(total, 2)}


@app.get("/coins")
def get_coins():
    db = load_json(USAGE_FILE)
    total = sum(calculate_greywater(e) for e in db["history"])
    return {"coins": calculate_coins(total)}


@app.get("/recommendation")
def get_recommendation():
    db = load_json(USAGE_FILE)
    total = sum(calculate_greywater(e) for e in db["history"])
    return {"recommendation": generate_recommendation(total)}


@app.get("/history")
def history():
    return load_json(USAGE_FILE)


# -------------------------------
# AI Water Quality Analysis
# -------------------------------
@app.post("/analyze-water")
def analyze_water(data: WaterAnalysisInput):
    values = data.dict()

    # Model prediction
    quality_idx = model.predict_quality(
        values["turbidity"],
        values["pH"],
        values["tds"],
        values["temperature"]
    )

    quality_label = ["High", "Medium", "Low"][quality_idx]
    recommendation = generate_water_recommendation(quality_idx)

    # Log entry
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "turbidity": values["turbidity"],
        "pH": values["pH"],
        "tds": values["tds"],
        "temperature": values["temperature"],
        "quality_level": quality_label,
        "recommendation": recommendation
    }

    db = load_json(WATER_ANALYSIS_FILE)
    db["analysis"].append(entry)
    save_json(WATER_ANALYSIS_FILE, db)

    return entry


# -------------------------------
# Dashboard Summary Endpoint
# -------------------------------
@app.get("/analysis-summary")
def analysis_summary():
    db = load_json(WATER_ANALYSIS_FILE)
    items = db["analysis"]

    if not items:
        return {
            "latest_report": None,
            "count": 0,
            "quality_distribution": {"High": 0, "Medium": 0, "Low": 0}
        }

    latest = items[-1]

    distribution = {"High": 0, "Medium": 0, "Low": 0}
    for a in items:
        distribution[a["quality_level"]] += 1

    return {
        "latest_report": latest,
        "count": len(items),
        "quality_distribution": distribution
    }
