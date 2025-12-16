# Pattern: AI Inference Service

**Context**: Integrating heavy Python processing (AI Models) into FastAPI.

## The Problem
Running AI inference directly inside a route handler blocks the request and makes testing difficult. Logic is often scattered across API endpoints.

### ❌ Anti-Pattern: Logic in Router

```python
# BAD: Logic tightly coupled to HTTP layer
@router.post("/predict")
def predict(vitals: Vitals):
    # Complex logic mixed with API code
    score = vitals.age * 0.5 
    time.sleep(1) # Blocks the thread!
    return {"score": score}
```

## Solution: The Service Layer Pattern
Isolate all "Smart" logic into a dedicated Service class. The Router only handles HTTP (request parsing, response formatting).

✅ Correct Pattern: Dependency Injection

1. Service Class: Encapsulates the logic (or model loading).

2. Dependency: Injected into the router.

```python
# services/inference.py
class RiskEngine:
    def __init__(self):
        # Load heavy models here (simulated)
        self.baseline = 10.0

    async def predict(self, vitals: PatientVitals) -> RiskAssessment:
        await asyncio.sleep(0.5) # Simulate non-blocking async inference
        # ... logic ...
        return result

# api/routes.py
@router.post("/predict")
async def predict_risk(
    vitals: PatientVitals, 
    engine: RiskEngine = Depends(get_risk_engine) # Dependency Injection
):
    return await engine.predict(vitals)
```

## Frontend Integration

- Composables: Never call axios directly in components. Use the useRiskPrediction composable.

- Loading State: The frontend MUST handle the await delay with a loading spinner.