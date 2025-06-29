from pydantic import BaseModel, Field
import uuid

class PublishVideoRequest(BaseModel):
    request_id: str = Field(default_factory=lambda: str(uuid.uuid4()))

class PublishVideoResponse(BaseModel):
    request_id: str
    video_url: str | None = None
    error_message: str | None = None