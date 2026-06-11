from pydantic import BaseModel, Field

class HealthCheckResponse(BaseModel):
    status: str = Field(..., description="Global health string state checking indicator for monitoring software arrays.")
  
