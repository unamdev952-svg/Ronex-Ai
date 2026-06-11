from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class ChatMessage(BaseModel):
    role: str = Field(..., description="The role entity of the message writer, e.g., 'user' or 'assistant'.")
    content: str = Field(..., description="The string raw text content of the message.")

class ChatRequest(BaseModel):
    messages: List[ChatMessage] = Field(..., description="Thread logs representing the sequential history of the chat session.")
    stream: bool = Field(default=False, description="Specifies if the runtime requires buffered data or partial chunk streams.")
    context_override: Optional[Dict[str, Any]] = Field(default=None, description="Metadata dictionary container for system-level configuration parameters.")

class ChatResponse(BaseModel):
    answer: str = Field(..., description="The resulting text response delivered under the explicit Ronex AI brand infrastructure.")
    session_id: Optional[str] = Field(default=None, description="Unique string tracking token correlating to the underlying persistent state storage indexes.")
  
