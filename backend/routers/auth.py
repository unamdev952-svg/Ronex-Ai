from fastapi import APIRouter, status, HTTPException
from models.auth import LoginRequest, LoginResponse

router = APIRouter(tags=["User Authentication"])

@router.post(
    "/login", 
    response_model=LoginResponse, 
    status_code=status.HTTP_200_OK,
    summary="Logs in the user and establishes their session name"
)
async def login(request: LoginRequest) -> LoginResponse:
    if not request.username.strip():
        raise HTTPException(status_code=400, detail="Username cannot be empty")
    
    # In production, you can validate credentials here. 
    # For a direct workable session, we return the username as the auth token token.
    return LoginResponse(
        username=request.username.strip(),
        token=f"token_{request.username.strip()}"
    )
  
