<template>
  <div class="history-container">
    <h1 class="title">Usage History</h1>

    <button class="refresh-btn" @click="loadHistory">Refresh</button>

    <table v-if="history.length > 0" class="history-table">
      <thead>
        <tr>
          <th>Date</th>
          <th>Shower (L)</th>
          <th>Washing Machine (L)</th>
          <th>Bathroom Sink (L)</th>
          <th>Kitchen Sink (L)</th>
          <th>Total (L)</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="(entry, index) in history" :key="index">
          <td>{{ entry.date }}</td>
          <td>{{ entry.shower }}</td>
          <td>{{ entry.washing_machine }}</td>
          <td>{{ entry.bathroom_sink }}</td>
          <td>{{ entry.kitchen_sink }}</td>
          <td>{{ entry.total }}</td>
        </tr>
      </tbody>
    </table>

    <p v-else class="no-data">No history available.</p>
  </div>
</template>

<script>
import API from "../services/api";

export default {
  data() {
    return {
      history: [],
    };
  },

  created() {
    this.loadHistory();
  },

  methods: {
    async loadHistory() {
      try {
        const res = await API.getHistory();
        this.history = res.data.history;
      } catch (err) {
        console.error(err);
      }
    },
  },
};
</script>

<style scoped>
.history-container {
  max-width: 900px;
  margin: auto;
  padding: 2rem;
}

.title {
  text-align: center;
  margin-bottom: 1.5rem;
}

.refresh-btn {
  margin-bottom: 1rem;
  padding: 0.6rem 1.2rem;
  background: #42b883;
  border: none;
  color: white;
  border-radius: 5px;
  display: block;
  margin-left: auto;
  cursor: pointer;
}

.history-table {
  width: 100%;
  border-collapse: collapse;
}

.history-table th,
.history-table td {
  padding: 0.7rem;
  border: 1px solid #ddd;
  text-align: center;
}

.no-data {
  text-align: center;
  color: #777;
  margin-top: 1rem;
}
</style>
