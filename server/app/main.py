"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.api.v1 import router as v1_router
from app.core.config import settings

# Configure Loguru
logger.add(
    "logs/app.log",
    rotation="10 MB",
    retention="10 days",
    level="INFO"
)

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="MediPredict Lite - Disease Risk Analysis API"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vite default ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(v1_router)

@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "MediPredict Lite API",
        "version": settings.app_version,
        "docs": "/docs"
    }

@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=settings.debug)

