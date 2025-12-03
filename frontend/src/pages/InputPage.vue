<template>
  <div class="page-container">
    <h1 class="title">Water Usage & Quality Input</h1>

    <!-- -------------------- WATER USAGE SECTION --------------------- -->
    <section class="section-box">
      <h2 class="section-title">Daily Water Usage</h2>

      <form @submit.prevent="submitUsage" class="form-container">
        <div class="form-group">
          <label>Shower Usage (litres)</label>
          <input type="number" v-model.number="usageForm.shower" required />
        </div>

        <div class="form-group">
          <label>Washing Machine (litres)</label>
          <input type="number" v-model.number="usageForm.washing_machine" required />
        </div>

        <div class="form-group">
          <label>Bathroom Sink (litres)</label>
          <input type="number" v-model.number="usageForm.bathroom_sink" required />
        </div>

        <div class="form-group">
          <label>Kitchen Sink (litres)</label>
          <input type="number" v-model.number="usageForm.kitchen_sink" required />
        </div>

        <button type="submit" class="submit-btn">Submit Usage</button>
      </form>

      <p v-if="usageMsg" class="success-message">{{ usageMsg }}</p>
    </section>

    <!-- -------------------- WATER QUALITY SECTION --------------------- -->
    <section class="section-box">
      <h2 class="section-title">Wastewater Quality Analysis</h2>

      <form @submit.prevent="submitQuality" class="form-container">

        <div class="form-group">
          <label>Turbidity (NTU)</label>
          <input type="number" step="0.1" v-model.number="qualityForm.turbidity" required />
        </div>

        <div class="form-group">
          <label>pH Level</label>
          <input type="number" step="0.1" min="0" max="14" v-model.number="qualityForm.pH" required />
        </div>

        <div class="form-group">
          <label>TDS (mg/L)</label>
          <input type="number" v-model.number="qualityForm.tds" required />
        </div>

        <div class="form-group">
          <label>Temperature (°C)</label>
          <input type="number" step="0.1" v-model.number="qualityForm.temperature" required />
        </div>

        <button type="submit" class="submit-btn analyze-btn">Analyze Water</button>
      </form>

      <!-- Analysis result -->
      <div v-if="analysisResult" class="analysis-box">
        <h3>AI Analysis Result</h3>
        <p><strong>Quality Level:</strong> {{ analysisResult.quality_level }}</p>
        <p><strong>Recommendation:</strong> {{ analysisResult.recommendation }}</p>
      </div>

      <p v-if="qualityMsg" class="success-message">{{ qualityMsg }}</p>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import API from "../services/api";

export default {
  data() {
    return {
      usageForm: {
        shower: 0,
        washing_machine: 0,
        bathroom_sink: 0,
        kitchen_sink: 0,
      },
      qualityForm: {
        turbidity: null,
        pH: null,
        tds: null,
        temperature: null,
      },

      usageMsg: "",
      qualityMsg: "",
      analysisResult: null,
    };
  },

  methods: {
    // -------------------------------- WATER USAGE ------------------------------
    async submitUsage() {
      try {
        await API.submitUsage(this.usageForm);

        this.usageMsg = "Water usage submitted successfully!";

        this.usageForm = { shower: 0, washing_machine: 0, bathroom_sink: 0, kitchen_sink: 0 };

      } catch (err) {
        console.error(err);
        this.usageMsg = "Failed to submit usage.";
      }
    },

    // ------------------------------- WATER QUALITY -------------------------------
    async submitQuality() {
      try {
        const res = await axios.post("http://127.0.0.1:8000/analyze-water", this.qualityForm);
        this.analysisResult = res.data;

        this.qualityMsg = "Water quality analyzed successfully!";

        // Save to history for dashboard
        const history = JSON.parse(localStorage.getItem("history")) || [];
        history.push({
          ...this.qualityForm,
          result: res.data,
          time: new Date().toLocaleString(),
        });
        localStorage.setItem("history", JSON.stringify(history));

      } catch (err) {
        console.error(err);
        this.qualityMsg = "Failed to analyze water.";
      }
    },
  },
};
</script>

<style scoped>
.page-container {
  max-width: 600px;
  margin: auto;
  padding: 2rem;
}

.title {
  font-size: 2rem;
  text-align: center;
  margin-bottom: 1.5rem;
}

.section-box {
  padding: 1.5rem;
  margin-bottom: 2rem;
  background: #f8f9fa;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.06);
}

.section-title {
  font-size: 1.4rem;
  margin-bottom: 1rem;
  color: #34495e;
}

.form-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
}

input {
  padding: 0.6rem;
  font-size: 1rem;
}

.submit-btn {
  padding: 0.8rem;
  background-color: #42b883;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
}

.analyze-btn {
  background-color: #3498db;
}

.success-message {
  margin-top: 1rem;
  text-align: center;
  color: #2ecc71;
  font-weight: 500;
}

.analysis-box {
  margin-top: 1rem;
  background: #eaf6ff;
  padding: 1rem;
  border-left: 4px solid #3498db;
  border-radius: 6px;
}
</style>
