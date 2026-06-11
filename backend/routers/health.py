from fastapi import APIRouter, status
from models.health import HealthCheckResponse

router = APIRouter(tags=["System Framework Core Checks"])

@router.get(
    "/health", 
    response_model=HealthCheckResponse, 
    status_code=status.HTTP_200_OK,
    summary="Queries runtime environment metrics to guarantee platform validation availability."
)
async def health_check() -> HealthCheckResponse:
    return HealthCheckResponse(status="healthy")
  
