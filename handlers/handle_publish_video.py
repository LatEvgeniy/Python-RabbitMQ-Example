import json
from json import JSONDecodeError
from pydantic import ValidationError
from processors.process_publish_video import process_publish_video
from faststream import Logger
from models.publish_video_models import PublishVideoRequest, PublishVideoResponse
from rabbit.broker import broker
from rabbit.queues import publish_video_response_queue, publish_video_request_queue
from rabbit.exchanges import video_publisher_service_exchange 

@broker.subscriber(publish_video_request_queue, video_publisher_service_exchange)
@broker.publisher(publish_video_response_queue, video_publisher_service_exchange)
async def handle_publish_video(message: bytes | dict, logger: Logger) -> PublishVideoResponse:
    logger.info("Publish video got request")

    try:
        raw_request = message if isinstance(message, dict) else json.loads(message.decode())
        request = PublishVideoRequest(**raw_request) 
        response = await process_publish_video(request)

    except (JSONDecodeError, ValidationError) as e:
        request_id = raw_request.get('request_id', 'unknown') if isinstance(e, ValidationError) else 'unknown'

        response = PublishVideoResponse(
            request_id=request_id,
            error_message=str(e)
        )
        logger.error(f"[{response.request_id}] Error while parsing/validating request")
        logger.debug(f"[{response.request_id}] Error: {str(e)}")
        
    return response
