from fastapi import APIRouter, status, Depends, HTTPException
from models.ai import ChatRequest, ChatResponse
from services.ai_router import ai_router_service, AIRouterService

router = APIRouter(tags=["Ronex AI Interactive Router Core"])

@router.post(
    "/chat", 
    response_model=ChatResponse, 
    status_code=status.HTTP_200_OK,
    summary="Primary interface gateway executing requests across the integrated core engine."
)
async def chat(
    request: ChatRequest, 
    ai_service: AIRouterService = Depends(lambda: ai_router_service)
) -> ChatResponse:
    try:
        return await ai_service.process_chat(request)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ronex AI pipeline exception occurred evaluating current chat context structure."
        )
