<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-title class="text-h5 mb-4">
            Disease Risk Analysis
          </v-card-title>

          <v-card-text>
            <!-- Input Section -->
            <v-row>
              <v-col cols="12" md="6">
                <v-card variant="outlined" class="pa-4">
                  <v-card-title class="text-h6 mb-4">Patient Vitals</v-card-title>

                  <!-- Age Slider -->
                  <v-slider
                    v-model="vitals.age"
                    label="Age"
                    :min="1"
                    :max="120"
                    :step="1"
                    thumb-label
                    class="mb-4"
                  >
                    <template #append>
                      <v-text-field
                        v-model.number="vitals.age"
                        type="number"
                        style="width: 100px"
                        density="compact"
                        hide-details
                        variant="outlined"
                      />
                    </template>
                  </v-slider>

                  <!-- BMI Slider -->
                  <v-slider
                    v-model="vitals.bmi"
                    label="BMI"
                    :min="10"
                    :max="60"
                    :step="0.1"
                    thumb-label
                    class="mb-4"
                  >
                    <template #append>
                      <v-text-field
                        v-model.number="vitals.bmi"
                        type="number"
                        style="width: 100px"
                        density="compact"
                        hide-details
                        variant="outlined"
                      />
                    </template>
                  </v-slider>

                  <!-- Blood Pressure Slider -->
                  <v-slider
                    v-model="vitals.systolic_bp"
                    label="Systolic BP"
                    :min="70"
                    :max="200"
                    :step="1"
                    thumb-label
                    class="mb-4"
                  >
                    <template #append>
                      <v-text-field
                        v-model.number="vitals.systolic_bp"
                        type="number"
                        style="width: 100px"
                        density="compact"
                        hide-details
                        variant="outlined"
                      />
                    </template>
                  </v-slider>

                  <!-- Smoker Switch -->
                  <v-switch
                    v-model="vitals.is_smoker"
                    label="Smoker"
                    color="primary"
                    class="mb-4"
                  />

                  <!-- Predict Button -->
                  <v-btn
                    color="primary"
                    size="large"
                    block
                    :loading="loading"
                    :disabled="loading"
                    @click="handlePredict"
                  >
                    Predict Risk
                  </v-btn>
                </v-card>
              </v-col>

              <!-- Result Section -->
              <v-col cols="12" md="6">
                <v-card variant="outlined" class="pa-4">
                  <v-card-title class="text-h6 mb-4">Risk Assessment</v-card-title>

                  <!-- Error Display -->
                  <v-alert
                    v-if="error"
                    type="error"
                    class="mb-4"
                    closable
                    @click:close="error = null"
                  >
                    {{ error }}
                  </v-alert>

                  <!-- Loading State -->
                  <div v-if="loading" class="text-center pa-8">
                    <v-progress-circular
                      indeterminate
                      color="primary"
                      size="64"
                    />
                    <p class="mt-4">Analyzing risk factors...</p>
                  </div>

                  <!-- Results Display -->
                  <div v-else-if="result">
                    <!-- Risk Score Gauge -->
                    <div class="mb-6">
                      <h3 class="text-h6 mb-2">Overall Risk Score</h3>
                      <canvas ref="gaugeChart"></canvas>
                    </div>

                    <!-- Risk Level Badge -->
                    <v-chip
                      :color="getRiskColor(result.risk_level)"
                      size="large"
                      class="mb-4"
                    >
                      {{ result.risk_level }} RISK
                    </v-chip>

                    <!-- Contributing Factors -->
                    <div class="mb-4">
                      <h4 class="text-subtitle-1 mb-2">Contributing Factors</h4>
                      <v-list density="compact">
                        <v-list-item
                          v-for="(value, key) in result.factors"
                          :key="key"
                        >
                          <template #prepend>
                            <v-icon>mdi-circle-small</v-icon>
                          </template>
                          <v-list-item-title>
                            {{ formatFactorName(key) }}: {{ value.toFixed(1) }}
                          </v-list-item-title>
                        </v-list-item>
                      </v-list>
                    </div>

                    <!-- Radar Chart -->
                    <div>
                      <h4 class="text-subtitle-1 mb-2">Patient vs Healthy Baseline</h4>
                      <canvas ref="radarChart"></canvas>
                    </div>
                  </div>

                  <!-- No Results State -->
                  <v-alert
                    v-else
                    type="info"
                    variant="tonal"
                  >
                    Enter patient vitals and click "Predict Risk" to see results.
                  </v-alert>
                </v-card>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref, onMounted, watch, nextTick } from 'vue'
import {
  Chart,
  ArcElement,
  Tooltip,
  Legend,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
} from 'chart.js'
import { useRiskPrediction, type PatientVitals, type RiskAssessment } from '../composables/useRiskPrediction'

