from faststream.rabbit import RabbitQueue, RabbitExchange, ExchangeType
from rabbit import service_exchange
from processors.process_chunk_video import process_chunk_video
from rabbit import broker
from faststream import Logger
from models.chunk_video_mobels import ChunkVideoRequest, ChunkVideoResponse

api_name = "chunk_video"

request_listener = RabbitQueue(api_name, routing_key=f"{api_name}.request.*")
#trigger_api_listener = RabbitQueue(api_name, routing_key="trigger_api.response.*")
#trigger_api_exchange = RabbitExchange("trigger", type=ExchangeType.TOPIC)

@broker.subscriber(request_listener, service_exchange)
#@broker.subscriber(trigger_api_listener, trigger_api_exchange)
@broker.publisher(routing_key=f"{api_name}.response.*", exchange=service_exchange)
async def handle_chunk_video(data: ChunkVideoRequest, logger: Logger) -> ChunkVideoResponse:
    logger.info(f"Starting process {data}")
    result = await process_chunk_video(data)
    logger.info(f"Sending response {result}")
    return result
