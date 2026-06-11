from fastapi import APIRouter, status, Depends, HTTPException, Header
from models.ai import ChatRequest, ChatResponse
from services.ai_router import ai_router_service, AIRouterService

router = APIRouter(tags=["Ronex AI Interactive Router Core"])

@router.post("/chat", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def chat(
    request: ChatRequest, 
    authorization: str = Header(..., description="Format: Bearer token_Username"),
    ai_service: AIRouterService = Depends(lambda: ai_router_service)
) -> ChatResponse:
    try:
        # Extract the user's name directly from the authentication token header
        if not authorization.startswith("Bearer token_"):
            raise HTTPException(status_code=401, detail="Invalid session token.")
        
        username = authorization.replace("Bearer token_", "").strip()
        return await ai_service.process_chat(request, username)
    except HTTPException as http_exc:
        raise http_exc
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ronex AI pipeline exception occurred evaluating current chat context structure."
        )
        
