import json
from json import JSONDecodeError
from pydantic import ValidationError
from faststream import Logger
from processors.process_chunk_video import process_chunk_video
from models.chunk_video_models import ChunkVideoRequest, ChunkVideoResponse
from rabbit.broker import broker
from rabbit.queues import chuck_video_request_queue, chuck_video_response_queue, publish_video_response_queue
from rabbit.exchanges import video_processor_service_exchange, video_publisher_service_exchange 

@broker.subscriber(publish_video_response_queue, video_publisher_service_exchange)
@broker.subscriber(chuck_video_request_queue, video_processor_service_exchange)
@broker.publisher(chuck_video_response_queue, video_processor_service_exchange)
async def handle_chunk_video(message: bytes | dict, logger: Logger) -> ChunkVideoResponse:
    logger.info("Chuck video got request")

    try:
        raw_request = message if isinstance(message, dict) else json.loads(message.decode())
        request = ChunkVideoRequest(**raw_request) 
        response = await process_chunk_video(request)
        
    except (JSONDecodeError, ValidationError) as e:
        request_id = raw_request.get('request_id', 'unknown') if isinstance(e, ValidationError) else 'unknown'

        response = ChunkVideoResponse(
            request_id=request_id,
            status="error",
            error_message=str(e)
        )
        logger.error(f"[{response.request_id}] Error while parsing/validating request")
        logger.debug(f"[{response.request_id}] Error: {str(e)}")

    return response
