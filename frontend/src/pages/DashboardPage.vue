<template>
  <div class="dashboard-container">
    <h1 class="title">Recycling Dashboard</h1>

    <!-- MAIN CARDS -->
    <div class="cards">

      <div class="card">
        <h2 class="card-title">Greywater Recovered</h2>
        <p class="value">{{ greywater }} L</p>
      </div>

      <div class="card">
        <h2 class="card-title">Recycle Coins</h2>
        <p class="value">{{ coins }}</p>
      </div>

      <div class="card recommendation">
        <h2 class="card-title">AI Recommendation</h2>
        <p class="recommendation-text">{{ recommendation }}</p>
      </div>

    </div>

    <!-- ANALYSIS SUMMARY -->
    <div class="analysis-section">
      <h2 class="section-title">Latest Analysis Summary</h2>

      <div class="analysis-card">
        <div class="analysis-card" v-if="analysisSummary">
          <p><strong>Quality:</strong> {{ analysisSummary.quality_level }}</p>
          <p><strong>Recommendation:</strong> {{ analysisSummary.recommendation }}</p>
          <p><strong>Date:</strong> {{ analysisSummary.date }}</p>

          <h3 class="sub-title">Water Metrics</h3>
          <p>Turbidity: {{ analysisSummary.turbidity }}</p>
          <p>pH: {{ analysisSummary.pH }}</p>
          <p>TDS: {{ analysisSummary.tds }}</p>
          <p>Temperature: {{ analysisSummary.temperature }}</p>
        </div>

        <p v-else class="loading-text">Loading latest analysis...</p>
      </div>
    </div>

    <!-- RECENT HISTORY -->
    <div class="history-section">
      <h2 class="section-title">Recent Usage History</h2>

      <ul class="history-list" v-if="history.length">
        <li v-for="(item, i) in history" :key="i" class="history-item">
          <span class="history-date">{{ item.date }}</span>
          <span class="history-details">
            Shower: {{ item.shower }}L, WM: {{ item.washing_machine }}L, Bath: {{ item.bathroom_sink }}L, Kitchen: {{ item.kitchen_sink }}L
          </span>
        </li>
      </ul>

      <p v-else class="loading-text">Loading history...</p>
    </div>

    <button class="refresh-btn" @click="loadDashboard">
      Refresh Dashboard
    </button>
  </div>
</template>

<script>
import API from "../services/api";

export default {
  data() {
    return {
      greywater: 0,
      coins: 0,
      recommendation: "Loading...",
      analysisSummary: "",
      history: []
    };
  },

  created() {
    this.loadDashboard();
  },

  methods: {
    async loadDashboard() {
      try {
        const grey = await API.getGreywater();
        const coin = await API.getCoins();
        const rec = await API.getRecommendation();
        const summary = await API.getAnalysisSummary();
        const historyList = await API.getHistory();

        this.greywater = grey.data.greywater;
        this.coins = coin.data.coins;
        this.recommendation = rec.data.recommendation;
        this.analysisSummary = summary.data.latest_report ?? null;
        this.history = historyList.data.history;

      } catch (err) {
        console.error(err);
        this.recommendation = "Unable to load data.";
      }
    }
  }
};
</script>

<style scoped>
.dashboard-container {
  max-width: 900px;
  margin: auto;
  padding: 2rem;
}

/* Titles */
.title {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 2rem;
  font-weight: 600;
  color: #333;
}

.section-title {
  margin-top: 2rem;
  font-size: 1.5rem;
  font-weight: 600;
  color: #444;
}

/* Cards Layout */
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 1.8rem;
  justify-content: center;
}

.card {
  width: 280px;
  background: white;
  padding: 1.8rem;
  border-radius: 14px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  text-align: center;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 18px rgba(0,0,0,0.12);
}

.card-title {
  font-size: 1.3rem;
  margin-bottom: 1rem;
  color: #555;
  font-weight: 600;
}

.value {
  font-size: 2.4rem;
  color: #42b883;
  font-weight: bold;
}

.recommendation {
  background: #e9f9f0;
  border-left: 5px solid #42b883;
}

.recommendation-text {
  margin-top: 0.8rem;
  font-size: 1.1rem;
  color: #333;
}

/* Analysis Summary */
.analysis-card {
  margin-top: 1rem;
  background: #f9fafb;
  padding: 1.6rem;
  border-radius: 10px;
  box-shadow: 0 3px 10px rgba(0,0,0,0.06);
  font-size: 1.1rem;
  line-height: 1.5rem;
  color: #333;
}

/* History List */
.history-section {
  margin-top: 2rem;
}

.history-list {
  list-style: none;
  margin: 1rem 0 0 0;
  padding: 0;
}

.history-item {
  padding: 0.9rem 1rem;
  background: white;
  margin-bottom: 0.7rem;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.06);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.history-date {
  font-weight: 600;
  color: #35495e;
}

.history-details {
  font-size: 0.95rem;
  color: #444;
}

.loading-text {
  margin-top: 1rem;
  color: #888;
  text-align: center;
}

/* Refresh Button */
.refresh-btn {
  margin: 2.5rem auto 0 auto;
  display: block;
  padding: 0.9rem 1.8rem;
  background: #35495e;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1.1rem;
  transition: background 0.2s ease;
}

.refresh-btn:hover {
  background: #2c3e50;
}
</style>
