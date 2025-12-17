/**
 * Composable for Disease Risk Prediction API calls.
 * 
 * Follows the pattern: Never call axios directly in components.
 * Use this composable for all risk prediction API interactions.
 */

import { ref, type Ref } from 'vue'
import axios from 'axios'

// Types matching backend schemas
export interface PatientVitals {
  age: number
  bmi: number
  systolic_bp: number
  is_smoker: boolean
}

export interface RiskAssessment {
  risk_score: number
  risk_level: 'LOW' | 'MODERATE' | 'HIGH'
  factors: Record<string, number>
}

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

export function useRiskPrediction() {
  const loading = ref(false)
  const error = ref<string | null>(null)
  const result: Ref<RiskAssessment | null> = ref(null)

  const predictRisk = async (vitals: PatientVitals): Promise<RiskAssessment | null> => {
    loading.value = true
    error.value = null
    result.value = null

    try {
      const response = await axios.post<RiskAssessment>(
        `${API_BASE_URL}/api/v1/predict`,
        vitals,
        {
          withCredentials: true, // Include credentials for session-based auth
          headers: {
            'Content-Type': 'application/json',
          },
        }
      )

      result.value = response.data
      return response.data
    } catch (err) {
      if (axios.isAxiosError(err)) {
        error.value = err.response?.data?.detail || err.message || 'Failed to predict risk'
      } else {
        error.value = 'An unexpected error occurred'
      }
      console.error('Risk prediction error:', err)
      return null
    } finally {
      loading.value = false
    }
  }

  return {
    loading,
    error,
    result,
    predictRisk,
  }
}

