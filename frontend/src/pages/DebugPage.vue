<template>
  <div class="debug-page">
    <h2>Debug Information</h2>
    
    <div class="debug-section">
      <h3>API Configuration</h3>
      <p><strong>API Base URL:</strong> {{ apiUrl }}</p>
      <p><strong>Environment:</strong> {{ environment }}</p>
    </div>

    <div class="debug-section">
      <h3>API Connectivity Test</h3>
      <button @click="testBackend">Test Backend Connection</button>
      <p v-if="connectionStatus" :class="{ success: connectionStatus.success }">
        {{ connectionStatus.message }}
      </p>
    </div>

    <div class="debug-section">
      <h3>Data Summary</h3>
      <p v-if="dataSummary">
        <strong>Total History Records:</strong> {{ dataSummary.totalRecords }}<br>
        <strong>Last Updated:</strong> {{ dataSummary.lastUpdate }}
      </p>
    </div>

    <div class="debug-section">
      <h3>Recent History</h3>
      <pre v-if="history">{{ JSON.stringify(history.history.slice(-3), null, 2) }}</pre>
    </div>
  </div>
</template>

<script>
import api from '@/services/api'

export default {
  name: 'DebugPage',
  data() {
    return {
      apiUrl: import.meta.env.VITE_API_URL || 'http://localhost:8000',
      environment: import.meta.env.MODE,
      connectionStatus: null,
      dataSummary: null,
      history: null,
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async testBackend() {
      try {
        const response = await api.getHistory()
        this.connectionStatus = {
          success: true,
          message: 'Backend connected successfully!'
        }
      } catch (error) {
        this.connectionStatus = {
          success: false,
          message: `Connection failed: ${error.message}`
        }
      }
    },
    async loadData() {
      try {
        this.history = await api.getHistory()
        this.dataSummary = {
          totalRecords: this.history.history.length,
          lastUpdate: this.history.history[this.history.history.length - 1]?.date || 'N/A'
        }
      } catch (error) {
        console.error('Error loading data:', error)
      }
    }
  }
}
</script>

<style scoped>
.debug-page {
  padding: 20px;
  font-family: monospace;
}

.debug-section {
  margin-bottom: 20px;
  padding: 15px;
  background: #f5f5f5;
  border-radius: 4px;
  border-left: 4px solid #42b983;
}

.debug-section h3 {
  margin-top: 0;
  color: #333;
}

button {
  padding: 10px 20px;
  background: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background: #359970;
}

.success {
  color: #42b983;
  font-weight: bold;
}

pre {
  background: #fff;
  padding: 10px;
  border-radius: 4px;
  overflow-x: auto;
  max-height: 300px;
}
</style>