// Register Chart.js components
Chart.register(ArcElement, Tooltip, Legend, RadialLinearScale, PointElement, LineElement, Filler)

// Composable
const { loading, error, result, predictRisk } = useRiskPrediction()

// Form data
const vitals = ref<PatientVitals>({
  age: 45,
  bmi: 24.5,
  systolic_bp: 120,
  is_smoker: false,
})

// Chart refs
const gaugeChart = ref<HTMLCanvasElement | null>(null)
const radarChart = ref<HTMLCanvasElement | null>(null)

let gaugeChartInstance: Chart | null = null
let radarChartInstance: Chart | null = null

// Handle prediction
const handlePredict = async () => {
  await predictRisk(vitals.value)
  await nextTick()
  if (result.value) {
    updateCharts()
  }
}

// Update charts when result changes
watch(result, () => {
  if (result.value) {
    nextTick(() => {
      updateCharts()
    })
  }
})

// Update both charts
const updateCharts = () => {
  if (!result.value) return

  updateGaugeChart()
  updateRadarChart()
}

// Update gauge chart
const updateGaugeChart = () => {
  if (!gaugeChart.value || !result.value) return

  const score = result.value.risk_score
  const color = getRiskColor(result.value.risk_level)

  // Destroy existing chart
  if (gaugeChartInstance) {
    gaugeChartInstance.destroy()
  }

  // Create gauge chart (doughnut chart as gauge)
  gaugeChartInstance = new Chart(gaugeChart.value, {
    type: 'doughnut',
    data: {
      datasets: [{
        data: [score, 100 - score],
        backgroundColor: [color, '#e0e0e0'],
        borderWidth: 0,
      }],
    },
    options: {
      cutout: '75%',
      plugins: {
        legend: {
          display: false,
        },
        tooltip: {
          callbacks: {
            label: (context) => {
              if (context.dataIndex === 0) {
                return `Risk Score: ${score.toFixed(1)}`
              }
              return ''
            },
          },
        },
      },
    },
    plugins: [{
      id: 'gaugeLabel',
      beforeDraw: (chart) => {
        const ctx = chart.ctx
        const centerX = chart.chartArea.left + (chart.chartArea.right - chart.chartArea.left) / 2
        const centerY = chart.chartArea.top + (chart.chartArea.bottom - chart.chartArea.top) / 2

        ctx.save()
        ctx.font = 'bold 24px Arial'
        ctx.fillStyle = color
        ctx.textAlign = 'center'
        ctx.textBaseline = 'middle'
        ctx.fillText(score.toFixed(1), centerX, centerY)
        ctx.restore()
      },
    }],
  })
}

// Update radar chart
const updateRadarChart = () => {
  if (!radarChart.value || !result.value) return

  // Destroy existing chart
  if (radarChartInstance) {
    radarChartInstance.destroy()
  }

  // Normalize patient data for radar chart (as per spec)
  const patientData = [
    vitals.value.age / 100,      // Age normalized
    vitals.value.bmi / 50,       // BMI normalized
    vitals.value.systolic_bp / 200, // BP normalized
  ]

  // Healthy baseline (as per spec)
  const healthyBaseline = [0.3, 0.4, 0.6]

  radarChartInstance = new Chart(radarChart.value, {
    type: 'radar',
    data: {
      labels: ['Age', 'BMI', 'Blood Pressure'],
      datasets: [
        {
          label: 'Patient',
          data: patientData,
          borderColor: 'rgb(75, 192, 192)',
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          pointBackgroundColor: 'rgb(75, 192, 192)',
        },
        {
          label: 'Healthy Baseline',
          data: healthyBaseline,
          borderColor: 'rgb(255, 99, 132)',
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          pointBackgroundColor: 'rgb(255, 99, 132)',
        },
      ],
    },
    options: {
      scales: {
        r: {
          beginAtZero: true,
          max: 1,
        },
      },
      plugins: {
        legend: {
          display: true,
          position: 'top',
        },
      },
    },
  })
}

// Helper functions
const getRiskColor = (level: string): string => {
  switch (level) {
    case 'LOW':
      return '#4caf50' // Green
    case 'MODERATE':
      return '#ff9800' // Orange/Yellow
    case 'HIGH':
      return '#f44336' // Red
    default:
      return '#757575' // Grey
  }
}

const formatFactorName = (key: string): string => {
  return key
    .replace(/_/g, ' ')
    .replace(/\b\w/g, (l) => l.toUpperCase())
}

// Initialize charts on mount
onMounted(() => {
  // Charts will be created when results are available
})
</script>

<style scoped>
canvas {
  max-width: 100%;
  height: auto;
}
</style>

