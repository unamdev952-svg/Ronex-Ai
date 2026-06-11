from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    username: str = Field(..., min_length=2, max_length=50, description="The name the user logs in with")

class LoginResponse(BaseModel):
    username: str = Field(..., description="Confirmed logged-in username")
    token: str = Field(..., description="Session token for authenticating chat requests")
