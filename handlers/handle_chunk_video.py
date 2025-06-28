from faststream.rabbit import RabbitQueue, RabbitExchange, ExchangeType
from exchange import service_exchange
from app import app
from pydantic import BaseModel, Field
import uuid
import logging
from processors.process_chunk_video import process_chunk_video

logger = logging.getLogger("myapp")

class ChunkVideoRequest(BaseModel):
    request_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    videoUrl: str
    chuck_amount: int

api_name = "chuck_video"

request_listener = RabbitQueue(api_name, routing_key=f"{api_name}.request.*")
trigger_api_listener = RabbitQueue(api_name, routing_key="trigger_api.response.*")
trigger_api_exchange = RabbitExchange("trigger", type=ExchangeType.TOPIC)

broker = app.broker

@broker.subscriber(request_listener, service_exchange)
@broker.subscriber(trigger_api_listener, trigger_api_exchange)
@broker.publisher(routing_key=f"{api_name}.response.*", exchange=service_exchange)
async def handle_chuck_video(data: ChunkVideoRequest) -> ChunkVideoRequest:
    logger.info(f"Starting process {data}")
    result = await process_chunk_video(data)
    logger.info(f"Sending response {result}")
    return result
