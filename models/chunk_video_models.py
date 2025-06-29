from pydantic import BaseModel, Field
import uuid

class ChunkVideoRequest(BaseModel):
    request_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    video_url: str
    chunk_amount: int

class ChunkVideoResponse(BaseModel):
    request_id: str
    status: str = Field(default="success")
    error_message: str | None = None