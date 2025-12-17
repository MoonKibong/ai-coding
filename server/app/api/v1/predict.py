"""Disease Risk Prediction API endpoint."""

from fastapi import APIRouter, Depends
from loguru import logger

from app.core.config import settings
from app.schemas.disease_risk import PatientVitals, RiskAssessment
from app.services.risk_engine import RiskEngine, get_risk_engine

router = APIRouter(prefix="/predict", tags=["prediction"])


@router.post("", response_model=RiskAssessment, summary="Predict disease risk")
async def predict_risk(
    vitals: PatientVitals,
    engine: RiskEngine = Depends(get_risk_engine)
) -> RiskAssessment:
    """
    Predict disease risk based on patient vitals.
    
    This endpoint accepts patient vitals and returns a calculated disease risk score
    with visual explanations following the Disease Risk Analysis feature specification.
    
    Args:
        vitals: Patient vitals (age, BMI, blood pressure, smoking status)
        engine: RiskEngine service instance (dependency injection)
        
    Returns:
        RiskAssessment with risk score, level, and contributing factors
    """
    logger.info(f"Received prediction request for patient age={vitals.age}")
    
    result = await engine.predict(vitals)
    
    logger.info(f"Prediction completed: score={result.risk_score}, level={result.risk_level}")
    
    return result

