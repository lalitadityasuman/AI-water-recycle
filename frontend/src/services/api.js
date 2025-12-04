import axios from "axios"

const API_BASE = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000"

// Create axios instance
const api = axios.create({
  baseURL: API_BASE,
})

// Existing endpoint: submit usage
export default {
  submitUsage(data) {
    return api.post("/usage", data)
  },

  // Greywater
  getGreywater() {
    return api.get("/greywater")
  },

  // Recycle coins
  getCoins() {
    return api.get("/coins")
  },

  // AI recommendation
  getRecommendation() {
    return api.get("/recommendation")
  },

  // NEW: analyze-water endpoint
  analyzeWater(data) {
    return api.post("/analyze-water", data)
  },

  // NEW: summary of latest analysis
  getAnalysisSummary() {
    return api.get("/analysis-summary")
  },

  // NEW: recent history
  getHistory() {
    return api.get("/history")
  },
}
