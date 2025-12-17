"""API v1 routes."""

from fastapi import APIRouter

from app.api.v1.predict import router as predict_router
from app.core.config import settings

router = APIRouter(prefix=settings.api_v1_prefix)

router.include_router(predict_router)
