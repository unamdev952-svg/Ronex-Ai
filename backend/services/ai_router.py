import logging
import asyncio
from models.ai import ChatRequest, ChatResponse
from config import settings

logger = logging.getLogger("ronex_ai_backend.services.ai_router")

class AIRouterService:
    """
    Unified AI Orchestration Service Layer. Normalizes API calls down 
    to a single gateway to prevent disclosing upstream partner providers to web or mobile nodes.
    """
    def __init__(self) -> None:
        self._secret_token = settings.UPSTREAM_PROVIDER_API_KEY

    async def process_chat(self, request: ChatRequest) -> ChatResponse:
        logger.info("AIRouterService processing client message thread inside Ronex matrix parameters.")
        
        # Simulating external structural payload travel latency safely without halting the async loop
        await asyncio.sleep(0.05)
        
        last_input = request.messages[-1].content if request.messages else ""
        controlled_output = f"Ronex AI engine response confirmed: Successfully evaluated context: '{last_input}'"
        
        return ChatResponse(
            answer=controlled_output,
            session_id="ronex-session-active-matrix"
        )

ai_router_service = AIRouterService()
