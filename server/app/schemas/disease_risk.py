"""Pydantic schemas for Disease Risk Analysis feature."""

from enum import Enum
from typing import Dict

from pydantic import BaseModel, Field


class RiskLevel(str, Enum):
    """Risk level enumeration."""
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"


class PatientVitals(BaseModel):
    """Input schema for patient vitals."""
    age: int = Field(..., ge=1, le=120, description="Patient age in years")
    bmi: float = Field(..., ge=10.0, le=60.0, description="Body Mass Index")
    systolic_bp: int = Field(..., ge=70, le=200, description="Systolic blood pressure")
    is_smoker: bool = Field(..., description="Smoking status")

    class Config:
        json_schema_extra = {
            "example": {
                "age": 45,
                "bmi": 24.5,
                "systolic_bp": 120,
                "is_smoker": False
            }
        }


class RiskAssessment(BaseModel):
    """Output schema for risk assessment."""
    risk_score: float = Field(..., ge=0.0, le=100.0, description="Risk score (0-100)")
    risk_level: RiskLevel = Field(..., description="Risk level category")
    factors: Dict[str, float] = Field(..., description="Contributing factors to the score")

    class Config:
        json_schema_extra = {
            "example": {
                "risk_score": 35.5,
                "risk_level": "LOW",
                "factors": {
                    "age_factor": 10.0,
                    "bmi_factor": 5.0
                }
            }
        }

