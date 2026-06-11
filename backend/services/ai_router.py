import logging
import asyncio
from models.ai import ChatRequest, ChatResponse
from config import settings

logger = logging.getLogger("ronex_ai_backend.services.ai_router")

class AIRouterService:
    def __init__(self) -> None:
        self._secret_token = settings.UPSTREAM_PROVIDER_API_KEY

    async def process_chat(self, request: ChatRequest, username: str) -> ChatResponse:
        logger.info(f"AIRouterService processing chat for user: {username}")
        
        await asyncio.sleep(0.1) # Simulate network streaming/processing latency
        
        last_input = request.messages[-1].content if request.messages else ""
        
        # Personalized response using the logged-in user's name
        controlled_output = f"Hello {username}! I am Ronex AI. You just said: '{last_input}'. How can I assist you further today?"
        
        return ChatResponse(
            answer=controlled_output,
            session_id=f"ronex-session-{username}"
        )

ai_router_service = AIRouterService()
