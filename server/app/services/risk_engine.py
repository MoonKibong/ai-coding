"""Risk Engine Service - Implements Disease Risk Analysis logic following AI Service Layer pattern."""

import asyncio
from typing import Dict

from loguru import logger

from app.schemas.disease_risk import PatientVitals, RiskAssessment, RiskLevel


class RiskEngine:
    """
    Service class for disease risk prediction.
    
    Follows the AI Service Layer pattern:
    - Encapsulates all business logic
    - Async to prevent blocking
    - Dependency injectable
    """
    
    def __init__(self):
        """Initialize the risk engine."""
        self.baseline = 10.0
        logger.info("RiskEngine initialized")
    
    async def predict(self, vitals: PatientVitals) -> RiskAssessment:
        """
        Predict disease risk based on patient vitals.
        
        Implements heuristic logic as specified in DISEASE_RISK_ANALYSIS.md:
        1. Base score = 0
        2. If age > 50 → +20 points
        3. If bmi > 30 → +30 points
        4. If smoker → +25 points
        5. Must simulate 500ms delay to mimic model inference
        
        Args:
            vitals: Patient vitals input
            
        Returns:
            RiskAssessment with calculated risk score and factors
        """
        logger.info(f"Predicting risk for patient: age={vitals.age}, bmi={vitals.bmi}, "
                   f"bp={vitals.systolic_bp}, smoker={vitals.is_smoker}")
        
        # Simulate non-blocking async inference delay (500ms as per spec)
        await asyncio.sleep(0.5)
        
        # Initialize base score
        base_score = 0.0
        factors: Dict[str, float] = {}
        
        # Age factor: +20 if age > 50
        if vitals.age > 50:
            age_factor = 20.0
            base_score += age_factor
            factors["age_factor"] = age_factor
        else:
            factors["age_factor"] = 0.0
        
        # BMI factor: +30 if bmi > 30
        if vitals.bmi > 30:
            bmi_factor = 30.0
            base_score += bmi_factor
            factors["bmi_factor"] = bmi_factor
        else:
            factors["bmi_factor"] = 0.0
        
        # Smoker factor: +25 if smoker
        if vitals.is_smoker:
            smoker_factor = 25.0
            base_score += smoker_factor
            factors["smoker_factor"] = smoker_factor
        else:
            factors["smoker_factor"] = 0.0
        
        # Ensure score is within 0-100 range
        risk_score = min(100.0, max(0.0, base_score))
        
        # Determine risk level
        if risk_score < 30:
            risk_level = RiskLevel.LOW
        elif risk_score < 60:
            risk_level = RiskLevel.MODERATE
        else:
            risk_level = RiskLevel.HIGH
        
        logger.info(f"Risk prediction complete: score={risk_score}, level={risk_level}")
        
        return RiskAssessment(
            risk_score=risk_score,
            risk_level=risk_level,
            factors=factors
        )


# Dependency injection function
def get_risk_engine() -> RiskEngine:
    """Get RiskEngine instance (singleton pattern)."""
    return RiskEngine()

